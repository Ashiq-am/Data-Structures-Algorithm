# Python3 Program to count substrings
# which are divisible by 8 but not by 3

# Returns count of substrings
# divisible by 8 but not by 3.
def count(s, Len):
	global MAX
	cur = 0
	dig = 0
	Sum = [0] * MAX
	dp = [[0, 0, 0] for i in range(MAX)]

	dp[0][0] = 1

	# Iterating the string.
	for i in range(1, Len + 1):
		dig = int(s[i - 1]) - 48
		cur += dig
		cur %= 3

		Sum[i] = cur

		# Prefix sum of number of substrings
		# whose sum of digits mudolo 3 is
		# 0, 1, 2.
		dp[i][0] = dp[i - 1][0]
		dp[i][1] = dp[i - 1][1]
		dp[i][2] = dp[i - 1][2]

		dp[i][Sum[i]] += 1

	ans = 0
	dprev = 0
	value = 0
	dprev2 = 0

	# Iterating the string.
	for i in range(1, Len + 1):
		dig = int(s[i - 1]) - 48

		# Since single digit 8 is
		# divisible by 8 and not by 3.
		if dig == 8:
			ans += 1

		# Taking two digit number.
		if i - 2 >= 0:
			dprev = int(s[i - 2]) - 48 # 10th position
			value = dprev * 10 + dig # Complete 2 digit
									# number

			if (value % 8 == 0) and (value % 3 != 0):
				ans += 1

		# Taking 3 digit number.
		if i - 3 >= 0:
			dprev2 = int(s[i - 3]) - 48 # 100th position
			dprev = int(s[i - 2]) - 48 # 10th position

			# Complete 3 digit number.
			value = (dprev2 * 100 +
					dprev * 10 + dig)

			if value % 8 != 0:
				continue

			# If number formed is divisible by 8
			# then last 3 digits are also divisible
			# by 8. Then all the substring ending
			# at this index are divisible.
			ans += (i - 2)

			# But those substring also contain
			# number which are not divisible
			# by 3 so remove them.
			ans -= (dp[i - 3][Sum[i]])

	return ans

# Driver Code
MAX = 1000
Str = "6564525600"
Len = len(Str)
print(count(Str, Len))
