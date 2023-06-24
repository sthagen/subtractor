# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/subtractor/blob/default/sbom/cdx.json) with SHA256 checksum ([ff2b9adc ...](https://git.sr.ht/~sthagen/subtractor/blob/default/sbom/cdx.json.sha256 "sha256:ff2b9adc42203dd5e212dd7043ad98abbfd461e87ee16877e5c3b7f4a1fbf334")).
<!--[[[end]]] (checksum: 3f94514b2a74769ace3270189bede3d0)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                  | Version                                                      | License                                            | Author                  | Description (from packaging data)                                  |
|:------------------------------------------------------|:-------------------------------------------------------------|:---------------------------------------------------|:------------------------|:-------------------------------------------------------------------|
| [Pillow](https://python-pillow.org)                   | [9.5.0](https://pypi.org/project/Pillow/9.5.0/)              | Historical Permission Notice and Disclaimer (HPND) | Jeffrey A. Clark (Alex) | Python Imaging Library (Fork)                                      |
| [pixelmatch](https://github.com/whtsky/pixelmatch-py) | [0.3.0](https://pypi.org/project/pixelmatch/0.3.0/)          | ISC                                                | Wu Haotian              | A pixel-level image comparison library.                            |
| [pypng](https://gitlab.com/drj11/pypng)               | [0.20220715.0](https://pypi.org/project/pypng/0.20220715.0/) | MIT License                                        | David Jones             | Pure Python library for saving and loading PNG images              |
| [typer](https://github.com/tiangolo/typer)            | [0.7.0](https://pypi.org/project/typer/0.7.0/)               | MIT License                                        | Sebastián Ramírez       | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 1ed8a9e86abb6893fb60d58283b597f9)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Pillow==9.5.0
pixelmatch==0.3.0
pypng==0.20220715.0
typer==0.7.0
└── click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 4f0e1e1d2bda1fc4713df89c5505116b)-->
