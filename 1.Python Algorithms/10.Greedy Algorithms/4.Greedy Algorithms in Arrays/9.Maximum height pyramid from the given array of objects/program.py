# Python 3 program to find
# maximum height pyramid from
# the given object width.

# Returns maximum number
# of pyramidcal levels n
# boxes of given widths.
def maxLevel(boxes, n):
    # Sort objects in increasing
    # order of widths
    boxes.sort()

    ans = 1  # Initialize result

    # Total width of previous
    # level and total number of
    # objects in previous level
    prev_width = boxes[0]
    prev_count = 1

    # Number of object in
    # current level.
    curr_count = 0

    # Width of current level.
    curr_width = 0
    for i in range(1, n):

        # Picking the object. So
        # increase current width
        # and number of object.
        curr_width += boxes[i]
        curr_count += 1

        # If current width and
        # number of object are
        # greater than previous.
        if (curr_width > prev_width and
                curr_count > prev_count):
            # Update previous width,
            # number of object on
            # previous level.
            prev_width = curr_width
            prev_count = curr_count

            # Reset width of current
            # level, number of object
            # on current level.
            curr_count = 0
            curr_width = 0

            # Increment number of level.
            ans += 1
    return ans


# Driver Code
if __name__ == "__main__":
    boxes = [10, 20, 30, 50, 60, 70]
    n = len(boxes)
    print(maxLevel(boxes, n))

