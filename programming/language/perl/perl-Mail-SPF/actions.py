#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-v%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()

# to protect conflict with perl-Mail-SPF-Query package
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/share/man/man1")
