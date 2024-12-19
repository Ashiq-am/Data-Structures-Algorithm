# Python3 program to find number of diagonals
# in n sided convex polygon
def numberOfDiagonals(n):
	return n * (n - 3) / 2


# driver code to test above function
def main():
	n = 5
	print(n , " sided convex polygon have ")
	print(numberOfDiagonals(n) , " diagonals")

if __name__ == '__main__':
	main()
