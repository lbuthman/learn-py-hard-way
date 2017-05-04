try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Exercise 48 solution",
    "author": "Luke Buthman",
    "url": "url to get it at",
    "download_url": "where to download it",
    "author_email": "lbuthman@gmail.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["ex48"],
    "scripts": [],
    "name": "ex48"
}

setup(**config)
