# This function assumes that a[] is
# sorted. If a[] is not sorted, we need
# to sort it first.
def minCostToMakeElementEqual(a):
	l = len(a)

	# If there are odd elements, we choose
	# middle element
	if (l%2 == 1):
		y = a[l//2]

	# If there are odd elements, then we choose
	# the average of middle two.
	else:
		y = (a[l//2] + a[(l-2)//2])//2

	# After deciding the final value, find the
	# result.
	s = 0
	for i in range(l):
		s += abs(a[i]-y)
	return s

# Driver code
a = [1, 100, 101]
print(minCostToMakeElementEqual(a))
