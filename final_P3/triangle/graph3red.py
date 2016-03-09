#!/usr/bin/env python


import sys
count = 0

for line in sys.stdin:
    line = line.strip()
	

    a,b = line.split('\t', 1)
    a = int(a)
    b = int(b)
    count = count + (b*a) 
    
    
    
count = count/3
print (count)    
