#!/usr/bin/env python

import sys

current_word = None
current_speaker = None
current_count = 0
x = 0

stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other","some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    
    # parse the input we got from mapper.py
    speaker, word, count = line.split('\t', 2)

    
    if current_speaker == speaker:
        
    # convert count (currently a string) to int
        try:
            count = int (count)
        except ValueError:
            continue
        # count was not a number, so silently
        # ignore/discard this line


	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reduce
        if word in stopwords:
            x =x +1
        else:
            if current_word == word:
                current_count = current_count + count
            else:
                if current_word:                
                    if current_count > 200:
                        print('%s\t%s\t%s' % (current_speaker, current_word, current_count))
                    current_count = count
                    current_word = word
    else:
        count  = int(count)
        current_speaker = speaker
        current_count = count
        current_word = word
            
# do not forget to output the last word if needed!

        #print('%s\t%s\t%s' % (current_speaker,current_word, current_count))