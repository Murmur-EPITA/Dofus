#!/usr/bin/env python
from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = cythonize([
    Extension("utils.ClickMouse", ["utils/ClickMouse.py"]),
    Extension("utils.CONSTANTS", ["utils/CONSTANTS.py"]),
    Extension("utils.DIRECTION", ["utils/DIRECTION.py"]),
    Extension("utils.Player", ["utils/Player.py"]),
    Extension("utils.tKinter", ["utils/tKinter.py"]),
    Extension("utils.WindowManagement", ["utils/WindowManagement.py"]),
    Extension("utils.write_resources", ["utils/write_resources.py"]),
])

setup(
    ext_modules=ext_modules
)