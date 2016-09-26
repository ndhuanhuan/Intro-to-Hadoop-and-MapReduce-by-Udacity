#!/usr/bin/env python

import sys, csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)
for line in reader:
	author_id = line[3]
	node_type = line[5]
	if node_type == "question":
		id = line[0]
	elif node_type == "answer":
		id = line[7]

	print "%s\t%s" % (id, author_id)
