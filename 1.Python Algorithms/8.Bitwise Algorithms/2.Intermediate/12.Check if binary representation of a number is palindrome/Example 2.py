def bin(n):
	ans="";
	while n > 0:
		ans = (str(n&1)) + ans;
		n >>= 1;
	return ans;

def checkPalindrome(x):
	s1 = bin(x)
	s2 = s1[::-1]
	return 1 if s1 == s2 else 0

# Some test cases....
x = 9;
print(checkPalindrome(x)) # output 1

x = 10
print(checkPalindrome(x)) # output 0
