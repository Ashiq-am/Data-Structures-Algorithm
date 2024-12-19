def changeToZero(a):
    a[a[1]] = a[not a[1]]
    return a


# Driver code
if __name__ == '__main__':
    a = [1, 0]
    a = changeToZero(a)

    print(" arr[0] = " + str(a[0]))
    print(" arr[1] = " + str(a[1]))

# This code is contributed by Yash_R
