import setuptools

from pathlib import Path
from pkg_resources import parse_requirements

with open("README.md", "r") as fh:
    long_description = fh.read()

path = Path("requirements.txt")
install_requires = [str(ir) for ir in parse_requirements(path.open())]

setuptools.setup(
    name="python_advanced_search",
    version='0.0.1',
    author="Rémi Lopez",
    author_email="contact.remilopez@gmail.com",
    description="Python open-source package : advanced queries for search-engines (Google, Bing)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zepolimer/python-advanced-search",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=install_requires,
)
