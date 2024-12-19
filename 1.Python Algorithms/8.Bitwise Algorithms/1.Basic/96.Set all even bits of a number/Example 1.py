# Simple Python program to set all even
# bits of a number

# Sets even bits of n and returns
# modified number.
def evenbitsetnumber(n):
    # Generate 101010...10 number and
    # store in res.
    count = 0
    res = 0
    temp = n
    while (temp > 0):

        # if bit is even then generate
        # number and or with res
        if (count % 2 == 1):
            res |= (1 << count)

        count += 1
        temp >>= 1

    # return OR number
    return (n | res)


n = 10
print(evenbitsetnumber(n))

# This code is contributed
# by Smitha Dinesh Semwal
