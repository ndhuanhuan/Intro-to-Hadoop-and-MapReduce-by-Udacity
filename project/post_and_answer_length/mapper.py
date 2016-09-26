#!/usr/bin/env python

import sys, csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)
for line in reader:
	node_id = line[0]
	body = line[4]
	node_type = line[5]
	if node_type == "question":
		print "%s\t%s\t%d" % (node_id, "1", len(body))
	elif node_type == "answer":
		abs_parent_id = line[7]
		print "%s\t%s\t%d" % (abs_parent_id, "2", len(body))
		