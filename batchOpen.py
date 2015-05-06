#!/usr/bin/env python

import sys
import subprocess

fileList = sys.argv[1]
fileArr = open(fileList).read().split('\n')
fileString = ' '.join(fileArr)
subprocess.call('open -a "Sublime Text 2" ' + fileString, shell=True)