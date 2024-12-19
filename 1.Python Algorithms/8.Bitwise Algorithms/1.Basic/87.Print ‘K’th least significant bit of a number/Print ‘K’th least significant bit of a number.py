# Python code to print 'K'th LSB

# Function returns 1 if set, 0 if not
def LSB(num, K):
	return bool(num & (1 << (K - 1) ))

# Driver code
num, k = 10, 4

res = LSB(num, k)
if res :
	print(1)
else:
	print(0)

#This code is contributed by Sachin Bisht
