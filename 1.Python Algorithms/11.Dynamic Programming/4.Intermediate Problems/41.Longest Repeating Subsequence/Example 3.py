# Python 3 program to find the longest repeating
# subsequence Length

# This function mainly returns LRS(str, str,i,j,dp)
# with a condition that same characters at
# same index are not considered.
def lrs(s1, i, j, dp):
    # return if we have reached the
    # end of either string
    if i >= len(s1) or j >= len(s1):
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    # while dp[i][j] is not computed earlier
    if dp[i][j] == -1:

        # if characters at index m and n matches
        # and index is different
        # Index should not match
        if s1[i] == s1[j] and i != j:
            dp[i][j] = 1 + lrs(s1, i + 1, j + 1, dp)

        # else if characters at index m and n don't match
        else:
            dp[i][j] = max(lrs(s1, i, j + 1, dp),
                           lrs(s1, i + 1, j, dp))

    # return answer
    return dp[i][j]


# Driver Code
if __name__ == "__main__":
    s1 = "aabb"

    # Reversing the same string
    s2 = s1[::-1]
    dp = [[-1 for i in range(1000)] for j in range(1000)]
    print("LENGTH OF LONGEST REPEATING SUBSEQUENCE IS :",
          lrs(s1, 0, 0, dp))
