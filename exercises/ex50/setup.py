try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "My First Python Website",
    "author": "Luke Buthman",
    "url": "localhost",
    "download_url": "where to download it",
    "author_email": "lbuthman@gmail.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["ex50"],
    "scripts": [],
    "name": "ex50"
}

setup(**config)
