#!/usr/bin/env python

import sys

hit_count = 0

for line in sys.stdin:
    ip = line.strip()

    if ip == "10.99.99.186":
        hit_count += 1

print hit_count
