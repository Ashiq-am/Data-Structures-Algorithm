# Function to extract ‘k’ bits from a given
# position in a number

def extractKBits(num, k, p):
    # convert number into binary first
    binary = bin(num)

    # remove first two characters
    binary = binary[2:]

    end = len(binary) - p
    start = end - k + 1

    # extract k bit sub-string
    kBitSubStr = binary[start: end + 1]

    # convert extracted sub-string into decimal again
    print(int(kBitSubStr, 2))


# Driver program
if __name__ == "__main__":
    num = 171
    k = 5
    p = 2
    extractKBits(num, k, p)


