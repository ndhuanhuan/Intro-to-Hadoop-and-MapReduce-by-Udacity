#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, id, user, datetime, timezone, method, path, protocol, status, size = data
        path = re.sub(r"^http://www.the-associates.co.uk", '', path)
        print path
