
import sys
import re
for line in sys.stdin:
	for word in re.split('\\W+',line):#
		if len(word) > 0:
			print(word[:1]+'\t'+ str(len(word)))


#!/usr/bin/python
#import sys

#for line in sys.stdin:
#	line = line.strip() #remove leading and trailing whitespaces
#	words = line.split() #split the line into words and returns as a list
#for word in words:
#write the results to standard output STDOUT
#	print'%s    %s' % (word,1) #Emit the word

