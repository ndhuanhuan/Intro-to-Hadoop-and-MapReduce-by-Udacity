#!/usr/bin/env python

import sys, csv, re

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
	node_id = line[0]
	body = line[4]
	words = re.split(r"\W+", body)
	for word in words:
		print "{0}\t{1}".format(word.lower(), node_id)
