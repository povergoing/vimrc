#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys


CURRENT_DIR = os.getcwd()
ZIP_FILES = [ i for i in os.listdir(CURRENT_DIR) if i.rfind(".zip") > -1 ]

if sys.argv[1] == "d":
    ZIP_FILES = [ i.replace(".zip", "") for i in ZIP_FILES]
    for i in ZIP_FILES :
        os.system("rm -rf %s" % i)
    print "All dirs has been removed"
    exit()

for i in ZIP_FILES:
    os.system("unzip -uq %s -d %s" % (i, i.replace(".zip", "")))

print "FINISHED"


