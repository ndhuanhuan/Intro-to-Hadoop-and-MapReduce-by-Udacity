#!/usr/bin/env python

import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split("\t")
	date, time, store, item, cost, payment = data
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
	print "{0}\t{1}".format(weekday, cost)
root@osboxes:~# cat reducer.py 
#!/usr/bin/env python

import sys

prev_weekday = None
sales_count = 0
sales_sum = 0.0

for line in sys.stdin:
	weekday, sale = line.strip().split("\t")
	if prev_weekday and prev_weekday != weekday:
		sales_mean = sales_sum / sales_count
		print prev_weekday, sales_mean

	prev_weekday = weekday
	sales_count += 1
	sales_sum += float(sale)

if prev_weekday != None:
	sales_mean = sales_sum / sales_count
	print prev_weekday, sales_mean
	