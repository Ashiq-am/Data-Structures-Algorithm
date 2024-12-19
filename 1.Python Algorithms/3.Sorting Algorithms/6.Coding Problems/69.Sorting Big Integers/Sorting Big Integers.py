# Below is Python code to sort the Big integers
# in ascending order
def SortingBigIntegers(arr, n):
    # Direct sorting using lamda operator
    # and length comparison
    arr.sort(key=lambda x: (len(x), x))

# Driver code of above implementation
arr = ["54", "724523015759812365462",
       "870112101220845", "8723"]
n = len(arr)

SortingBigIntegers(arr, n)

# Print the final sorted list using
# join method
print(" ".join(arr))
