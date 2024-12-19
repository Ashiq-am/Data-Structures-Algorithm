k = 3

# Multiply Two Matrix Function


def multiply(A, B):

	# third matrix to store multiplication of Two matrix9*
	C = [[0 for x in range(k+1)] for y in range(k+1)]

	for i in range(1, k+1):
		for j in range(1, k+1):
			for x in range(1, k+1):
				C[i][j] = (C[i][j] + (A[i][x] * B[x][j]))

	return C

# Optimal Way For finding pow(t,n)
# If n Is Odd then It Will be t*pow(t,n-1)
# else return pow(t,n/2)*pow(t,n/2)


def pow(t, n):
	# base Case
	if (n == 1):
		return t
	# Recurrence Case
	if (n & 1):
		return multiply(t, pow(t, n - 1))
	else:
		X = pow(t, n // 2)
	return multiply(X, X)


def compute(n):
	# base Case
	if (n == 0):
		return 1
	if (n == 1):
		return 1
	if (n == 2):
		return 2

	# Function Vector(indexing 1 )
	# that is [1,2]
	f1 = [0]*(k + 1)
	f1[1] = 1
	f1[2] = 2
	f1[3] = 4

	# Constructing Transformation Matrix that will be
	# [[0,1,0],[0,0,1],[3,2,1]]

	t = [[0 for x in range(k+1)] for y in range(k+1)]
	for i in range(1, k+1):
		for j in range(1, k+1):
			if (i < k):
				# Store 1 in cell that is next to diagonal of Matrix else Store 0 in
				# cell
				if (j == i + 1):
					t[i][j] = 1
				else:
					t[i][j] = 0
				continue
			# Last Row - store the Coefficients in reverse order
			t[i][j] = 1

	# Computing T^(n-1) and Setting Transformation matrix T to T^(n-1)
	t = pow(t, n - 1)
	sum = 0
	# Computing first cell (row=1,col=1) For Resultant Matrix TXF
	for i in range(1, k+1):
		sum += t[1][i] * f1[i]
	return sum


# Driver Code
n = 4
print(compute(n))

n = 5
print(compute(n))

n = 10
print(compute(n))
