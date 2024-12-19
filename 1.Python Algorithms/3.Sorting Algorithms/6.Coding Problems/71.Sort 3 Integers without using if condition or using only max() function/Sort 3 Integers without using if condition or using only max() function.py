# Python3 program to print three numbers
# in sorted order using max function

def printSorted(a, b, c):
    # Find maximum element
    get_max = max(a, max(b, c))

    # Find minimum element
    get_min = -max(-a, max(-b, -c))

    get_mid = (a + b + c) - (get_max + get_min)

    print(get_min, " ", get_mid, " ", get_max)


# Driver Code
a, b, c = 4, 1, 9
printSorted(a, b, c)
