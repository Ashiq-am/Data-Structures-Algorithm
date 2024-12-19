# Python3 program to find lexicographically largest
# subsequence where every character appears at
# least k times.

# Find lexicographically largest subsequence of
# s[0..n-1] such that every character appears
# at least k times. The result is filled in t[]
def subsequence(s, t, n, k):
	last = 0
	cnt = 0
	new_last = 0
	size = 0

	string = 'zyxwvutsrqponmlkjihgfedcba'

	# Starting from largest charter 'z' to 'a'
	for ch in string:
		cnt = 0
		for i in range(last, n):
			if s[i] == ch:
				cnt += 1

		# If frequency is greater than k
		if cnt >= k:

			# From the last point we leave
			for i in range(last, n):

				# check if string contain ch
				if s[i] == ch:

					# If yes, append to output string
					t[size] = ch
					new_last = i
					size += 1

			# Update the last point.
			last = new_last

# Driver Code
if __name__ == "__main__":
	s = ['b', 'a', 'n', 'a', 'n', 'a']
	n = len(s)
	k = 2
	t = [''] * n
	subsequence(s, t, n - 1, k)
	t = ''.join(t)
	print(t)
