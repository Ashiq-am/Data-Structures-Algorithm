# A tabulation based solution in Python3

def getMinSteps(n):
    table = [0] * (n + 1)

    for i in range(n + 1):
        table[i] = n - i

    for i in range(n, 0, -1):

        if (not (i % 2)):
            table[i // 2] = min(table[i] + 1, table[i // 2])

        if (not (i % 3)):
            table[i // 3] = min(table[i] + 1, table[i // 3])

    return table[1]


# driver program
if __name__ == "__main__":
    n = 14
    print(getMinSteps(n))
