#!/usr/bin/env python

import sys

prev_store = None
highest_sale = 0.0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    current_store, current_sale = data

    current_sale_float = float(current_sale)
    if current_sale_float > highest_sale:
        highest_sale = current_sale_float

    if prev_store and prev_store != current_store:
        print "{0}\t{1}".format(prev_store, highest_sale)
        highest_sale = 0.0

    prev_store = current_store

if prev_store != None:
    print "{0}\t{1}".format(prev_store, highest_sale)

