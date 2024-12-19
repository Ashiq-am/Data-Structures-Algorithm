# A O(n) solution that uses
# table fact[] to calculate
# the Permutation Coefficient

# Returns value of Permutation
# Coefficient P(n, k)
def permutationCoeff(n, k):


f = 1

for i in range(k):  # P(n,k)=n*(n-1)*(n-2)*....(n-k-1)
    f *= (n - i)

return f  # This code is contributed by Suyash Saxena

# Driver Code
n = 10
k = 2
print("Value of P(", n, ", ", k, ") is ",permutationCoeff(n, k))
