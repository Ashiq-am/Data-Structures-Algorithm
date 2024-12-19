# A Dynamic Programming based Python program
# to find maximum number of A's
# that can be printed using four keys

# this function returns the optimal
# length string for N keystrokes
def findoptimal(N):
    # The optimal string length is
    # N when N is smaller than 7
    if (N <= 6):
        return N

    # An array to store result of
    # subproblems
    screen = [0] * N

    # Initializing the optimal lengths
    # array for uptil 6 input
    # strokes.

    for n in range(1, 7):
        screen[n - 1] = n

    # Solve all subproblems in bottom manner
    for n in range(7, N + 1):

        # Initialize length of optimal
        # string for n keystrokes
        screen[n - 1] = 0

        # For any keystroke n, we need to
        # loop from n-3 keystrokes
        # back to 1 keystroke to find a breakpoint
        # 'b' after which we
        # will have ctrl-a, ctrl-c and then only
        # ctrl-v all the way.
        for b in range(n - 3, 0, -1):

            # if the breakpoint is at b'th keystroke then
            # the optimal string would have length
            # (n-b-1)*screen[b-1];
            curr = (n - b - 1) * screen[b - 1]
            if (curr > screen[n - 1]):
                screen[n - 1] = curr

    return screen[N - 1]


# Driver program
if __name__ == "__main__":

    # for the rest of the array we
    # will rely on the previous
    # entries to compute new ones
    for N in range(1, 21):
        print("Maximum Number of A's with ", N, " keystrokes is ",
              findoptimal(N))