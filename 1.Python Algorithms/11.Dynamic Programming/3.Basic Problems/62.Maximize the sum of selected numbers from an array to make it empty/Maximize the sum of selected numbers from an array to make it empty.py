# Python3 program to Maximize the sum of selected
# numbers by deleting three consecutive numbers.

# function to maximize the sum of
# selected numbers
def maximizeSum(a, n):
    # maximum in the sequence
    maximum = max(a)

    # stores the occurrences of the numbers
    ans = dict.fromkeys(range(0, n + 1), 0)

    # marks the occurrence of every
    # number in the sequence
    for i in range(n):
        ans[a[i]] += 1

    # ans to store the result
    result = 0
    i = maximum

    # Using the above mentioned approach
    while i > 0:

        # if occurence is greater than 0
        if ans[i] > 0:
            # add it to ans
            result += i

            # decrease i-1th element by 1
            ans[i - 1] -= 1

            # decrease ith element by 1
            ans[i] -= 1
        else:
            # decrease i
            i -= 1

    return result


# Driver code
if __name__ == "__main__":
    a = [1, 2, 3]
    n = len(a)
    print(maximizeSum(a, n))
