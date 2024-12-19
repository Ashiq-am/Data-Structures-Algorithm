# Python3 program to find optimal number
# of trials for k floors and 2 eggs.
import math as mt

def twoEggDrop(k):
	return mt.ceil((-1.0 +
		mt.sqrt(1 + 8 * k)) / 2)

# Driver Code
k = 100
print(twoEggDrop(k))
