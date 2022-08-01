# Usage

## Examples

You can add four environment variables (and mix them independently) per `-e VAR_NAME=value` to modify the behavior of the subtractor:

* `-e SUBTRACTOR_ABORT=1` (1 or any other truth value) will abort processing on first file not found in both folders or mismatch of same name files
* `-e SUBTRACTOR_DEBUG=1` (1 or any other truth value) lowers the log level to debug
* `-e SUBTRACTOR_DIFF_TEMPLATE='tool --options xyz $ref $obs'` to execute that `tool` with options `xyz`; `$ref` and `$obs` are mandatory and will receive the respective paths.
* `-e SUBTRACTOR_THRESHOLD=0.05` (0.05 or any other float value in [0, 1])  sets the mismatch pixel ratio threshold before a difference is considered a failure

There is some temporary magic implemented as template DSL to enable external tool use that requires a parameter file. 
The tokens `:$file:`and `:$name:` (none or both must be present to succeed) will result in translating 
`'what ever @foo.txt:$file:CONTENT:$name:foo.txt'`into an executing vector of `["what", "ever", "@foo.txt"]` for the subprocess and 
the creation of a file `foo.txt` (because of the trailing part after the `:$name:`token) where 
for every invocation the usual `$ref` and `$obs`are also performed on the `CONTENT`(the text between the `:$file:`and `:$name:` tokens.

Folders with even different files (not present in the other folder):
```
$ python -m subtractor tests/fixtures/different/{ref,obs}
2021-05-09T22:36:45.960 INFO [subtractor]: Starting comparisons visiting past=tests/fixtures/different/ref and future=tests/fixtures/different/obs in folder mode
2021-05-09T22:36:45.960 INFO [subtractor]:   Threshold for pixel mismatch is 1 %
2021-05-09T22:36:45.961 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/_a.png, obs=None
2021-05-09T22:36:45.961 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/bright_red_green_and_blue.png, obs=None
2021-05-09T22:36:45.961 INFO [subtractor]: Pair ref=None, obs=tests/fixtures/different/obs/bright_red_green_or_blue_dunno.png
2021-05-09T22:36:45.961 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/bright_red_half_transparent.png, obs=tests/fixtures/different/obs/bright_red_half_transparent.png
2021-05-09T22:36:45.961 INFO [subtractor]:   Found ref=tests/fixtures/different/ref/bright_red_half_transparent.png to be OK with size 290 bytes
2021-05-09T22:36:45.962 INFO [subtractor]:     Analyzed ref=tests/fixtures/different/ref/bright_red_half_transparent.png as PNG to be OK with shape 2x2
2021-05-09T22:36:45.962 INFO [subtractor]:   Found obs=tests/fixtures/different/obs/bright_red_half_transparent.png to be OK with size 290 bytes
2021-05-09T22:36:45.964 INFO [subtractor]:     Analyzed obs=tests/fixtures/different/obs/bright_red_half_transparent.png as PNG to be OK with shape 2x2
2021-05-09T22:36:45.991 INFO [subtractor]:   Match of obs=tests/fixtures/different/obs/bright_red_half_transparent.png
2021-05-09T22:36:45.992 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/bright_red_or_blue.png, obs=tests/fixtures/different/obs/bright_red_or_blue.png
2021-05-09T22:36:45.992 INFO [subtractor]:   Found ref=tests/fixtures/different/ref/bright_red_or_blue.png to be OK with size 276 bytes
2021-05-09T22:36:45.992 INFO [subtractor]:     Analyzed ref=tests/fixtures/different/ref/bright_red_or_blue.png as PNG to be OK with shape 10x10
2021-05-09T22:36:45.992 INFO [subtractor]:   Found obs=tests/fixtures/different/obs/bright_red_or_blue.png to be OK with size 276 bytes
2021-05-09T22:36:45.993 INFO [subtractor]:     Analyzed obs=tests/fixtures/different/obs/bright_red_or_blue.png as PNG to be OK with shape 10x10
2021-05-09T22:36:45.995 INFO [subtractor]:   Mismatch of obs=tests/fixtures/different/obs/bright_red_or_blue.png is 100 of 100 pixels or 100.0 %
2021-05-09T22:36:45.995 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/bright_red_or_green_dunno.png, obs=tests/fixtures/different/obs/bright_red_or_green_dunno.png
2021-05-09T22:36:45.995 INFO [subtractor]:   Found ref=tests/fixtures/different/ref/bright_red_or_green_dunno.png to be OK with size 276 bytes
2021-05-09T22:36:45.996 INFO [subtractor]:     Analyzed ref=tests/fixtures/different/ref/bright_red_or_green_dunno.png as PNG to be OK with shape 10x10
2021-05-09T22:36:45.996 INFO [subtractor]:   Found obs=tests/fixtures/different/obs/bright_red_or_green_dunno.png to be OK with size 6245 bytes
2021-05-09T22:36:45.997 INFO [subtractor]:     Analyzed obs=tests/fixtures/different/obs/bright_red_or_green_dunno.png as PNG to be OK with shape 10x10
2021-05-09T22:36:45.998 INFO [subtractor]:   Mismatch of obs=tests/fixtures/different/obs/bright_red_or_green_dunno.png is 20 of 100 pixels or 20.0 %
2021-05-09T22:36:45.998 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/negative_strip.png, obs=tests/fixtures/different/obs/negative_strip.png
2021-05-09T22:36:45.998 INFO [subtractor]:   Found ref=tests/fixtures/different/ref/negative_strip.png to be OK with size 38574 bytes
2021-05-09T22:36:45.999 INFO [subtractor]:     Analyzed ref=tests/fixtures/different/ref/negative_strip.png as PNG to be OK with shape 1920x1080
2021-05-09T22:36:45.999 INFO [subtractor]:   Found obs=tests/fixtures/different/obs/negative_strip.png to be OK with size 38574 bytes
2021-05-09T22:36:46.000 INFO [subtractor]:     Analyzed obs=tests/fixtures/different/obs/negative_strip.png as PNG to be OK with shape 1920x1080
2021-05-09T22:36:49.076 INFO [subtractor]:   Match of obs=tests/fixtures/different/obs/negative_strip.png
2021-05-09T22:36:49.076 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/something_else.png, obs=tests/fixtures/different/obs/something_else.png
2021-05-09T22:36:49.076 INFO [subtractor]:   Found ref=tests/fixtures/different/ref/something_else.png to be OK with size 540 bytes
2021-05-09T22:36:49.078 INFO [subtractor]:     Analyzed ref=tests/fixtures/different/ref/something_else.png as PNG to be OK with shape 1920x1080
2021-05-09T22:36:49.078 INFO [subtractor]:   Found obs=tests/fixtures/different/obs/something_else.png to be OK with size 38574 bytes
2021-05-09T22:36:49.079 INFO [subtractor]:     Analyzed obs=tests/fixtures/different/obs/something_else.png as PNG to be OK with shape 1920x1080
2021-05-09T22:37:07.103 INFO [subtractor]:   Mismatch of obs=tests/fixtures/different/obs/something_else.png is 1369324 of 2073600 pixels or 66.0 %
2021-05-09T22:37:07.103 INFO [subtractor]: Pair ref=None, obs=tests/fixtures/different/obs/z.png
2021-05-09T22:37:07.103 INFO [subtractor]: Pair ref=None, obs=tests/fixtures/different/obs/zz.png
2021-05-09T22:37:07.103 INFO [subtractor]: Finished comparisons finding good=2 and bad=8 in folder mode
FAIL
```

Folders with deviating files (same number of files with matching names):
```
$ python -m subtractor tests/fixtures/deviating/{ref,obs}
2021-05-09T22:38:14.227 INFO [subtractor]: Starting comparisons visiting past=tests/fixtures/deviating/ref and future=tests/fixtures/deviating/obs in folder mode
2021-05-09T22:38:14.228 INFO [subtractor]:   Threshold for pixel mismatch is 1 %
2021-05-09T22:38:14.228 INFO [subtractor]: Pair ref=tests/fixtures/deviating/ref/bright_red_half_transparent.png, obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png
2021-05-09T22:38:14.228 INFO [subtractor]:   Found ref=tests/fixtures/deviating/ref/bright_red_half_transparent.png to be OK with size 290 bytes
2021-05-09T22:38:14.229 INFO [subtractor]:     Analyzed ref=tests/fixtures/deviating/ref/bright_red_half_transparent.png as PNG to be OK with shape 2x2
2021-05-09T22:38:14.229 INFO [subtractor]:   Found obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png to be OK with size 290 bytes
2021-05-09T22:38:14.231 INFO [subtractor]:     Analyzed obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png as PNG to be OK with shape 2x2
2021-05-09T22:38:14.266 INFO [subtractor]:   Match of obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png
2021-05-09T22:38:14.266 INFO [subtractor]: Pair ref=tests/fixtures/deviating/ref/bright_red_or_blue.png, obs=tests/fixtures/deviating/obs/bright_red_or_blue.png
2021-05-09T22:38:14.266 INFO [subtractor]:   Found ref=tests/fixtures/deviating/ref/bright_red_or_blue.png to be OK with size 276 bytes
2021-05-09T22:38:14.268 INFO [subtractor]:     Analyzed ref=tests/fixtures/deviating/ref/bright_red_or_blue.png as PNG to be OK with shape 10x10
2021-05-09T22:38:14.268 INFO [subtractor]:   Found obs=tests/fixtures/deviating/obs/bright_red_or_blue.png to be OK with size 276 bytes
2021-05-09T22:38:14.269 INFO [subtractor]:     Analyzed obs=tests/fixtures/deviating/obs/bright_red_or_blue.png as PNG to be OK with shape 10x10
2021-05-09T22:38:14.272 INFO [subtractor]:   Mismatch of obs=tests/fixtures/deviating/obs/bright_red_or_blue.png is 100 of 100 pixels or 100.0 %
2021-05-09T22:38:14.272 INFO [subtractor]: Pair ref=tests/fixtures/deviating/ref/bright_red_or_green_dunno.png, obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png
2021-05-09T22:38:14.272 INFO [subtractor]:   Found ref=tests/fixtures/deviating/ref/bright_red_or_green_dunno.png to be OK with size 276 bytes
2021-05-09T22:38:14.273 INFO [subtractor]:     Analyzed ref=tests/fixtures/deviating/ref/bright_red_or_green_dunno.png as PNG to be OK with shape 10x10
2021-05-09T22:38:14.273 INFO [subtractor]:   Found obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png to be OK with size 6245 bytes
2021-05-09T22:38:14.275 INFO [subtractor]:     Analyzed obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png as PNG to be OK with shape 10x10
2021-05-09T22:38:14.277 INFO [subtractor]:   Mismatch of obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png is 20 of 100 pixels or 20.0 %
2021-05-09T22:38:14.277 INFO [subtractor]: Finished comparisons finding good=1 and bad=2 in folder mode
FAIL
```

Folders with identical files:
```
$ python -m subtractor tests/fixtures/ref_obs/{ref,obs}
2021-05-09T22:39:05.954 INFO [subtractor]: Starting comparisons visiting past=tests/fixtures/ref_obs/ref and future=tests/fixtures/ref_obs/obs in folder mode
2021-05-09T22:39:05.954 INFO [subtractor]:   Threshold for pixel mismatch is 1 %
2021-05-09T22:39:05.955 INFO [subtractor]: Pair ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png, obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png
2021-05-09T22:39:05.955 INFO [subtractor]:   Found ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png to be OK with size 277 bytes
2021-05-09T22:39:05.957 INFO [subtractor]:     Analyzed ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:05.957 INFO [subtractor]:   Found obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png to be OK with size 277 bytes
2021-05-09T22:39:05.958 INFO [subtractor]:     Analyzed obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:05.993 INFO [subtractor]:   Match of obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png
2021-05-09T22:39:05.994 INFO [subtractor]: Pair ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png, obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png
2021-05-09T22:39:05.994 INFO [subtractor]:   Found ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png to be OK with size 290 bytes
2021-05-09T22:39:05.996 INFO [subtractor]:     Analyzed ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:05.996 INFO [subtractor]:   Found obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png to be OK with size 290 bytes
2021-05-09T22:39:06.006 INFO [subtractor]:     Analyzed obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:06.007 INFO [subtractor]:   Match of obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png
2021-05-09T22:39:06.008 INFO [subtractor]: Finished comparisons finding good=2 and bad=0 in folder mode
OK
```

Same with debug mode:
```
$ SUBTRACTOR_DEBUG=1 python -m subtractor tests/fixtures/ref_obs/{ref,obs}
2021-05-09T22:39:51.410 DEBUG [subtractor]: Guarded dispatch forest=['tests/fixtures/ref_obs/ref', 'tests/fixtures/ref_obs/obs']
2021-05-09T22:39:51.410 DEBUG [subtractor]: Timeline past=tests/fixtures/ref_obs/ref, present=tests/fixtures/ref_obs/diff-of-ref_obs, and future=tests/fixtures/ref_obs/obs
2021-05-09T22:39:51.410 INFO [subtractor]: Starting comparisons visiting past=tests/fixtures/ref_obs/ref and future=tests/fixtures/ref_obs/obs in folder mode
2021-05-09T22:39:51.410 INFO [subtractor]:   Threshold for pixel mismatch is 1 %
2021-05-09T22:39:51.411 INFO [subtractor]: Pair ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png, obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png
2021-05-09T22:39:51.411 INFO [subtractor]:   Found ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png to be OK with size 277 bytes
2021-05-09T22:39:51.413 INFO [subtractor]:     Analyzed ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:51.413 INFO [subtractor]:   Found obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png to be OK with size 277 bytes
2021-05-09T22:39:51.415 INFO [subtractor]:     Analyzed obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:51.462 DEBUG [PIL.PngImagePlugin]: STREAM b'IHDR' 16 13
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'gAMA' 41 4
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'cHRM' 57 32
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'PLTE' 101 6
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'bKGD' 119 1
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: b'bKGD' 119 1 (unknown)
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'tIME' 132 7
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: b'tIME' 132 7 (unknown)
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'IDAT' 151 12
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'IHDR' 16 13
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'gAMA' 41 4
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'cHRM' 57 32
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'PLTE' 101 6
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'bKGD' 119 1
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: b'bKGD' 119 1 (unknown)
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'tIME' 132 7
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: b'tIME' 132 7 (unknown)
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'IDAT' 151 12
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 175 37
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 224 37
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 175 37
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 224 37
2021-05-09T22:39:51.467 INFO [subtractor]:   Match of obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png
2021-05-09T22:39:51.467 INFO [subtractor]: Pair ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png, obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png
2021-05-09T22:39:51.467 INFO [subtractor]:   Found ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png to be OK with size 290 bytes
2021-05-09T22:39:51.468 INFO [subtractor]:     Analyzed ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:51.468 INFO [subtractor]:   Found obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png to be OK with size 290 bytes
2021-05-09T22:39:51.470 INFO [subtractor]:     Analyzed obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'IHDR' 16 13
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'gAMA' 41 4
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'cHRM' 57 32
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'PLTE' 101 6
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'tRNS' 119 1
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'bKGD' 132 1
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: b'bKGD' 132 1 (unknown)
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'tIME' 145 7
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: b'tIME' 145 7 (unknown)
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'IDAT' 164 12
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'IHDR' 16 13
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'gAMA' 41 4
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'cHRM' 57 32
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'PLTE' 101 6
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tRNS' 119 1
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'bKGD' 132 1
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: b'bKGD' 132 1 (unknown)
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tIME' 145 7
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: b'tIME' 145 7 (unknown)
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'IDAT' 164 12
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 188 37
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 237 37
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 188 37
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 237 37
2021-05-09T22:39:51.473 INFO [subtractor]:   Match of obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png
2021-05-09T22:39:51.473 INFO [subtractor]: Finished comparisons finding good=2 and bad=0 in folder mode
OK
```

Use external diff tool:
```bash
$ SUBTRACTOR_DIFF_TEMPLATE='diff --text $ref $obs' python -m subtractor tests/fixtures/deviating/{ref,obs}
2021-05-10T22:08:05.355 INFO [subtractor]: Requested external diff tool per template(diff --text $ref $obs)
2021-05-10T22:08:05.356 INFO [subtractor]: Starting comparisons visiting past=tests/fixtures/deviating/ref and future=tests/fixtures/deviating/obs in folder mode
2021-05-10T22:08:05.356 INFO [subtractor]:   Threshold for pixel mismatch is 1 %
2021-05-10T22:08:05.357 INFO [subtractor]: Pair ref=tests/fixtures/deviating/ref/bright_red_half_transparent.png, obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png
2021-05-10T22:08:05.357 INFO [subtractor]:   Found ref=tests/fixtures/deviating/ref/bright_red_half_transparent.png to be OK with size 290 bytes
2021-05-10T22:08:05.360 INFO [subtractor]:     Analyzed ref=tests/fixtures/deviating/ref/bright_red_half_transparent.png as PNG to be OK with shape 2x2
2021-05-10T22:08:05.360 INFO [subtractor]:   Found obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png to be OK with size 290 bytes
2021-05-10T22:08:05.361 INFO [subtractor]:     Analyzed obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png as PNG to be OK with shape 2x2
2021-05-10T22:08:05.370 INFO [subtractor]: b'3,4c3,4\n< \x00\x00\x00\rIHDR\x00\x00\x00\x02\x00\x00\x00\x02\x01\x03\x00\x00\x00Hx\x9fg\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00 cHRM\x00\x00 ...
2021-05-10T22:08:05.371 INFO [subtractor]: Pair ref=tests/fixtures/deviating/ref/bright_red_or_blue.png, obs=tests/fixtures/deviating/obs/bright_red_or_blue.png
2021-05-10T22:08:05.371 INFO [subtractor]:   Found ref=tests/fixtures/deviating/ref/bright_red_or_blue.png to be OK with size 276 bytes
2021-05-10T22:08:05.373 INFO [subtractor]:     Analyzed ref=tests/fixtures/deviating/ref/bright_red_or_blue.png as PNG to be OK with shape 10x10
2021-05-10T22:08:05.373 INFO [subtractor]:   Found obs=tests/fixtures/deviating/obs/bright_red_or_blue.png to be OK with size 276 bytes
2021-05-10T22:08:05.374 INFO [subtractor]:     Analyzed obs=tests/fixtures/deviating/obs/bright_red_or_blue.png as PNG to be OK with shape 10x10
2021-05-10T22:08:05.383 INFO [subtractor]: b'5c5\n< \x01\x03\x00\x00\x00\xb7\xfc]\xfe\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00 cHRM\x00\x00z&\x00\x00\x80\x84\x00\x00\xfa\x00\x00\x00\x80\x ...
2021-05-10T22:08:05.383 INFO [subtractor]: Pair ref=tests/fixtures/deviating/ref/bright_red_or_green_dunno.png, obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png
2021-05-10T22:08:05.383 INFO [subtractor]:   Found ref=tests/fixtures/deviating/ref/bright_red_or_green_dunno.png to be OK with size 276 bytes
2021-05-10T22:08:05.385 INFO [subtractor]:     Analyzed ref=tests/fixtures/deviating/ref/bright_red_or_green_dunno.png as PNG to be OK with shape 10x10
2021-05-10T22:08:05.385 INFO [subtractor]:   Found obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png to be OK with size 6245 bytes
2021-05-10T22:08:05.387 INFO [subtractor]:     Analyzed obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png as PNG to be OK with shape 10x10
2021-05-10T22:08:05.395 INFO [subtractor]: b'5c5,91\n< \x01\x03\x00\x00\x00\xb7\xfc]\xfe\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00 cHRM\x00\x00z&\x00\x00\x80\x84\x00\x00\xfa\x00\x00\x00\x8 ...
2021-05-10T22:08:05.395 INFO [subtractor]: Finished comparisons finding good=0 and bad=3 in folder mode
FAIL
```

Contrived and made up use case with diff template and param file magic:
```bash
$ SUBTRACTOR_DIFF_TEMPLATE='echo $ref $obs @foo:$file:asd=42 $ref $obs:$name:foo' python -m subtractor tests/fixtures/ref_obs/{ref,obs}/ff0000_2x2.png
2021-05-11T23:33:03.183 INFO [subtractor]: Requested external diff tool per template(echo $ref $obs @foo:$file:asd=42 $ref $obs:$name:foo)
2021-05-11T23:33:03.183 INFO [subtractor]: Detected magic (:$file:) in template
2021-05-11T23:33:03.183 INFO [subtractor]: Parsed diff template (echo $ref $obs @foo:$file:asd=42 $ref $obs:$name:foo) into executor ...
2021-05-11T23:33:03.183 INFO [subtractor]:  ...   into executor ({'executor': 'echo $ref $obs @foo', 'param_file_content': 'asd=42 $ref $obs', 'param_file_name': 'foo'})
2021-05-11T23:33:03.183 INFO [subtractor]: Starting comparisons visiting past=tests/fixtures/ref_obs/ref/ff0000_2x2.png and future=tests/fixtures/ref_obs/obs/ff0000_2x2.png in file mode
2021-05-11T23:33:03.183 INFO [subtractor]:   Threshold for pixel mismatch is 1 %
2021-05-11T23:33:03.183 INFO [subtractor]: Pair ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png, obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png
2021-05-11T23:33:03.183 INFO [subtractor]:   Found ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png to be OK with size 277 bytes
2021-05-11T23:33:03.185 INFO [subtractor]:     Analyzed ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png as PNG to be OK with shape 2x2
2021-05-11T23:33:03.185 INFO [subtractor]:   Found obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png to be OK with size 277 bytes
2021-05-11T23:33:03.186 INFO [subtractor]:     Analyzed obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png as PNG to be OK with shape 2x2
2021-05-11T23:33:03.190 INFO [subtractor]: b'tests/fixtures/ref_obs/ref/ff0000_2x2.png tests/fixtures/ref_obs/obs/ff0000_2x2.png @foo\n'
2021-05-11T23:33:03.190 INFO [subtractor]: Finished comparisons finding good=1 and bad=0 in file mode
OK
$ cat foo
asd=42 tests/fixtures/ref_obs/ref/ff0000_2x2.png tests/fixtures/ref_obs/obs/ff0000_2x2.png%
```
