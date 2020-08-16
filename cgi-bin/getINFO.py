#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
import subprocess
import json
cmd = "python3 /var/www/mini-hoen/service_request.py info -j"
proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
cgitb.enable()
a = proc.stdout.decode('utf-8')
# d = str(a).replace("'", '"')
# Json = json.dumps(a)



print('Content-Type: text/html')
print()
# a=json.dumps(proc.stdout.decode('utf-8'),indent=3)
print(a)
# print(proc.stderr)