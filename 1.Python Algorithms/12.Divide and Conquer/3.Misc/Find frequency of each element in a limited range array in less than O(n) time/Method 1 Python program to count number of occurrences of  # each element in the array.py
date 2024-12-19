# Python program to count number of occurrences of
# each element in the array #include <iostream>

# It prints number of
# occurrences of each element in the array.
def findFrequency(arr, n):
    # HashMap to store frequencies
    mp = {}

    # traverse the array
    for i in range(n):

        # update the frequency
        if arr[i] not in mp:
            mp[arr[i]] = 0
        mp[arr[i]] += 1

    # traverse the hashmap
    for i in mp:
        print("Element", i, "occurs", mp[i], "times")

    # Driver function


arr = [1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10]
n = len(arr)

findFrequency(arr, n)

# This code is contributed by shubhamsingh10
