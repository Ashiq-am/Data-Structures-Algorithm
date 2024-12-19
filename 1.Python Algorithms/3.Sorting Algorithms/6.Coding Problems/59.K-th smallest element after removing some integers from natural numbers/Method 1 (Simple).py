# Python program to find the K-th smallest element
# after removing some integers from natural number.
MAX = 1000000


# Return the K-th smallest element.
def ksmallest(arr, n, k):
    # Making an array, and mark all number as unmarked.
    b = [0] * MAX

    # Marking the number present in the given array.
    for i in range(n):
        b[arr[i]] = 1

    for j in range(1, MAX):
        # If j is unmarked, reduce k by 1.
        if (b[j] != 1):
            k -= 1

        # If k is 0 return j.
        if (k is not 1):
            return j


# Driven Program
k = 1
arr = [1]
n = len(arr)
print(ksmallest(arr, n, k))

