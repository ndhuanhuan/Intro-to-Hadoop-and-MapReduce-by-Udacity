#!/usr/bin/env python

import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split("\t")
	date, time, store, item, cost, payment = data
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
	print weekday, "\t", cost
	