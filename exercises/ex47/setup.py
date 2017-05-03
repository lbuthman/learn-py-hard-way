try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Exercise for writing python test cases",
    "author": "Luke Buthman",
    "url": "url to get it at",
    "download_url": "where to download it",
    "author_email": "lbuthman@gmail.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["ex47"],
    "scripts": [],
    "name": "ex47"
}

setup(**config)
