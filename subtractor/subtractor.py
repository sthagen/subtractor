# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,invalid-name,line-too-long,logging-fstring-interpolation
"""Do the diff."""
import logging
import pathlib
import subprocess
import sys

from subtractor.pixel import diff_img, shape_of_png
import subtractor.pixel as pixel  # To access pixel.OPTIONS["threshold"]
from subtractor.stream import final_suffix_in, visit

ENCODING = "utf-8"

APP = "subtractor"

LOG = logging.getLogger()  # Temporary refactoring: module level logger
LOG_FOLDER = pathlib.Path("logs")
LOG_FILE = f"{APP}.log"
LOG_PATH = (
    pathlib.Path(LOG_FOLDER, LOG_FILE)
    if LOG_FOLDER.is_dir()
    else pathlib.Path(LOG_FILE)
)
LOG_LEVEL = logging.INFO

FAILURE_PATH_REASON = "Failed action for path %s with error: %s"

VISIT_OPTIONS = {
    "pre_filter": sorted,
    "pre_filter_options": {"reverse": True},
    "post_filter": final_suffix_in,
    "post_filter_options": {"suffixes": (".png",)},
}

SLUG_CAP = 164
SLUG_ETC = " ..."

DSL_MAIN_SPLIT = ":$file:"
DSL_SUB_SPLIT = ":$name:"


def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global LOG  # pylint: disable=global-statement

    log_format = {
        "format": "%(asctime)s.%(msecs)03d %(levelname)s [%(name)s]: %(message)s",
        "datefmt": "%Y-%m-%dT%H:%M:%S",
        # 'filename': LOG_PATH,
        "level": LOG_LEVEL if level is None else level,
    }
    logging.basicConfig(**log_format)
    LOG = logging.getLogger(APP if name is None else name)
    LOG.propagate = True


def slugify(thing, these=('\n',), those=(' ',)) -> str:
    """Replace these (default: new lines) by those (default: space) and return string of thing."""
    if not these or not those:
        return str(thing)
    if len(these) < len(those):
        raise ValueError("slugify called with more replacement targets than sources")
    if len(those) == 1:
        that = those[0]  # HACK A DID ACK
        if len(these) == 1:
            these = these[0]
            return str(thing).replace(these, that)
        hook = str(thing)
        for this in these:
            hook = hook.replace(this, that)
        return hook

    hook = str(thing)
    for this, that in zip(these, those):
        hook = hook.replace(this, that)
    return hook


def file_has_content(path: pathlib.Path) -> (bool, str):
    """Simplistic handler to develop generic processing function."""
    if not path.is_file():
        return False, f"{path} is no file"
    byte_size = path.stat().st_size
    return byte_size > 0, str(byte_size)


def process(path, handler, success, failure):
    """Generic processing of path yields a,ended COHDA protocol."""
    valid, message = handler(path)
    if valid:
        return True, message, success + 1, failure

    return False, message, success, failure + 1


def process_pair(invoke, good, bad, obs_path, present, ref_path):
    """The main per pair processing code."""
    LOG.info("Pair ref=%s, obs=%s", ref_path, obs_path)
    if ref_path and obs_path:
        ok_ref, size, _, _ = process(ref_path, file_has_content, good, bad)
        LOG.info("  Found ref=%s to be %s with size %s bytes", ref_path, "OK" if ok_ref else "NOK", size)
        ok_ref, width, height, info = shape_of_png(ref_path)
        LOG.info("    Analyzed ref=%s as PNG to be %s with %s",
                 ref_path, "OK" if ok_ref else "NOK", f"shape {width}x{height}" if ok_ref else info["error"])
        ok_obs, size, _, _ = process(obs_path, file_has_content, good, bad)
        LOG.info("  Found obs=%s to be %s with size %s bytes", obs_path, "OK" if ok_obs else "NOK", size)
        ok_obs, width, height, info = shape_of_png(obs_path)
        LOG.info("    Analyzed obs=%s as PNG to be %s with %s",
                 obs_path, "OK" if ok_obs else "NOK", f"shape {width}x{height}" if ok_obs else info["error"])
        present_path = pathlib.Path(present, f"diff-of-{obs_path.parts[-1]}") if present.is_dir() else present
        if not all([ok_ref, ok_obs]):
            bad += 1
        else:
            if not invoke:
                pixel_count = width * height
                mismatch, _, _ = diff_img(ref_path, obs_path, present_path)
                if mismatch:
                    LOG.info("  Mismatch of obs=%s is %d of %d pixels or %0.1f %%",
                             obs_path, mismatch, pixel_count, round(100 * mismatch / pixel_count, 1))
                    bad += 1
                else:
                    LOG.info("  Match of obs=%s", obs_path)
                    good += 1
            else:
                args = invoke["executor"].replace("$ref", str(ref_path)).replace("$obs", str(obs_path)).split()
                if invoke["param_file_name"]:
                    param_file_content = invoke["param_file_content"].replace("$ref", str(ref_path)).replace("$obs", str(obs_path))
                    with open(invoke["param_file_name"], "wt", encoding=ENCODING) as handle:
                        handle.write(param_file_content)
                completed = subprocess.run(args, capture_output=True, check=True)
                if not completed.returncode:
                    good += 1
                else:
                    bad += 1
                slug = slugify(completed.stdout)
                if len(slug) > SLUG_CAP:
                    slug = slug[:SLUG_CAP] + SLUG_ETC
                LOG.info(slug)
    else:
        bad += 1

    return good, bad


