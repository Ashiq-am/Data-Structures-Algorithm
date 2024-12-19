# Python 3 implementation of above approach

INT_SIZE = 32


def Right_most_setbit(num):
    pos = 1

    # counting the position of first set bit
    for i in range(INT_SIZE):
        if not (num & (1 << i)):
            pos += 1
        else:
            break

    return pos


if __name__ == "__main__":
    num = 18
    pos = Right_most_setbit(num)
    print(pos)

# This code is contributed by ANKITRAI1
