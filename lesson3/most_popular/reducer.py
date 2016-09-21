#!/usr/bin/env python

import sys

prev_path = None
current_path_count = 0

most_popular_path = None
most_popular_path_count = 0

for line in sys.stdin:
    current_path = line.strip()

    if prev_path and prev_path != current_path:
        if current_path_count > most_popular_path_count:
            most_popular_path = prev_path
            most_popular_path_count = current_path_count
        current_path_count = 0

    prev_path = current_path
    current_path_count += 1

print "{0}\t{1}".format(most_popular_path, most_popular_path_count)
