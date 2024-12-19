# Python program to count PanDigital pairs
pandigitalMask = ((1 << 10) - 1)
freq = dict()

def computeMaskFrequencies(v):
	global freq
	for i in range(len(v)):

		mask = 0

		# Stores digits present in string v[i]
		# atleast once. We use a set as we only
		# need digits which exist only once
		# (irrespective of reputation)
		digits = set()

		for j in range(len(v[i])):
			digits.add(int(v[i][j]))

		# Calculate the mask by considering
		# all digits existing atleast once
		for it in digits:

			digit = it
			mask += (1 << digit)

		# Increment the frequency of this mask
		if mask in freq:
			freq[mask] += 1

		else:
			freq[mask] = 1


# Returns number of pairs of strings resulting
# in Pandigital Concatenations
def pandigitalConcatenations():
	global freq

	ans = 0

	# All possible strings lie between 1 and 1023
	# so we iterate over every possible mask
	for i in range(1, 1024):
		for j in range(1, 1024):

			# if the concatenation results in mask of
			# Pandigital Concatenation, calculate all
			# pairs formed with Masks i and j
			if ((i | j) == pandigitalMask and
					i in freq and j in freq):

				if (i == j):
					ans += (freq[i] * (freq[i] - 1))
				else:
					ans += (freq[i] * freq[j])

	# Since every pair is considers twice,
	# we get rid of half of these
	return ans // 2


def countPandigitalPairs(v):

	# Find frequencies of all masks in
	# given vector of strings
	computeMaskFrequencies(v)

	# Return all possible concatenations.
	return pandigitalConcatenations()

# Driver code
v = ["123567", "098234", "14765", "19804"]
print(countPandigitalPairs(v))
