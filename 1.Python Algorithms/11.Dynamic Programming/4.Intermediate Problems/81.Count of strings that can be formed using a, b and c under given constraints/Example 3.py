# A O(1) Python3 program to find
# number of strings that can be
# made under given constraints.

def countStr(n):
	return (1 + (n * 2) +
				(n * ((n * n) - 1) // 2))

# Driver code
if __name__ == "__main__":
	n = 3
	print(countStr(n))
