# Python 3 program to print distinct subset sums of
# a given array.

# sum denotes the current sum of the subset
# currindex denotes the index we have reached in
# the given array
def distSumRec(arr, n, sum, currindex, s):
	if (currindex > n):
		return

	if (currindex == n):
		s.add(sum)
		return

	distSumRec(arr, n, sum + arr[currindex], currindex+1, s)
	distSumRec(arr, n, sum, currindex+1, s)

# This function mainly calls recursive function
# distSumRec() to generate distinct sum subsets.
# And finally prints the generated subsets.
def printDistSum(arr,n):
	s = set()
	distSumRec(arr, n, 0, 0, s)

	# Print the result
	for i in s:
		print(i,end = " ")

# Driver code
if __name__ == '__main__':
	arr = [2, 3, 4, 5, 6]
	n = len(arr)
	printDistSum(arr, n)
