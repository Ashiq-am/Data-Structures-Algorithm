# The function returns true if there exist three elements in AP
# Assumption: set[0..n-1] is sorted.
# The code strictly implements the algorithm provided in the reference.
def arithematicThree(set_, n):
    # One by fix every element as middle element
    for j in range(n):

        # Initialize i and k for the current j
        i, k = j - 1, j + 1

        # Find if there exist i and k that form AP
        # with j as middle element
        while i > -1 and k < n:
            if set_[i] + set_[k] == 2 * set_[j]:
                return True

            elif set_[i] + set_[k] < 2 * set_[j]:
                i -= 1

            else:
                k += 1
    return False
# This code is contributed by Kushagra Bansal
