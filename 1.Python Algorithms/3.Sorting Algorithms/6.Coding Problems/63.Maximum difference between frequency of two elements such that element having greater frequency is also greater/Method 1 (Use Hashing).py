# Python program to find maximum difference
# between frequency of any two element
# such that element with greater frequency
# is also greater in value.

from collections import defaultdict

# Return the maximum difference between
# frequencies of any two elements such that
# element with greater frequency is also
# greater in value.
def maxdiff(arr, n):
	freq = defaultdict(lambda: 0)

	# Finding the frequency of each element.
	for i in range(n):
		freq[arr[i]] += 1
	ans = 0
	for i in range(n):
		for j in range(n):

			# finding difference such that element
			# having greater frequency is also
			# greater in value.
			if freq[arr[i]] > freq[arr[j]] and arr[i] > arr[j]:
				ans = max(ans, freq[arr[i]] - freq[arr[j]])
			elif freq[arr[i]] < freq[arr[j]] and arr[i] < arr[j]:
				ans = max(ans, freq[arr[j]] - freq[arr[i]])
	return ans


arr = [3,1,3,2,3,2]
n = len(arr)
print(maxdiff(arr,n))
