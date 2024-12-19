# Function to Count total set bits in all numbers
# from 1 to n

# user defined function
def countSetBit(num):
    # convert decimal value into binary and
    # count all 1's in it
    binary = bin(num)

    return len([ch for ch in binary if ch == '1'])


# function which count set bits in each number
def countSetBitAll(input):
    # map count function on each number
    print(sum(map(countSetBit, input)))


# Driver program
if __name__ == "__main__":
    n = 8
    input = []
    for i in range(1, n + 1):
        input.append(i)
    countSetBitAll(input)
