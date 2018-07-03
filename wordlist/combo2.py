from itertools import product
import sys

symbols = []

for i in range(len(sys.argv)):
	if i == 0:
		continue
	else:
		symbols.append(sys.argv[i])

for j in range(1, len(symbols)):
	for l in product(symbols, repeat=j):
		print("".join(l))
