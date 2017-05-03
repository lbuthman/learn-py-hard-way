try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Quiz for ch. 46",
    "author": "Luke Buthman",
    "url": "url to get it at",
    "download_url": "where to download it",
    "author_email": "lbuthman@gmail.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["quiz"],
    "scripts": ["./bin/hello_world.py"],
    "name": "quiz"
}

setup(**config)
