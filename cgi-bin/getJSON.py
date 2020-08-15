#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
import subprocess
cmd = "python3 /home/mario/Desktop/mini-hoen/service_request.py request -j"
proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
cgitb.enable()
print('Content-Type: text/html')
print()

print(proc.stdout.decode('utf-8'))
# print(proc.stderr)