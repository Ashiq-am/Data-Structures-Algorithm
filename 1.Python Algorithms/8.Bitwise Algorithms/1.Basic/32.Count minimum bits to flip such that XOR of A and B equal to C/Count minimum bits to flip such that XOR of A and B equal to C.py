# Python code to find minimum bits to be flip
def totalFlips(A, B, C, N):
    count = 0
    for i in range(N):

        # If both A[i] and B[i] are equal
        if A[i] == B[i] and C[i] == '1':
            count = count + 1

        # if A[i] and B[i] are unequal
        elif A[i] != B[i] and C[i] == '0':
            count = count + 1
    return count


# Driver Code
# N represent total count of Bits
N = 5
a = "10100"
b = "00010"
c = "10011"
print(totalFlips(a, b, c, N))
