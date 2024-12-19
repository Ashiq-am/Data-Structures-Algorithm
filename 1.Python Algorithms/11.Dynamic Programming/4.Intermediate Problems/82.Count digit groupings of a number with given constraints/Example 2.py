# Python3 program to count the number of
# ways to group digits of a number
# such that sum of digits in every
# subgroup is less than or equal
# to its immediate right subgroup.

# Maximum length of
# input number string
MAX = 40

# A memoization table to store
# results of subproblems length
# of string is 40 and maximum
# sum will be 9 * 40 = 360.
dp = [[-1 for i in range(9 * MAX + 1)]
      for i in range(MAX)]


# Function to find the count
# of splits with given condition
def countGroups(position, previous_sum,
                length, num):
    # Terminating Condition
    if (position == length):
        return 1

    # If already evaluated for
    # a given sub problem then
    # return the value
    if (dp[position][previous_sum] != -1):
        return dp[position][previous_sum]

    # countGroups for current
    # sub-group is 0
    dp[position][previous_sum] = 0

    res = 0

    # sum of digits
    sum = 0

    # Traverse all digits from
    # current position to rest
    # of the length of string
    for i in range(position, length):
        sum += (ord(num[i]) - ord('0'))

        # If forward_sum is greater
        # than the previous sum,
        # then call the method again
        if (sum >= previous_sum):
            # Note : We pass current
            # sum as previous sum
            res += countGroups(i + 1, sum,
                               length, num)

    dp[position][previous_sum] = res

    # total number of subgroups
    # till the current position
    return res


# Driver Code
num = "1119"
len = len(num)

print(countGroups(0, 0, len, num))
