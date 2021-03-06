#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "scorched"

def setup():
    autotools.aclocal()
    autotools.automake("--foreign")
    autotools.autoconf()

    autotools.configure("--disable-dependency-tracking \
                         --datadir=/usr/share/scorched3d \
                         --with-docdir=/%s/%s \
                         --without-wx-static \
                         --without-pgsql \
                         --without-mysql \
                         --with-wx-config=/usr/bin/wx-config \
                         --with-ogg \
                         --with-vorbis \
                         --with-ft \
                         --with-fftw \
                         --without-sdl-static"
                         % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG", "README")
