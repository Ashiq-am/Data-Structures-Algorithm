# Python3 program to find the element
# that occur only once

# function which find number
def singleNumber(nums):
    # applying the formula.
    return (3 * sum(set(nums)) - sum(nums)) / 2


# driver function.
a = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
print("The element with single occurrence is ",
      int(singleNumber(a)))
