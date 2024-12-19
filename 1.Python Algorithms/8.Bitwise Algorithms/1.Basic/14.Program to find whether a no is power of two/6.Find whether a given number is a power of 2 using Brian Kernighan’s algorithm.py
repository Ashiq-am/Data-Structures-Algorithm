# Python3 program of the above approach

# Function to check if x is power of 2


def isPowerofTwo(n):

	return (n != 0) and ((n & (n - 1)) == 0)


# Driver code
if __name__ == "__main__":

		# Function call
	if isPowerofTwo(30):
		print("Yes")
	else:
		print("No")

	if isPowerofTwo(128):
		print("Yes")
	else:
		print("No")

# this code is contributed by aditya942003patil
