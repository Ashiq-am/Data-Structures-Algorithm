# Program to find minimum total
# offerings required.

# Returns minimum offerings required
def offeringNumber(n, templeHeight):
    sum = 0  # Initialize result

    # Go through all templs one by one
    for i in range(n):

        # Go to left while height
        # keeps increasing
        left = 0
        right = 0
        for j in range(i - 1, -1, -1):
            if (templeHeight[j] < templeHeight[j + 1]):
                left += 1
            else:
                break

        # Go to right while height
        # keeps increasing
        for j in range(i + 1, n):
            if (templeHeight[j] < templeHeight[j - 1]):
                right += 1
            else:
                break

        # This temple should offer maximum
        # of two values to follow the rule.
        sum += max(right, left) + 1
    return sum


# Driver Code
arr1 = [1, 2, 2]
print(offeringNumber(3, arr1))
arr2 = [1, 4, 3, 6, 2, 1]
print(offeringNumber(6, arr2))
