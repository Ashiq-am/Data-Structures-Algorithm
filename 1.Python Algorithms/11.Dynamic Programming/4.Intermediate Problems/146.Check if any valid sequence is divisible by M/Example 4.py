# Python3 program for the above approach

# Function to check if any valid
# sequence is divisible by M
def func(n, m, A):

	# DEclare mod array
	ModArray = [0]*n
	Sum = 0

	# Calculate the mod array
	for i in range(n):
		ModArray[i] = A[i] % m
		Sum += ModArray[i]

	Sum = Sum % m

	# Check if sum is divisible by M
	if (Sum % m == 0) :
		print("True")
		return

	# Check if sum is not divisible by 2
	if (Sum % 2 != 0) :
		print("False")

	else :

		# Remove the first element from
		# the ModArray since it is not
		# possible to place minus
		# on the first element
		ModArray.pop(0)
		i = 0

		# Decrease the size of array
		j = len(ModArray) - 1

		# Sort the array
		ModArray.sort()
		Sum = Sum // 2

		# Loop until the pointer
		# cross each other
		while (i <= j) :
			s = ModArray[i] + ModArray[j]

			# Check if sum becomes equal
			if (s == Sum) :
				i1 = i
				i2 = j
				print("True")
				break

			# Increase and decrease
			# the pointer accordingly
			elif (s > Sum):
				j -= 1

			else:
				i += 1

# Driver code
m = 2
a = [ 1, 3, 9 ]
n = len(a)

# Function call
func(n, m, a)
