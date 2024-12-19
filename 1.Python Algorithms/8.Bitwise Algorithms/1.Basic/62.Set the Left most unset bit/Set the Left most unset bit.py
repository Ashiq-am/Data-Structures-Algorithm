# Python program to set the leftmost unset bit

# Set left most unset bit
def setleftmostunsetbit(n):
    # if number contain all
    # 1 then return n
    if not (n & (n + 1)):
        return n

    # Find position of leftmost unset bit
    pos, temp, count = 0, n, 0

    while temp:
        # if temp L.S.B is zero
        # then unset bit pos is
        # change
        if not (temp & 1):
            pos = count

        count += 1;
        temp >>= 1

    # return OR of number and
    # unset bit pos
    return (n | (1 << (pos)))


# Driver Function
n = 10
print(setleftmostunsetbit(n))

# This code is contributed by Ansu Kumari
