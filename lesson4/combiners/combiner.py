#!/usr/bin/env python

import sys

prev_weekday = None
sales_sums = [0.0] * 7

for line in sys.stdin:
	weekday, sale = line.strip().split("\t")
	sales_sums[int(weekday)] += float(sale)
for weekday, sales_sum in enumerate(sales_sums):
	print weekday, "\t", sales_sum
	