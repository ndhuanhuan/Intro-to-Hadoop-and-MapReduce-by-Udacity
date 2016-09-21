#!/usr/bin/env python

import sys

prev_path = None
current_path_count = 0

for line in sys.stdin:
    current_path = line.strip()

    if prev_path and prev_path != current_path:
        print "{0}\t{1}".format(prev_path, current_path_count)
        current_path_count = 0

    prev_path = current_path
    current_path_count += 1

if prev_path != None:
    print "{0}\t{1}".format(prev_path, current_path_count)
