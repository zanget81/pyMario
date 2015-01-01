
__author__ = 'Angel'

from distutils.core import setup
from setuptools import find_packages
import py2exe
import pygame

__name__ = 'pyMario'
__version__ ='0.0.1'

setup(
    name = __name__,
    version = __version__,
    description='An amateur port of the Super Mario Bros game for NES to PC',
    author='Angel Campo',
    author_email='nagel81@gmail.com',
    packages=find_packages(),
    options = {'py2exe': {
        "packages" : ["src"],
        "bundle_files" :  "1",
        "optimize" : "1",
        "excludes": ["test"],
        "dll_excludes" :"w9xpopen.exe"
    }},

    # targets to build
    console = [{
                   'script': "./src/main.py",
                   "dest_base" : __name__,
                   'icon_resources':[(1, 'resources/img/mario.ico')]
               }],
    zipfile = None
)