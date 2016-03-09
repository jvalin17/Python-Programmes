#!/usr/bin/env python

import sys

s = []
m = []
c = 1
x = None

# input comes from STDIN (standard input)
for line in sys.stdin: 
	# remove leading and trailing whitespace
    line = line.strip()
	# split the line into count 
    b,a = line.split('\t', 1)
    
    if x == b:
        c = c + 1
    else:
        x = b
        s.append(c)
        c = 1
   
s.append(c)    
for i in range(len(s)):
    k = s.pop()
    print("%s\t%s" % (1,k))
 

               
    
    