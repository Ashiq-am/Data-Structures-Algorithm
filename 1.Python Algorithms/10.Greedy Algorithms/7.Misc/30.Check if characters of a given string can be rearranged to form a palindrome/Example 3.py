# Python3 implementation of above approach.
def canFormPalindrome(s):
	bitvector = 0
	for str in s:
		bitvector ^= 1 << ord(str)
	return bitvector == 0 or bitvector & (bitvector - 1) == 0


#s = input()
if canFormPalindrome("geeksforgeeks"):
	print('Yes')
else:
	print('No')
