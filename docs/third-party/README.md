# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/subtractor/blob/default/sbom.json) with SHA256 checksum ([029f8022 ...](https://git.sr.ht/~sthagen/subtractor/blob/default/sbom.json.sha256 "sha256:029f80220666d15601d514e21819df1ebcf367b67a44e1f345a586d8e271f29d")).
<!--[[[end]]] (checksum: c83b330db159a26484a6b245b044ad2d)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                  | Version                                                      | License                                            | Author                       | Description (from packaging data)                                  |
|:------------------------------------------------------|:-------------------------------------------------------------|:---------------------------------------------------|:-----------------------------|:-------------------------------------------------------------------|
| [Pillow](https://python-pillow.org)                   | [9.3.0](https://pypi.org/project/Pillow/9.3.0/)              | Historical Permission Notice and Disclaimer (HPND) | Alex Clark (PIL Fork Author) | Python Imaging Library (Fork)                                      |
| [pixelmatch](https://github.com/whtsky/pixelmatch-py) | [0.3.0](https://pypi.org/project/pixelmatch/0.3.0/)          | ISC                                                | Wu Haotian                   | A pixel-level image comparison library.                            |
| [pypng](https://gitlab.com/drj11/pypng)               | [0.20220715.0](https://pypi.org/project/pypng/0.20220715.0/) | MIT License                                        | David Jones                  | Pure Python library for saving and loading PNG images              |
| [typer](https://github.com/tiangolo/typer)            | [0.7.0](https://pypi.org/project/typer/0.7.0/)               | MIT License                                        | Sebastián Ramírez            | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 1dd88b903498fb81626fe7b574aca1b7)-->

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
Pillow==9.3.0
pixelmatch==0.3.0
pypng==0.20220715.0
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 337e8213f9c5fbc05f29ca02ddca0f66)-->
