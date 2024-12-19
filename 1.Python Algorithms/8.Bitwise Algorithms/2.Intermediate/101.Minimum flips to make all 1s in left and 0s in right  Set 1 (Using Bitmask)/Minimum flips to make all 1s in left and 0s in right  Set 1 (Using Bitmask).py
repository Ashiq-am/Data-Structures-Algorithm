# Python3 program to find minimum flips to make
# all 1s in left

# Function to count minimum number of flips
def findMiniFlip(nums):
    n = len(nums)
    s = ''

    for i in range(n):
        s += str(nums[i])

    # This is converting string s into integer
    # of base 2 (if s='100' then num=4)
    num = int(s, 2)

    # Initialize minXor with n that can be maximum
    # number of flips
    minXor = n;

    # Right shift 1 by(n-1) bits
    mask = (1 << (n - 1))
    while (n - 1 > 0):
        # Calculate bitwise XOR of num and mask
        temp = (num ^ mask)

        # Math.min(a, b) returns minimum of a and b
        # return minimum number of flips till that
        # digit
        minXor = min(minXor, countones(temp))
        n -= 1
        mask = (mask | (1 << n - 1))

    return minXor


# Function to count number of 1s
def countones(n):
    c = 0
    while (n > 0):
        n = n & (n - 1)
        c += 1

    return c


# Driver code
if __name__ == "__main__":
    nums = [1, 0, 1, 1, 0, 0, 0]
    n = findMiniFlip(nums)

    print(n)

# This code is contributed by chitranayal
