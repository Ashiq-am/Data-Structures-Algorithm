# Python3 soln using mathematical approach
# factorial array is stored dynamically
fact = [1]
def preComputeFact(n):
	for i in range(1, n+1):
		fact.append((fact[i-1]*i))

# Returns count of ways n people
# can remain single or paired up.
def countFriendsPairings(n):
	ones = n
	twos = 1
	ans = 0
	while(ones >= 0):
		# pow of 1 will always be one
		ans = ans + (fact[n]//(twos*fact[ones]*fact[(n-ones)//2]))
		ones = ones - 2
		twos = twos * 2
	return(ans)


# Driver Code
# pre-compute factorial
preComputeFact(1000)
n = 4
print(countFriendsPairings(n))
