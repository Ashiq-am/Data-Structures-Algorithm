# Python3 program for above approach

# Utility function for calculating
# Minimum element to delete
def utility_fun_for_del(Str, i, j):
    if (i >= j):
        return 0

    # Condition to compare characters
    if (Str[i] == Str[j]):
        # Recursive function call
        return utility_fun_for_del(Str, i + 1,
                                   j - 1)

    # Return value, increamenting by 1
    # return minimum Element between two values
    return (1 + min(utility_fun_for_del(Str, i + 1, j),
                    utility_fun_for_del(Str, i, j - 1)))


# Function to calculate the minimum
# Element required to delete for
# Making string pelindrom
def min_ele_del(Str):
    # Utility function call
    return utility_fun_for_del(Str, 0,
                               len(Str) - 1)


# Driver code
Str = "abefbac"

print("Minimum element of deletions =",
      min_ele_del(Str))


