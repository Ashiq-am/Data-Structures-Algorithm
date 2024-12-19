# Python3 Program for the binary
# representation of a given number


def bin(n):

	if n > 1:
		bin(n//2)

	print(n % 2, end="")


# Driver Code
if __name__ == "__main__":

	bin(7)
	print()
	bin(4)

# This code is contributed by ANKITRAI1
