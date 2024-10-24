from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

VERSION = '0.3.1'
DESCRIPTION = 'Create a gradient frame for customtkinter.'

setup(
    name = "CTkGradient",
    version = VERSION,
    author = "TrollSkull",
    url = "https://github.com/TrollSkull/CTkGradient",
    author_email = "<trollskull.contact@gmail.com>",
    license = "MIT",
    description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    long_description = LONG_DESCRIPTION,
    packages = find_packages(),
    install_requires = ['customtkinter'],
    keywords = ['python', 'tkinter', 'customtkinter', 'gradient'],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
