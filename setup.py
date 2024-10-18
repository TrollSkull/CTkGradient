from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Create a gradient frame for customtkinter .'
LONG_DESCRIPTION = 'Create a gradient frame for your customtkinter applications.'

setup(
    name = "CTkGradient",
    version = VERSION,
    author = "TrollSkull",
    author_email = "<trollskull.contact@gmail.com>",
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
