#!/usr/bin/env python3.8

import os
import re

result = os.popen("curl https://openhackbxb3pxs9userprofile-staging.azurewebsites.net/api/healthcheck/user").read()

if re.findall('\\bhealthy\\b', result):
    print("The word healthy was found")
else:
    print("Not found")