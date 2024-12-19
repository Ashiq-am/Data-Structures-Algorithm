from collections import Counter


# Python3 program to find the element
# that occur only once

# function which find number
def singleNumber(nums):
    # storing the frequencies using Counter
    freq = Counter(nums)

    # traversing the Counter dictionary
    for i in freq:

        # check if any value is 1
        if (freq[i] == 1):
            return i


# driver function.
a = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
print("The element with single occurrence is ",
      int(singleNumber(a)))
# This code is contributed by vikkycirus
