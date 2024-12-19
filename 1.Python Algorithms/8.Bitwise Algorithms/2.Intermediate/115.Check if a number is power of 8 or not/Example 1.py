# Python3 program to check
# if a number is power of 8
from math import log,trunc

# function to check if power of 8
def checkPowerof8(n):

	# calculate log8(n)
	i = log(n, 8)

	# check if i is an integer or not
	return (i - trunc(i) < 0.000001);

# Driver Code
n = 65
if checkPowerof8(n):
	print("Yes")
else:
	print("No")

# This code is contributed by Mohit Kumar
