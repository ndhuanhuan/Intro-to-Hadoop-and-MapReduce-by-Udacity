#!/usr/bin/env python

import sys

count_of_fantastic = 0
node_list_of_fantastically = []

for line in sys.stdin:
	word, node_id = line.rstrip().split("\t")
	if word == "fantastic":
		count_of_fantastic += 1
	elif word == "fantastically":
		node_list_of_fantastically.append(int(node_id))

print "count_of_fantastic", count_of_fantastic
for node_id in sorted(node_list_of_fantastically):
	print node_id
	