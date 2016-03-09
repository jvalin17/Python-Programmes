#!/usr/bin/env python
import sys
import re
c = 0 

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = re.findall(r"[\'A-Za-z]+", line)
    # increase counters
    for word in words:
        v = line.split(":")
        speaker = v.pop(0)
        if word in speaker:
            x = c+1
        else:
            word = word.lower()
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
            if word in speaker:
                c = c+1
            else:
                print('%s\t%s\t%s' % (speaker, word, 1))