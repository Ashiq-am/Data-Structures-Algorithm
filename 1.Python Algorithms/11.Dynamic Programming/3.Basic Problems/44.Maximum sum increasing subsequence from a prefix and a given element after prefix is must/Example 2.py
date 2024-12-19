# Python3 program for the above approach

# Function to find the sum
def pre_compute(a, n, index, k):
    # Base case
    if (index >= k):
        return -1

    # Initialize the dp table
    dp = [0 for i in range(index)]

    # Initialize the dp array with
    # corresponding array index value
    for i in range(index):
        dp[i] = a[i]

    maxi = -float('inf')

    for i in range(index):

        # Only include values
        # which are less than a[k]
        if (a[i] >= a[k]):
            continue

        for j in range(i):

            # Check if a[i] is
            # greater than a[j]
            if (a[i] > a[j]):
                dp[i] = dp[j] + a[i]

            # Update maxi
            maxi = max(maxi, dp[i])

    # Incase all the elements in
    # the array upto ith index
    # are greater or equal to a[k]
    if (maxi == -float('inf')):
        return a[k]

    return maxi + a[k]


# Driver code
a = [1, 101, 2, 3, 100, 4, 5]
n = len(a)
index = 4
k = 6

# Function call
print(pre_compute(a, n, index, k))
