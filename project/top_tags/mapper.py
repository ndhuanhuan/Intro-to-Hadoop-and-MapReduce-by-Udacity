#!/usr/bin/env python

import sys, csv

tag_dict = {}

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)
for line in reader:
	node_type = line[5]
	tags = line[2]
	tags = tags.split()
	for tag in tags:
		value = tag_dict.get(tag)
		if value != None:
			tag_dict[tag] += 1
		else:
			tag_dict[tag] = 1

for tag, count in tag_dict.items():
	print "%s\t%d" % (tag, count)
