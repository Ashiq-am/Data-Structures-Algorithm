# Returns count of ways n people
# can remain single or paired up.
def countFriendsPairings(n):
	a, b, c = 1, 2, 0
	if (n <= 2):
		return n
	for i in range(3, n + 1):
		c = b + (i - 1) * a
		a = b
		b = c
	return c

# Driver code
n = 4
print(countFriendsPairings(n))


