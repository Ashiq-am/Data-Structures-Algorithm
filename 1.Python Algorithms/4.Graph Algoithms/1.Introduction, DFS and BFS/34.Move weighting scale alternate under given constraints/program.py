# Python3 program to print weights for
# alternating the weighting scale

# DFS method to traverse among states
# of weighting scales
def dfs(residue, curStep, wt, arr, N, steps):
    # If we reach to more than required
    # steps, return true
    if (curStep >= steps):
        return True

    # Try all possible weights and choose
    # one which returns 1 afterwards
    for i in range(N):

        # Try this weight only if it is greater
        # than current residueand not same as
        # previous chosen weight
        if (arr[i] > residue and
                arr[i] != wt[curStep - 1]):

            # assign this weight to array and
            # recur for next state
            wt[curStep] = arr[i]
            if (dfs(arr[i] - residue, curStep + 1,
                    wt, arr, N, steps)):
                return True

    # if any weight is not possible,
    # return false
    return False


# method prints weights for alternating scale
# and if not possible prints 'not possible'
def printWeightsOnScale(arr, N, steps):
    wt = [0] * (steps)

    # call dfs with current residue as 0
    # and current steps as 0
    if (dfs(0, 0, wt, arr, N, steps)):
        for i in range(steps):
            print(wt[i], end=" ")
    else:
        print("Not possible")


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 5, 6]
    N = len(arr)

    steps = 10
    printWeightsOnScale(arr, N, steps)


