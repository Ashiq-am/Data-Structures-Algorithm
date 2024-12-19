# The function that adds two-bit sequences and returns the addition
def addBitStrings(str1, str2):
	ans = ''
	i = len(str1) - 1
	j = len(str2) - 1
	carry = 0
	while i >= 0 or j >= 0 or carry:
		if i >= 0:
			carry += ord(str1[i]) - ord('0')
			i = i - 1
		else:
			carry += 0

		if j >= 0:
			carry += ord(str2[j]) - ord('0')
			j = j - 1
		else:
			carry += 0

		ans = chr(ord('0') + carry % 2) + ans
		carry = carry // 2
	return ans


# Driver program to test above functions
str1 = '1100011'
str2 = '10'

print('Sum is ', addBitStrings(str1, str2))

# This code is contributed by ajaymakavan.
