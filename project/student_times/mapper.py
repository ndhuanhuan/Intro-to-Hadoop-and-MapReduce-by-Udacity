#!/usr/bin/env python

import sys, csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)
for line in reader:
	author_id, added_at = line[3], line[8]
	date, time = added_at.split()
	print author_id, "\t", int(time[0:2])
