# Function to count set bits in an integer
# in Python

def countSetBits(num):
    # convert given number into binary
    # output will be like bin(11)=0b1101
    binary = bin(num)

    # now separate out all 1's from binary string
    # we need to skip starting two characters
    # of binary string i.e; 0b
    setBits = [ones for ones in binary[2:] if ones == '1']

    print(len(setBits))


# Driver program
if __name__ == "__main__":
    num = 11
    countSetBits(num)
