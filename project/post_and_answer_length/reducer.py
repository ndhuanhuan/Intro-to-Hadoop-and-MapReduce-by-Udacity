#!/usr/bin/env python

import sys

prev_id = None
question_length = 0
answer_length_sum = 0.0
answer_count = 0

for line in sys.stdin:
	id, type, length = line.strip().split("\t")

	if prev_id and prev_id != id:
		if answer_count == 0:
			answer_length_average = 0
		else:
			answer_length_average = answer_length_sum / answer_count
		print prev_id, "\t", question_length, "\t", answer_length_average
		question_length = 0
		answer_length_sum = 0.0
		answer_count = 0

	prev_id = id
	if type == "1":
		question_length = int(length)
	elif type == "2":
		answer_length_sum += int(length)
		answer_count += 1

if prev_id:
	if answer_count == 0:
		answer_length_average = 0
	else:
		answer_length_average = answer_length_sum / answer_count
	print prev_id, "\t", question_length, "\t", answer_length_average
	question_length = 0
	answer_length_sum = 0.0
	answer_count = 0
	