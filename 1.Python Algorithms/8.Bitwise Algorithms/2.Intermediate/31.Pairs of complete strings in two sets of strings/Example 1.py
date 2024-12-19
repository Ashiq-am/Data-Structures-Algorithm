# Python3 implementation for find pairs of complete
# strings.

# Returns count of complete pairs from set[0..n-1]
# and set2[0..m-1]
def countCompletePairs(set1, set2, n, m):
    result = 0

    # Consider all pairs of both strings
    for i in range(n):
        for j in range(m):
            # Create a concatenation of current pair
            concat = set1[i] + set2[j]

            # Compute frequencies of all characters
            # in the concatenated String.
            frequency = [0 for i in range(26)]

            for k in range(len(concat)):
                frequency[ord(concat[k]) - ord('a')] += 1

            # If frequency of any character is not
            # greater than 0, then this pair is not
            # complete.

            k = 0
            while (k < 26):
                if (frequency[k] < 1):
                    break
                k += 1

            if (k == 26):
                result += 1

    return result


# Driver code
set1 = ["abcdefgh", "geeksforgeeks", "lmnopqrst", "abc"]
set2 = ["ijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "defghijklmnopqrstuvwxyz"]
n = len(set1)
m = len(set2)
print(countCompletePairs(set1, set2, n, m))

# This code is contributed by shinjanpatra
