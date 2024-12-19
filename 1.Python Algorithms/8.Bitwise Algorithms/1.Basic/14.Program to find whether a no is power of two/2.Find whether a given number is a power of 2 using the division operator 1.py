# Python program for above approach

# function which checks whether a
# number is a power of 2


def powerof2(n):

	# base cases
	# '1' is the only odd number
	# which is a power of 2(2^0)
	if n == 1:
		return True

	# all other odd numbers are not powers of 2
	elif n % 2 != 0 or n == 0:
		return False

	# recursive function call
	return powerof2(n/2)


# Driver Code
if __name__ == "__main__":

		# Function call
	print(powerof2(64)) # True
	print(powerof2(12)) # False

# code contributed by Moukthik a.k.a rowdyninja
