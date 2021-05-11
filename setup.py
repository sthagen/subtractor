import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
README += "\n"
README += (HERE / "docs" / "index.md").read_text()
README += "\n"
README += (HERE / "docs" / "install.md").read_text()
README += "\n"
README += (HERE / "docs" / "use.md").read_text()
README += "\n"
README += (HERE / "docs" / "changes.md").read_text()

# This call to setup() does all the work
setup(
    name="subtractor",
    version="0.0.5",
    description="Pixels, pixels, pixels.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sthagen/jubilant-invention",
    author="Stefan Hagen",
    author_email="stefan@hagen.link",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="csv development diff ini json compare",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "Pillow",
        "pixelmatch",
        "pypng",
    ],
    entry_points={
        "console_scripts": [
            "subtractor = subtractor.cli:main",
        ]
    },
)
