def countPairsBruteForce(X, Y, m, n):
	ans = 0
	for i in range(m):
		for j in range(n):
			if (pow(X[i], Y[j]) > pow(Y[j], X[i])):
				ans += 1
	return ans