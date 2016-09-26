#!/usr/bin/env python

import sys

top_tags = []
number_of_top = 10
min_index = 0

for line in sys.stdin:
	tag, count = line.strip().split("\t")
	list_len = len(top_tags)
	if list_len == number_of_top: 
		key, min_value = top_tags[min_index]
		if min_value < count:
			top_tags[min_index] = (tag, int(count))
		min_index = top_tags.index(min(top_tags, key=lambda x: x[1]))
	elif list_len == number_of_top - 1:
		top_tags.append((tag, int(count)))
		min_index = top_tags.index(min(top_tags, key=lambda x: x[1]))
	elif list_len < number_of_top - 1:
		top_tags.append((tag, int(count)))

for tag, count in sorted(top_tags, key=lambda x: x[1], reverse=True):
	print "%s\t%d" % (tag, count)
