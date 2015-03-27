#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
build_exe_options = {"packages": ['os', 'sys', 'PIL','PyPDF2', 'mylib', 'configparser', 'mywrapperpdflib'], 'include_msvcr' : True}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Fastscan",
        version = "0.0.1",
        description = "Программа для расщепления PDF файлов",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.pyw", base=base)])