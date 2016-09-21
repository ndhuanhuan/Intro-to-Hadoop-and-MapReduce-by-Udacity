#!/usr/bin/env python

import sys

num_sales = 0
total_sales = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    store, sale = data
    num_sales += 1
    total_sales += float(sale)

print "{0}\t{1}".format(num_sales, total_sales)

