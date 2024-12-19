# Python3 program to find whether
# two elements exist whose sum is
# equal to sum of rest of the elements.

# Function to check whether two
# elements exist whose sum is equal
# to sum of rest of the elements.
def checkPair(arr, n):
    s = set()
    sum = 0

    # Find sum of whole array
    for i in range(n):
        sum += arr[i]

    # / If sum of array is not
    # even than we can not
    # divide it into two part
    if sum % 2 != 0:
        return False
    sum = sum / 2

    # For each element arr[i], see if
    # there is another element with
    # value sum - arr[i]
    for i in range(n):
        val = sum - arr[i]
        if arr[i] not in s:
            s.add(arr[i])

        # If element exist than
        # return the pair
        if val in s:
            print("Pair elements are",
                  arr[i], "and", int(val))

        # Driver Code


arr = [2, 11, 5, 1, 4, 7]
n = len(arr)
if checkPair(arr, n) == False:
    print("No pair found")


