# Python3 program to find the longest consecutive path
R=3
C=3

# tool matrices to recur for adjacent cells.
x = [0, 1, 1, -1, 1, 0, -1, -1]
y = [1, 0, 1, 1, -1, -1, 0, -1]

# dp[i][j] Stores length of longest consecutive path
# starting at arr[i][j].
dp=[[0 for i in range(C)]for i in range(R)]

# check whether mat[i][j] is a valid cell or not.
def isvalid( i, j):
	if (i < 0 or j < 0 or i >= R or j >= C):
		return False
	return True

# Check whether current character is adjacent to previous
# character (character processed in parent call) or not.
def isadjacent( prev, curr):
	if (ord(curr) -ord(prev)) == 1:
		return True
	return False

# i, j are the indices of the current cell and prev is the
# character processed in the parent call.. also mat[i][j]
# is our current character.
def getLenUtil(mat,i,j, prev):
	# If this cell is not valid or current character is not
	# adjacent to previous one (e.g. d is not adjacent to b )
	# or if this cell is already included in the path than return 0.
	if (isvalid(i, j)==False or isadjacent(prev, mat[i][j])==False):
		return 0

	# If this subproblem is already solved , return the answer
	if (dp[i][j] != -1):
		return dp[i][j]

	ans = 0 # Initialize answer

	# recur for paths with different adjacent cells and store
	# the length of longest path.
	for k in range(8):
		ans = max(ans, 1 + getLenUtil(mat, i + x[k],j + y[k], mat[i][j]))

	# save the answer and return
	dp[i][j] = ans
	return dp[i][j]

# Returns length of the longest path with all characters consecutive
# to each other. This function first initializes dp array that
# is used to store results of subproblems, then it calls
# recursive DFS based function getLenUtil() to find max length path
def getLen(mat, s):
	for i in range(R):
		for j in range(C):
			dp[i][j]=-1
	ans = 0
	for i in range(R):
		for j in range(C):
			# check for each possible starting po
			if (mat[i][j] == s):
				# recur for all eight adjacent cells
				for k in range(8):
					ans = max(ans, 1 + getLenUtil(mat,i + x[k], j + y[k], s));
	return ans

# Driver program
mat = [['a','c','d'],
	[ 'h','b','a'],
	[ 'i','g','f']]

print (getLen(mat, 'a'))
print (getLen(mat, 'e'))
print (getLen(mat, 'b'))
print (getLen(mat, 'f'))
