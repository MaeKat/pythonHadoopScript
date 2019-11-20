from operator import itemgetter
import sys

current_word = None
current_count = 0.0
word = None
counter = 1.0


for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t', 1)
	try:
		count = int(count)
	except ValueError:
		continue

	if current_word == word:
		current_count += count
		counter = counter + 1
	else:
		current_count = current_count / counter
		if current_word:
			print '%s\t%s' % (current_word, current_count)
		current_count = count
		current_word = word


if current_word == word:
	current_count = current_count / counter
	print '%s\t%s' % (current_word, current_count)
