# A naive recursive Python3 program to
# find maximum tasks.

# Returns maximum amount of task
# that can be done till day n
def maxTasks(high, low, n):
    # If n is less than equal to 0,
    # then no solution exists
    if (n <= 0):
        return 0

    # Determines which task to choose on day n,
    # then returns the maximum till that day
    return max(high[n - 1] + maxTasks(high, low, (n - 2)),
               low[n - 1] + maxTasks(high, low, (n - 1)));


# Driver Code
if __name__ == "__main__":
    n = 5;
    high = [3, 6, 8, 7, 6]
    low = [1, 5, 4, 5, 3]
    print(maxTasks(high, low, n));

# This code is contributed by Ryuga
