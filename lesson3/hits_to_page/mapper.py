#!/usr/bin/env python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, id, user, datetime, timezone, method, path, protocol, status, size = data
        print path
        