def present_from(ref: pathlib.Path, obs: pathlib.Path) -> pathlib.Path:
    """Build a somehow least surprising difference folder from ref and obs."""
    ref_code = ref.parts[-1]
    if obs.is_file():
        return pathlib.Path(*obs.parts[:-1], f"diff-of-{obs.parts[-1]}")

    present = pathlib.Path(*obs.parts[:-1], f"diff-of-{ref_code}_{obs.parts[-1]}")
    present.mkdir(parents=True, exist_ok=True)
    return present


def causal_triplet(trunks) -> tuple:
    """Generate past, present, and future from trunks or include a present of None."""
    past, future = tuple(pathlib.Path(entry) for entry in trunks[:2])

    if any([past.is_dir(), future.is_dir()]):
        consistent_args = past.is_dir() and future.is_dir()
    elif any([past.is_file(), future.is_file()]):
        consistent_args = past.is_file() and future.is_file()
    else:
        consistent_args = False
    if not consistent_args:
        return past, None, future

    present = pathlib.Path(trunks[-1]) if len(trunks) == 3 else present_from(past, future)
    return past, present, future


class Splicer:
    """Hollow splicer - split and merge."""
    @staticmethod
    def split(thing):
        """Split thing into things."""
        return thing.parts[:-1], thing.parts[-1]

    @staticmethod
    def merge(left, right):
        """Merge left and right back into thing."""
        return pathlib.Path(left, right)


def names_of(root, splicer: Splicer, options):
    """Yield file names of root."""
    for path in visit(root, **options):
        yield splicer.split(path)


def matching_zipper(ref, obs, splicer: Splicer, gen, gen_options: dict):
    """Generate a complete matching zipper for the longest matching sequence."""
    x_p = {name: (name, None) for _, name in gen(ref, splicer, gen_options)}
    for _, name in gen(obs, splicer, gen_options):
        x_p[name] = (name, name) if name in x_p else (None, name)
    for key in sorted(x_p):
        r, o = x_p[key]
        yield (
            r if r is None else splicer.merge(ref, r),
            o if o is None else splicer.merge(obs, o)
        )


def parse_template(text):
    """Hack to return exec and param file template until config language is clear."""
    if DSL_MAIN_SPLIT in text:
        LOG.info("Detected magic (%s) in template", DSL_MAIN_SPLIT)
        executor, rest = text.split(DSL_MAIN_SPLIT)
        try:
            content, name = rest.split(DSL_SUB_SPLIT)
        except ValueError:
            LOG.critical("Template with (%s) lacks (%s) to link executor part (%s) with param file content via name.",
                         DSL_MAIN_SPLIT, DSL_SUB_SPLIT, executor)
            raise
        executor = {"executor": executor, "param_file_content": content, "param_file_name": name}
    else:
        executor = {"executor": text, "param_file_content": None, "param_file_name": None}
    LOG.info("Parsed diff template (%s) into executor ...", text)
    LOG.info(" ...   into executor (%s)", str(executor))
    return executor


def main(argv=None, abort=False, debug=None, threshold=None, diff_template=''):
    """Drive the subtractor.
    This function acts as the command line interface backend.
    There is some duplication to support testability.
    """
    init_logger(level=logging.DEBUG if debug else None)
    forest = argv if argv else sys.argv[1:]
    if not forest or len(forest) < 2 or len(forest) > 3:
        print("Usage: subtractor past future [present]")
        return 0, "USAGE"

    executor = {}
    if diff_template:
        LOG.info("Requested external diff tool per template(%s)", diff_template)
        executor = parse_template(diff_template)

    LOG.debug("Guarded dispatch forest=%s", forest)
    past, present, future = causal_triplet(forest)

    if not present:
        print("ERROR: Either all args are dirs or files, but no mix")
        return 2, "USAGE"

    present_is_dir = present.is_dir()
    LOG.debug("Timeline past=%s, present=%s, and future=%s", past, present, future)

    mode_display = "folder" if present_is_dir else "file"

    LOG.info("Starting comparisons visiting past=%s and future=%s in %s mode", past, future, mode_display)
    threshold_fraction = 0.00
    if threshold:
        threshold_fraction = threshold
    pixel.OPTIONS["threshold"] = threshold_fraction
    LOG.info("  Threshold for pixel mismatch is %d%s",
             int(100 * threshold_fraction), " %" if threshold_fraction > 0 else "")
    good, bad = 0, 0

    if not present_is_dir:
        good, bad = process_pair(executor, good, bad, future, present, past)
    else:
        for ref_path, obs_path in matching_zipper(past, future, Splicer(), names_of, VISIT_OPTIONS):
            good, bad = process_pair(executor, good, bad, obs_path, present, ref_path)
            if abort and bad:
                LOG.error("Requested abort and encountered a bad pair")
                break

    LOG.info("Finished comparisons finding good=%d and bad=%d in %s mode", good, bad, mode_display)

    print(f"{'OK' if not bad else 'FAIL'}")

    return 0, ""
