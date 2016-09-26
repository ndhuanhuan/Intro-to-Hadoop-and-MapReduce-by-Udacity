#!/usr/bin/env python

import sys, csv

writer = csv.writer(sys.stdout, delimiter='\t', quoting=csv.QUOTE_NONE)

prev_id = None
student_ids = []

for line in sys.stdin:
	id, author_id = line.strip().split("\t")
	if prev_id and prev_id != id:
		writer.writerow([prev_id, student_ids])
		student_ids = []
	
	prev_id = id
	student_ids.append(author_id)

if prev_id:
	writer.writerow([prev_id, student_ids])
	student_ids = []
