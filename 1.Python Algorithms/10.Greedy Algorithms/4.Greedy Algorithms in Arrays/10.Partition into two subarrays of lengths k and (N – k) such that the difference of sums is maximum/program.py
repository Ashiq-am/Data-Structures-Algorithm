# Python3 code to calculate max_difference
# between the sum of two subarrays of
# length k and N - k

# Function to calculate max_difference
def maxDifference(arr, N, k):
    S = 0
    S1 = 0
    max_difference = 0

    # Sum of the array
    for i in range(N):
        S += arr[i]

    # Sort the array in descending order
    arr.sort(reverse=True)
    M = max(k, N - k)
    for i in range(M):
        S1 += arr[i]

    # Calculating max_difference
    max_difference = S1 - (S - S1)
    return max_difference


# Driver Code
arr = [8, 4, 5, 2, 10]
N = len(arr)
k = 2
print(maxDifference(arr, N, k))
