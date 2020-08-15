#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
import subprocess
import json
cmd = "python3 /home/mario/Desktop/mini-hoen/service_request.py request -j"
proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
cgitb.enable()
print('Content-Type: text/html')
print()
# a=json.dumps(proc.stdout.decode('utf-8'),indent=3)
print(proc.stdout.decode('utf-8'))
# print(proc.stderr)