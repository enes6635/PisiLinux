#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "pycairo-%s" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pythonmodules.fixCompiledPy()
