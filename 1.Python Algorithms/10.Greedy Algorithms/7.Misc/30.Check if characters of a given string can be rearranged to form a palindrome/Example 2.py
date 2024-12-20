'''
* function to check whether characters of
a string can form a palindrome
'''


def canFormPalindrome(strr):

	# Create a listt
	listt = []

	# For each character in input strings,
	# remove character if listt contains
	# else add character to listt
	for i in range(len(strr)):
		if (strr[i] in listt):
			listt.remove(strr[i])
		else:
			listt.append(strr[i])

	# if character length is even
	# list is expected to be empty
	# or if character length is odd
	# listt size is expected to be 1
	if (len(strr) % 2 == 0 and len(listt) == 0 or
			(len(strr) % 2 == 1 and len(listt) == 1)):
		return True
	else:
		return False


# Driver code
if (canFormPalindrome("geeksforgeeks")):
	print("Yes")
else:
	print("No")

if (canFormPalindrome("geeksogeeks")):
	print("Yes")
else:
	print("No")
