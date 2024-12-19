# Python3 program to count swaps required to
# balance string
def swapCount(s):
    chars = s

    # Stores total number of left and
    # right brackets encountered
    countLeft = 0
    countRight = 0

    # Swap stores the number of swaps
    # required imbalance maintains the
    # number of imbalance pair
    swap = 0
    imbalance = 0;

    for i in range(len(chars)):
        if chars[i] == '[':

            # Increment count of left bracket
            countLeft += 1

            if imbalance > 0:
                # Swaps count is last swap
                # count + total number
                # imbalanced brackets
                swap += imbalance

                # Imbalance decremented by 1
                # as it solved only one
                # imbalance of left and right
                imbalance -= 1

        elif chars[i] == ']':

            # Increment count of right bracket
            countRight += 1

            # Imbalance is reset to current
            # difference between left and
            # right brackets
            imbalance = (countRight - countLeft)

    return swap


# Driver code
s = "[]][][";
print(swapCount(s))

s = "[[][]]";
print(swapCount(s))
