# Python 3 program to find missing point
# of a parallelogram

# Main method
if __name__ == "__main__":
    # coordinates of A

    ax, ay = 5, 0

    # coordinates of B

    bx, by = 1, 1

    # coordinates of C

    cx, cy = 2, 5

    print(ax + cx - bx, ",", ay + cy - by)
