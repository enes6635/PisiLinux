#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # do not install examples
    pisitools.dosed("Makefile.am", "^(install:\s.*?)install-examples", r"\1")
    autotools.autoreconf("-vif")

    autotools.configure("--enable-cxx \
                         --enable-fortran \
                         --enable-production \
                         --enable-linux-lfs \
                         --disable-static \
                         --disable-parallel \
                         --disable-sharedlib-rpath \
                         --disable-dependency-tracking \
                         --with-pthread \
                         --with-pic")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ACKNOWLEDGMENTS", "COPYING", "README*", "release_docs/HISTORY-*", "release_docs/RELEASE.txt")
