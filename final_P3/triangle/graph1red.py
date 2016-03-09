#!/usr/bin/env python

import sys
count = 0
o = 0
a = 0
c = []

# input comes from STDIN
for line in sys.stdin:
    
	# remove leading and trailing whitespace
    line = line.strip()

	# parse the input we got from mapper.py
    a, b = line.split('\t', 1)
    c.append(a)
    c.append(b)
    
    
l = len(c)

for i in range (l-1):
    u = i *2
    if u > (l-1):
        break
    a = c[u]
    b = c[u+1]
        
    for m in range (l-1):
        n = m*2
        if n > l-1:
            o = o +1
        else:
            x = c[n]
            y = c[n+1]            
            if b == x:
                k = x
                for j in range (l-1):
                    s = (j*2)
                    if s > l-1 and s != u:
                        o = o +1
                    else:
                        g = c[s]
                        f = c[s + 1 ]
                        if g == y and f == a:
                            print("%s%s%s\t%s%s\t%s%s"%(a,g,b,b,a,g,a))
                            
                           
                
        
    
    