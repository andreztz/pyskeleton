from setuptools import setup
from setuptools import find_packages

NAME = ""
VERSION = ""
DESCRIPTION = ""
KEYWORDS = ""
AUTHOR = ""
AUTHOR_EMAIL = ""
URL = ""
LICENSE = ""
CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Programming Language :: Python :: 3",
]
COMMAND = "command"


def readme():
    with open("README.md") as f:
        return f.read()


def required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


config = {
    "name": NAME,
    "version": VERSION,
    "description": DESCRIPTION,
    "long_description": readme(),
    "long_description_content_type": "text/markdown",
    "keywords": KEYWORDS,
    "author": AUTHOR,
    "author_email": AUTHOR_EMAIL,
    "url": URL,
    "license": LICENSE,
    "packages": find_packages(),
    "install_requires": required(),
    "entry_points": {"console_scripts": [f"{COMMAND}=src.__main__:main"]},
    "classifiers": CLASSIFIERS,
}

setup(**config)

# setup(
#     name=NAME,
#     version=VERSION,
#     description=DESCRIPTION,
#     long_description=readme(),
#     long_description_content_type="text/markdown",
#     keywords=KEYWORDS,
#     author=AUTHOR,
#     author_email=AUTHOR_EMAIL,
#     url=URL,
#     license=LICENSE,
#     packages=find_packages(),
#     install_requires=required(),
#     entry_points={"console_scripts": [f"{COMMAND}=src.__main__:main"]},
#     classifiers=CLASSIFIERS,
# )

