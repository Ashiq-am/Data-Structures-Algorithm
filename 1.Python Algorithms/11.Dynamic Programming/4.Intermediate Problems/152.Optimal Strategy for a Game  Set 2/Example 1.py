# python3 program to find out maximum value from a
# given sequence of coins

def oSRec (arr, i, j, Sum):

	if (j == i + 1):
		return max(arr[i], arr[j])

	# For both of your choices, the opponent
	# gives you total Sum minus maximum of
	# his value
	return max((Sum - oSRec(arr, i + 1, j, Sum - arr[i])),
				(Sum - oSRec(arr, i, j - 1, Sum - arr[j])))

# Returns optimal value possible that a player can
# collect from an array of coins of size n. Note
# than n must be even
def optimalStrategyOfGame(arr, n):

	Sum = 0
	Sum = sum(arr)
	return oSRec(arr, 0, n - 1, Sum)

# Driver code

arr1= [ 8, 15, 3, 7]
n = len(arr1)
print(optimalStrategyOfGame(arr1, n))

arr2= [ 2, 2, 2, 2 ]
n = len(arr2)
print(optimalStrategyOfGame(arr2, n))

arr3= [ 20, 30, 2, 2, 2, 10 ]
n = len(arr3)
print(optimalStrategyOfGame(arr3, n))
