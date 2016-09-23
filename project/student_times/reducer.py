#!/usr/bin/env python

import sys

prev_id = None
hour_counts = [0] * 24

for line in sys.stdin:
	id, hour = line.strip().split('\t')

	if prev_id and prev_id != id:
		max_value = max(hour_counts)
		max_hour = hour_counts.index(max_value)
		print prev_id, "\t", max_hour
		hour_counts = [0] * 24

	prev_id = id
	hour_counts[int(hour)] += 1

if prev_id:
	max_value = max(hour_counts)
	max_hour = hour_counts.index(max_value)
	print prev_id, "\t", max_hour
	