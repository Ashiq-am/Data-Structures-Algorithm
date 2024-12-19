# Python 3 program to
# check if a number is
# divisible by 17 or
# not using bitwise
# operator.

# function to check recursively if the
# number is divisible by 17 or not
def isDivisibleby17(n):

	# if n=0 or n=17 then yes
	if (n == 0 or n == 17):
		return True

	# if n is less than 17, not
	# divisible by 17
	if (n < 17):
		return False

	# reducing the number by floor(n/16)
	# - n%16
	return isDivisibleby17((int)(n >> 4) - (int)(n & 15))


# driver code to check the above function
n = 35
if (isDivisibleby17(n)):
	print(n,"is divisible by 17")
else:
	print(n,"is not divisible by 17")

# This code is contributed by
# Smitha Dinesh Semwal
