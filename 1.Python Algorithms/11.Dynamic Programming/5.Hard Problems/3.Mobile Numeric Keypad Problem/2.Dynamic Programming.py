# A Dynamic Programming based C program to count number of
# possible numbers of given length

# Return count of all possible numbers of length n
# in a given numeric keyboard
def getCount(keypad, n):
    if (keypad == None or n <= 0):
        return 0
    if (n == 1):
        return 10

    # left, up, right, down move from current location
    row = [0, 0, -1, 0, 1]
    col = [0, -1, 0, 1, 0]

    # taking n+1 for simplicity - count[i][j] will store
    # number count starting with digit i and length j
    # count[10][n+1]
    count = [[0] * (n + 1)] * 10
    i = 0
    j = 0
    k = 0
    move = 0
    ro = 0
    co = 0
    num = 0
    nextNum = 0
    totalCount = 0

    # count numbers starting with
    # digit i and of lengths 0 and 1
    for i in range(10):
        count[i][0] = 0
        count[i][1] = 1

    # Bottom up - Get number
    # count of length 2, 3, 4, ... , n
    for k in range(2, n + 1):
        for i in range(4):  # Loop on keypad row
            for j in range(3):  # Loop on keypad column

                # Process for 0 to 9 digits
                if (keypad[i][j] != '*' and keypad[i][j] != '#'):

                    # Here we are counting the numbers starting with
                    # digit keypad[i][j] and of length k keypad[i][j]
                    # will become 1st digit, and we need to look for
                    # (k-1) more digits
                    num = ord(keypad[i][j]) - 48
                    count[num][k] = 0

                    # move left, up, right, down from current location
                    # and if new location is valid, then get number
                    # count of length (k-1) from that new digit and
                    # add in count we found so far
                    for move in range(5):
                        ro = i + row[move]
                        co = j + col[move]
                        if (ro >= 0 and ro <= 3 and co >= 0 and co <= 2 and
                                keypad[ro][co] != '*' and keypad[ro][co] != '#'):
                            nextNum = ord(keypad[ro][co]) - 48
                            count[num][k] += count[nextNum][k - 1]

    # Get count of all possible numbers of length "n" starting
    # with digit 0, 1, 2, ..., 9
    totalCount = 0
    for i in range(10):
        totalCount += count[i][n]
    return totalCount


# Driver code
if __name__ == "__main__":
    keypad = [['1', '2', '3'],
              ['4', '5', '6'],
              ['7', '8', '9'],
              ['*', '0', '#']]

    print("Count for numbers of length", 1, ":", getCount(keypad, 1))
    print("Count for numbers of length", 2, ":", getCount(keypad, 2))
    print("Count for numbers of length", 3, ":", getCount(keypad, 3))
    print("Count for numbers of length", 4, ":", getCount(keypad, 4))
    print("Count for numbers of length", 5, ":", getCount(keypad, 5))