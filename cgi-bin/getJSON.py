#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
import subprocess

cgitb.enable()
print('Content-Type: text/html')
print()
cmd = "sudo python3 ~/Desktop/mini-hoen/service_request.py request -j"
proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

print(proc.stdout)