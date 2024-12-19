# Python3 program to find temple
# offerings required
from typing import List

# To store count of increasing order temples
# on left and right (including current temple)


class Temple:
	def __init__(self, l: int, r: int):

		self.L = l
		self.R = r

# Returns count of minimum offerings for
# n temples of given heights.


def offeringNumber(n: int,
				templeHeight: List[int]) -> int:

	# Initialize counts for all temples
	chainSize = [0] * n

	for i in range(n):
		chainSize[i] = Temple(-1, -1)

	# Values corner temples
	chainSize[0].L = 1
	chainSize[-1].R = 1

	# Filling left and right values
	# using same values of previous(or next
	for i in range(1, n):
		if templeHeight[i - 1] < templeHeight[i]:
			chainSize[i].L = chainSize[i - 1].L + 1
		else:
			chainSize[i].L = 1

	for i in range(n - 2, -1, -1):
		if templeHeight[i + 1] < templeHeight[i]:
			chainSize[i].R = chainSize[i + 1].R + 1
		else:
			chainSize[i].R = 1

	# Computing max of left and right for all
	# temples and returning sum
	sm = 0
	for i in range(n):
		sm += max(chainSize[i].L,
				chainSize[i].R)

	return sm


# Driver code
if __name__ == '__main__':

	arr1 = [1, 2, 2]
	print(offeringNumber(3, arr1))

	arr2 = [1, 4, 3, 6, 2, 1]
	print(offeringNumber(6, arr2))
