#defining a function computeXOR
def computeXOR(n):
	uni = 0
	if n==0:
		return 0 #base case
	for i in range(1,n+1):
		uni = uni ^ i
	return uni

n = 7
ans = computeXOR(n) #calling the function
print(ans)

#This code is contributed by Gayatri Deshmukh
