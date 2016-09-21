#!/usr/bin/env python

import sys

prev_item = None
total_sales = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    current_item, current_sale = data

    if prev_item and prev_item != current_item:
        print "{0}\t{1}".format(prev_item, total_sales)
        total_sales = 0

    prev_item = current_item
    total_sales += float(current_sale)

if prev_item != None:
    print "{0}\t{1}".format(prev_item, total_sales)

