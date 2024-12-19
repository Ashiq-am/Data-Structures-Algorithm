# Python3 program for the above approach


def countFlips(a, b):
    # initially flips is equal to 0
    flips = 0

    # & each bits of a && b with 1
    # and store them if t1 and t2
    # if t1 != t2 then we will flip that bit
    while(a > 0 or b > 0):
        t1 = (a & 1)
        t2 = (b & 1)

        if(t1 != t2):
            flips += 1

        # right shifting a and b
        a >>= 1
        b >>= 1


    return flips

# Driver code
if __name__ == "__main__":
    a = 10
    b = 20

    # Function call
    print(countFlips(a, b))

# This code is contributed by shivanisinghss2110
