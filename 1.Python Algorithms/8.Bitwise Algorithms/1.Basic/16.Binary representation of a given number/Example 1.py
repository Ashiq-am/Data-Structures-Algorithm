def bin(n):
    i = 1 << 31
    while (i > 0):

        if ((n & i) != 0):

            print("1", end="")

        else:
            print("0", end="")

        i = i // 2


bin(7)
print()
bin(4)

# This code is contributed by divyeshrabadiya07.
