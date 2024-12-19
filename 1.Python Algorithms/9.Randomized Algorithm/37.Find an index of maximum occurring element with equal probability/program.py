# Python3 program to return index of most occurring element
# of the array randomly with equal probability
import random


# Function to return index of most occurring element
# of the array randomly with equal probability
def findRandomIndexOfMax(arr, n):
    # freq store frequency of each element in the array
    mp = dict()
    for i in range(n):
        if (arr[i] in mp):
            mp[arr[i]] = mp[arr[i]] + 1

        else:
            mp[arr[i]] = 1

    max_element = -323567
    # stores max occurring element

    # stores count of max occurring element
    max_so_far = -323567

    # traverse each pair in map and find maximum
    # occurring element and its frequency
    for p in mp:

        if (mp[p] > max_so_far):
            max_so_far = mp[p]
            max_element = p

    # generate a random number between [1, max_so_far]
    r = int(((random.randrange(1, max_so_far, 2) % max_so_far) + 1))

    i = 0
    count = 0

    # traverse array again and return index of rth
    # occurrence of max element
    while (i < n):

        if (arr[i] == max_element):
            count = count + 1

        # Print index of rth occurrence of max element
        if (count == r):
            print("Element with maximum frequency present at index ", i)
            break
        i = i + 1


# Driver code

# input array
arr = [-1, 4, 9, 7, 7, 2, 7, 3, 0, 9, 6, 5, 7, 8, 9]
n = len(arr)
findRandomIndexOfMax(arr, n)
