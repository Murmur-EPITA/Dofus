#!/usr/bin/env python
from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = cythonize([
    Extension("tkinter_frames.position", ["tkinter_frames/position.py"]),

    Extension("utils.ClickMouse", ["utils/ClickMouse.py"]),
    Extension("utils.CONSTANTS", ["utils/CONSTANTS.py"]),
    Extension("utils.DIRECTION", ["utils/DIRECTION.py"]),
    Extension("utils.other", ["utils/other.py"]),
    Extension("utils.Player", ["utils/Player.py"]),
    Extension("utils.WindowManagement", ["utils/WindowManagement.py"]),
    Extension("utils.write_resources", ["utils/write_resources.py"]),

    Extension("main", ["main.py"]),
])

for module in ext_modules:
    module.cython_c_in_temp = True

setup(
    ext_modules=ext_modules
)