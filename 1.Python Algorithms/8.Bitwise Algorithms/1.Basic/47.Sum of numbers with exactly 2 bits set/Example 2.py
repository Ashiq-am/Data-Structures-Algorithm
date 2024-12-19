# Python3 program to find sum of
# numbers upto n whose 2 bits are set

# To calculate sum of numbers
def findSum(n):
    sum = 0

    # Find numbers whose 2
    # bits are set
    i = 1
    while ((1 << i) < n):
        for j in range(0, i):
            num = (1 << i) + (1 << j)

            # If number is greater than n
            # we don't include this in sum
            if (num <= n):
                sum += num

        i += 1

    # Return sum of numbers
    return sum


# Driver Code
n = 10
print(findSum(n))

# This code is contributed
# by Smitha
