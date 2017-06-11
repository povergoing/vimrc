#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

BUNDLE_DIR = os.path.expanduser('~/.vim/bundle/')
BACKUP_DIR = raw_input("Archive to:")
ORIGINAL_DIR = os.getcwd()

for i in os.listdir(BUNDLE_DIR) :
    os.chdir(os.path.join(BUNDLE_DIR, i))
    archive_name = i + ".zip"
    archive_name = os.path.join(BACKUP_DIR, archive_name)
    if os.path.exists(archive_name):
        os.remove(archive_name)
    os.system("git archive -o '%s' HEAD" % (archive_name))

os.chdir(ORIGINAL_DIR)
print "finished"
