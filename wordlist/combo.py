from itertools import combinations
import sys

symbols = ""

for i in range(len(sys.argv)):
	if i == 0:
		continue
	else:
		symbols += sys.argv[i]

max_length = len(symbols)

for length in range(0, max_length + 1):
	for word in map("".join, combinations(symbols, length)):
		print(word)
