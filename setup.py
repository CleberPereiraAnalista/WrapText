from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name = "wraptext",
    version = "1.0.0",
    description = "Um simples quebrador de texto para qualquer ocasião escrito em Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CleberPereiraAnalista/WrapText.git",
    author = "Cleber Almeida Pereira",
    author_email = "cleber.ap.ads@gmail.com",
    packages = ["wraptext"],
    classifiers = [  
    "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Portuguese (Brazilian)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords = ["wrap", "quebra-de-linha", "quebra"],
    python_requires=">=3.7, <4",
)
