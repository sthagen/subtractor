# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/subtractor/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([b0cbcbc7 ...](https://git.sr.ht/~sthagen/subtractor/blob/default/etc/sbom/cdx.json.sha256 "sha256:b0cbcbc75efec5bdeeec77d83680cf76c724f07b3186d76c37a0716dc0621e6a")).
<!--[[[end]]] (checksum: c2470aa47d3dc0c5f705a3aaccf825fa)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                  | Version                                                      | License                                            | Author                                        | Description (from packaging data)                                  |
|:------------------------------------------------------|:-------------------------------------------------------------|:---------------------------------------------------|:----------------------------------------------|:-------------------------------------------------------------------|
| [pillow](https://python-pillow.org)                   | [10.2.0](https://pypi.org/project/pillow/10.2.0/)            | Historical Permission Notice and Disclaimer (HPND) | "Jeffrey A. Clark (Alex)" <aclark@aclark.net> | Python Imaging Library (Fork)                                      |
| [pixelmatch](https://github.com/whtsky/pixelmatch-py) | [0.3.0](https://pypi.org/project/pixelmatch/0.3.0/)          | ISC                                                | Wu Haotian                                    | A pixel-level image comparison library.                            |
| [pypng](https://gitlab.com/drj11/pypng)               | [0.20220715.0](https://pypi.org/project/pypng/0.20220715.0/) | MIT License                                        | David Jones                                   | Pure Python library for saving and loading PNG images              |
| [typer](https://github.com/tiangolo/typer)            | [0.9.0](https://pypi.org/project/typer/0.9.0/)               | MIT License                                        | Sebastián Ramírez                             | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: c29e4056977372e9da34658aec30d1d2)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                             | Version                                                    | License                            | Author                                                                                | Description (from packaging data)                      |
|:-----------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                    | [8.1.6](https://pypi.org/project/click/8.1.6/)             | BSD License                        | Pallets <contact@palletsprojects.com>                                                 | Composable command line interface toolkit              |
| [typing_extensions](https://github.com/python/typing_extensions) | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+ |
<!--[[[end]]] (checksum: c620e5e6d9d46e4e35ff7b749d5230d8)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
pillow==10.2.0
pixelmatch==0.3.0
pypng==0.20220715.0
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 5bfcaef984196caec09eb2f79bea2eda)-->
