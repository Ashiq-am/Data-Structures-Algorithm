# Optimised school method based PYTHON program
# to check if a number is prime
# import the math module
import math

# function to check weather the number is prime or not


def isPrime(n):

	# Corner case
	if (n <= 1):
		return False

	# Check from 2 to square root of n
	for i in range(2, int(math.sqrt(n)) + 1):
		if (n % i == 0):
			return False
	return True


# Driver Program to test above function
print("true") if isPrime(11) else print("false")
print("true") if isPrime(15) else print("false")

# This code is contributed by bhoomikavemula
