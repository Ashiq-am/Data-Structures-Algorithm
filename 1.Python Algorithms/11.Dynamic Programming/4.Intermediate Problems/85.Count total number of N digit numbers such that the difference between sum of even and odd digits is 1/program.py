# A memoization based recursive program to count numbers
# with difference between odd and even digit sums as 1

# Memoization based recursive function to count numbers
# with even and odd digit sum difference as 1. This function
# considers leading zero as a digit
def countRec(digits, esum, osum, isOdd, n):
    # Base Case
    if digits == n:
        return (esum - osum == 1)

    # If current subproblem is already computed
    if lookup[digits][esum][osum][isOdd] != -1:
        return lookup[digits][esum][osum][isOdd]

    # Initialize result
    ans = 0

    # If the current digit is odd,
    # then add it to odd sum and recur
    if isOdd:
        for i in range(10):
            ans += countRec(digits + 1, esum,
                            osum + i, False, n)

    # Add to even sum and recur
    else:
        for i in range(10):
            ans += countRec(digits + 1, esum + i,
                            osum, True, n)

    # Store current result in lookup table
    # and return the same
    lookup[digits][esum][osum][isOdd] = ans
    return ans


# This is mainly a wrapper over countRec. It
# explicitly handles leading digit and calls
# countRec() for remaining digits.
def finalCount(n):
    global lookup

    # Initialize number digits considered so far
    digits = 0

    # Initialize all entries of lookup table
    lookup = [[[[-1, -1] for i in range(500)]
               for j in range(500)]
              for k in range(50)]

    # Initialize final answer
    ans = 0

    # Initialize even and odd sums
    esum = 0
    osum = 0

    # Explicitly handle first digit and call
    # recursive function countRec for remaining digits.
    # Note that the first digit is considered as even digit
    for i in range(1, 10):
        ans += countRec(digits + 1, esum + i,
                        osum, True, n)

    return ans


# Driver Code
if __name__ == "__main__":
    # A lookup table used for memoization.
    lookup = []
    n = 3
    print("Count of %d digit numbers is %d" % (n, finalCount(n)))
