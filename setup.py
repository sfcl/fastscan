#!/usr/bin/env python
# -*- coding:utf-8 -*-

from distutils.core import setup
import py2exe
 
setup(windows=[{ "script":'main.pyw', 'icon_resources': [(0, "myicon.ico")], }])

#setup(windows=['main.pyw'])
