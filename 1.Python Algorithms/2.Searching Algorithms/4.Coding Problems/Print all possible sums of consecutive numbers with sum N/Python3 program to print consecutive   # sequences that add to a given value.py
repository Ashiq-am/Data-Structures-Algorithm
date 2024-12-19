# Python3 program to print consecutive
# sequences that add to a given value
def findConsecutive(N):
    # Note that we don't ever have to
    # Sum numbers > ceil(N/2)
    start = 1
    end = (N + 1) // 2

    # Repeat the loop from bottom to half
    while (start < end):

        # Check if there exist any sequence
        # from bottom to half which adds up to N
        Sum = 0
        for i in range(start, end + 1):

            Sum = Sum + i

            # If Sum = N, this means consecutive
            # sequence exists
            if (Sum == N):

                # found consecutive numbers! prthem
                for j in range(start, i + 1):
                    print(j, end=" ")

                print()
                break

            # if Sum increases N then it can not
            # exist in the consecutive sequence
            # starting from bottom
            if (Sum > N):
                break

        Sum = 0
        start += 1


# Driver code
N = 125
findConsecutive(N)
