# Python3 Implementation to find the line passing
# through two points

# This pair is used to store the X and Y
# coordinate of a point respectively
# define pdd pair<double, double>

# Function to find the line given two points


def lineFromPoints(P, Q):

	a = Q[1] - P[1]
	b = P[0] - Q[0]
	c = a*(P[0]) + b*(P[1])

	if(b < 0):
		print("The line passing through points P and Q is:",
			a, "x - ", b, "y = ", c, "\n")
	else:
		print("The line passing through points P and Q is: ",
			a, "x + ", b, "y = ", c, "\n")


# Driver code
if __name__ == '__main__':
	P = [3, 2]
	Q = [2, 6]
	lineFromPoints(P, Q)

# This code is contributed by ash264
