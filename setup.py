import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Physica",
    version="0.0.5",
    author="Sean Richards",
    author_email="sric560@aucklanduni.ac.nz",
    description="A lightweight, flexible package to automate common tasks in Physics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krytic/physica",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)