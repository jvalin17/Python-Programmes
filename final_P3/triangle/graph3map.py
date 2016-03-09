#!/usr/bin/env python

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	
	a,b = line.split('\t',1)
	# increase counters
	print("%s\t%s" % (a,b) )
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		
		

