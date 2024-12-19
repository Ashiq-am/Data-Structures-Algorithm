# Python3 implementation to count
# number of ways to jump to reach end

# Function to count ways to jump to
# reach end for each array element
def countWaysToJump(arr, n):
    # count_jump[i] store number of ways
    # arr[i] can reach to the end
    count_jump = [0 for i in range(n)]

    # Last element does not require
    # to jump. Count ways to jump for
    # remaining elements
    for i in range(n - 2, -1, -1):

        # if the element can directly
        # jump to the end
        if (arr[i] >= n - i - 1):
            count_jump[i] += 1

        # Add the count of all the elements
        # that can reach to end and arr[i]
        # can reach to them
        j = i + 1
        while (j < n - 1 and j <= arr[i] + i):

            # if element can reach to end then
            # add its count to count_jump[i]
            if (count_jump[j] != -1):
                count_jump[i] += count_jump[j]
            j += 1

        # if arr[i] cannot reach to the end
        if (count_jump[i] == 0):
            count_jump[i] = -1

    # print count_jump for each
    # array element
    for i in range(n):
        print(count_jump[i], end=" ")


# Driver code
arr = [1, 3, 5, 8, 9, 1, 0, 7, 6, 8, 9]
n = len(arr)
countWaysToJump(arr, n)
