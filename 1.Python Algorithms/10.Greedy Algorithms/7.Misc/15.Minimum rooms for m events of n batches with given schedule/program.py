# Python3 program to find minimum
# number of rooms required

# Returns minimum number of
# rooms required to perform
# classes of n groups in m
# slots with given schedule.
def findMinRooms(slots, n, m):
    # Store count of classes
    # happening in every slot.
    counts = [0] * m
    for i in range(n):
        for j in range(m):
            if (slots[i][j] == '1'):
                counts[j] += 1

    # Number of rooms required is
    # equal to maximum classes
    # happening in a particular slot.
    return max(counts)


# Driver Code
n = 3
m = 7
slots = ["0101011", "0011001", "0110111"]
print(findMinRooms(slots, n, m))


