# Python program to find Non-decreasing sequence
# of size k with minimum sum

# Global table used for memoization
from urllib3.connectionpool import xrange

dp = []
for i in xrange(10**2 + 1):
	temp = [-1]*(10**2 + 1)
	dp.append(temp)

def solve(a, i, k):
	if dp[i][k] != -1: # Memoization
		return dp[i][k]
	elif i < 0: # out of bounds
		return float('inf')

	# when there is only one element
	elif k == 1:
		return min(a[: i + 1])

	# Else two cases
	# 1 include current element
	# solve(a, j, k-1) + a[i]
	# 2 ignore current element
	# solve(a, j, k)
	else:
		ans = float('inf')
		for j in xrange(i):
			if a[i] >= a[j]:
				ans = min(ans, solve(a, j, k), solve(a, j, k-1) + a[i])
			else:
				ans = min(ans, solve(a, j, k))
		dp[i][k] = ans
		return dp[i][k]

# Driver code
a = [58, 12, 11, 12, 82, 30, 20, 77, 16, 86]
print(solve(a, len(a)-1, 4))
