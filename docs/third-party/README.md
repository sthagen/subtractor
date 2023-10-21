# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/subtractor/blob/default/sbom/cdx.json) with SHA256 checksum ([dc9294bc ...](https://git.sr.ht/~sthagen/subtractor/blob/default/sbom/cdx.json.sha256 "sha256:dc9294bc867c19bbcbc89aa3e3fe2e9651c9c3aa5479cc57756ce014203f3a06")).
<!--[[[end]]] (checksum: 90777205c8ee2daba908aab06083ca65)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                  | Version                                                      | License                                            | Author                  | Description (from packaging data)                                  |
|:------------------------------------------------------|:-------------------------------------------------------------|:---------------------------------------------------|:------------------------|:-------------------------------------------------------------------|
| [Pillow](https://python-pillow.org)                   | [10.1.0](https://pypi.org/project/Pillow/10.1.0/)            | Historical Permission Notice and Disclaimer (HPND) | Jeffrey A. Clark (Alex) | Python Imaging Library (Fork)                                      |
| [pixelmatch](https://github.com/whtsky/pixelmatch-py) | [0.3.0](https://pypi.org/project/pixelmatch/0.3.0/)          | ISC                                                | Wu Haotian              | A pixel-level image comparison library.                            |
| [pypng](https://gitlab.com/drj11/pypng)               | [0.20220715.0](https://pypi.org/project/pypng/0.20220715.0/) | MIT License                                        | David Jones             | Pure Python library for saving and loading PNG images              |
| [typer](https://github.com/tiangolo/typer)            | [0.9.0](https://pypi.org/project/typer/0.9.0/)               | MIT License                                        | Sebastián Ramírez       | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 5332284d9d44e34237ea36f156077923)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author                                | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:--------------------------------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.6](https://pypi.org/project/click/8.1.6/) | BSD License | Pallets <contact@palletsprojects.com> | Composable command line interface toolkit |
<!--[[[end]]] (checksum: 7b69d9be7fa227d2db394dcd865606d8)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Pillow==10.1.0
pixelmatch==0.3.0
pypng==0.20220715.0
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 74bf0a5e9bd2fb6d093b23489cb3ba9b)-->
