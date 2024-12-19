def binary(num):
	return int(bin(num).split('0b')[1])

if __name__ == "__main__" :
	x = 10
	binary_x = binary(x)
	print("the binary number is :",binary_x)

# This code is contributed by Rishika Gupta.
