# Python3 implementation to find maximum
# length subsequence with difference between
# adjacent elements as either 0 or 1
from collections import defaultdict


# Function to find maximum length subsequence with
# difference between adjacent elements as either 0 or 1
def maxLenSub(arr, n):
    # hash table to map the array element with the
    # length of the longest subsequence of which it is a
    # part of and is the last element of that subsequence
    um = defaultdict(lambda: 0)

    # to store the maximum length subsequence
    maxLen = 0

    # traverse the array elements
    for i in range(0, n):

        # initialize current length
        # for element arr[i] as 0
        length = 0

        # if 'arr[i]-1' is in 'um' and its length of
        # subsequence is greater than 'len'
        if (arr[i] - 1) in um and length < um[arr[i] - 1]:
            length = um[arr[i] - 1]

        # if 'arr[i]' is in 'um' and its length of
        # subsequence is greater than 'len'
        if arr[i] in um and length < um[arr[i]]:
            length = um[arr[i]]

        # if 'arr[i]+1' is in 'um' and its length of
        # subsequence is greater than 'len'
        if (arr[i] + 1) in um and length < um[arr[i] + 1]:
            length = um[arr[i] + 1]

        # update arr[i] subsequence length in 'um'
        um[arr[i]] = length + 1

        # update maximum length
        if maxLen < um[arr[i]]:
            maxLen = um[arr[i]]

    # required maximum length subsequence
    return maxLen


# Driver program to test above
if __name__ == "__main__":
    arr = [2, 5, 6, 3, 7, 6, 5, 8]
    n = len(arr)
    print("Maximum length subsequence =", maxLenSub(arr, n))
