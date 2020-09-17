#!/usr/bin/env python3.8

import os
result = os.popen("curl https://openhackbxb3pxs9userprofile-staging.azurewebsites.net/api/healthcheck/user").read()
print(result)
