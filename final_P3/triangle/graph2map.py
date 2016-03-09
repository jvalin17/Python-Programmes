#!/usr/bin/env python

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    
	# remove leading and trailing whitespace
    line = line.strip()
	# split the line into edges
    a,b,c = line.split('\t', 2)
    
	#paaing the values to reducer
    print("%s\t%s" % (b,a) )