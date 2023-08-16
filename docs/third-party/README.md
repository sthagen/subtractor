# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/subtractor/blob/default/sbom/cdx.json) with SHA256 checksum ([ca56e018 ...](https://git.sr.ht/~sthagen/subtractor/blob/default/sbom/cdx.json.sha256 "sha256:ca56e01819d98b3b880a8fc9124432cfe8a854954efe9aa37c72afc037204900")).
<!--[[[end]]] (checksum: fee7a57fd21c5b3f0813912d8853a4cb)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                  | Version                                                      | License                                            | Author                  | Description (from packaging data)                                  |
|:------------------------------------------------------|:-------------------------------------------------------------|:---------------------------------------------------|:------------------------|:-------------------------------------------------------------------|
| [Pillow](https://python-pillow.org)                   | [10.0.0](https://pypi.org/project/Pillow/10.0.0/)            | Historical Permission Notice and Disclaimer (HPND) | Jeffrey A. Clark (Alex) | Python Imaging Library (Fork)                                      |
| [pixelmatch](https://github.com/whtsky/pixelmatch-py) | [0.3.0](https://pypi.org/project/pixelmatch/0.3.0/)          | ISC                                                | Wu Haotian              | A pixel-level image comparison library.                            |
| [pypng](https://gitlab.com/drj11/pypng)               | [0.20220715.0](https://pypi.org/project/pypng/0.20220715.0/) | MIT License                                        | David Jones             | Pure Python library for saving and loading PNG images              |
| [typer](https://github.com/tiangolo/typer)            | [0.9.0](https://pypi.org/project/typer/0.9.0/)               | MIT License                                        | Sebastián Ramírez       | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 17dc2dd7ce2a4e11a11f4b6dbf9f1464)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author  | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:--------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.6](https://pypi.org/project/click/8.1.6/) | BSD License | UNKNOWN | Composable command line interface toolkit |
<!--[[[end]]] (checksum: ec405dc73a3ccb02ae4ac4f6b5c7739e)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Pillow==10.0.0
pixelmatch==0.3.0
pypng==0.20220715.0
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 6146970e129daa194cefbfe319242b8a)-->
