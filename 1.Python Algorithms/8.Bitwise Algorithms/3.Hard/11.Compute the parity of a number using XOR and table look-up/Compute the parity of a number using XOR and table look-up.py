# Python3 program to illustrate Compute the
# parity of a number using XOR

# Generating the look-up table while
# pre-processing
def P2(n, table):
    table.extend([n, n ^ 1, n ^ 1, n])


def P4(n, table):
    return (P2(n, table), P2(n ^ 1, table),
            P2(n ^ 1, table), P2(n, table))


def P6(n, table):
    return (P4(n, table), P4(n ^ 1, table),
            P4(n ^ 1, table), P4(n, table))


def LOOK_UP(table):
    return (P6(0, table), P6(1, table),
            P6(1, table), P6(0, table))


# LOOK_UP is the macro expansion to
# generate the table
table = [0] * 256
LOOK_UP(table)


# Function to find the parity
def Parity(num):
    # Number is considered to be
    # of 32 bits
    max = 16

    # Dividing the number o 8-bit
    # chunks while performing X-OR
    while (max >= 8):
        num = num ^ (num >> max)
        max = max // 2

    # Masking the number with 0xff (11111111)
    # to produce valid 8-bit result
    return table[num & 0xff]


# Driver code
if __name__ == "__main__":
    num = 1742346774

    # Result is 1 for odd parity,
    # 0 for even parity
    result = Parity(num)
    print("Odd Parity") if result else print("Even Parity")

# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
