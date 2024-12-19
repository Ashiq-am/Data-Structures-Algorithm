# Python3 Program to fid out
# minimum cost to process m tasks

# Function to find out the farthest
# position where one of the currently
# ongoing tasks will rehappen.
def find(arr, pos, m, isRunning):
    # Iterate form last to current
    # position and find where the
    # task will happen next.
    d = [0] * (m + 1)
    for i in range(m - 1, pos, -1):

        if isRunning[arr[i]]:
            d[arr[i]] = i

    # Find out maximum of all these positions
    # and it is the farthest position.
    maxipos = 0
    for ele in d:
        maxipos = max(ele, maxipos)

    return maxipos


# Function to find out minimum
# cost to process all the tasks
def mincost(n, m, arr):
    # freqarr[i][j] denotes the frequency
    # of type j task after position i
    # like in array 1, 2, 1, 3, 2, 1
    # frequency of type 1 task after
    # position 0 is 2. So, for this
    # array freqarr[0][1] = 2. Here,
    # i can range in between 0 to m-1 and
    # j can range in between 0 to m(though
    # there is not any type 0 task).
    freqarr = [[] for i in range(m)]

    # Fill up the freqarr vector from
    # last to first. After m-1 th position
    # frequency of all type of tasks will be
    # 0. Then at m-2 th position only frequency
    # of arr[m-1] type task will be increased
    # by 1. Again, in m-3 th position only
    # frequency of type arr[m-2] task will
    # be increased by 1 and so on.
    newvec = [0] * (m + 1)
    freqarr[m - 1] = newvec[:]
    for i in range(m - 2, -1, -1):
        nv = freqarr[i + 1][:]
        nv[arr[i + 1]] += 1
        freqarr[i] = nv[:]

    # isRunning[i] denotes whether type i
    # task is currently running in one
    # of the cores.
    # At the beginning no tasks are
    # running so all values are false.
    isRunning = [False] * (m + 1)

    # cost denotes total cost to assign tasks
    cost = 0

    # truecount denotes number of occupied cores
    truecount = 0

    # iterate through each task
    # and find the total cost.
    for i in range(0, m):

        # ele denotes type of task.
        ele = arr[i]

        # Case 1: if smae type of task is
        # currently running cost for this is 0.
        if isRunning[ele] == True:
            continue

        # Case 2: same type of task
        # is not currently running.
        else:

            # Subcase 1: if there is at least
            # one free core then assign this task
            # to that core at a cost of 1 unit.
            if truecount < n:
                cost += 1
                truecount += 1
                isRunning[ele] = True

            # Subcase 2: No core is free
            else:

                # here we will first find the minimum
                # frequency among all the ongoing tasks
                # in future.
                # If the minimum frequency is 0 then
                # there is at least one ongoing task
                # which will not occur again. Then we just
                # stop tha task.
                # If minimum frequency is >0 then, all the
                # tasks will occur at least once in future.
                # we have to find out which of these will
                # rehappen last among the all ongoing tasks.

                # set minimum frequency to a big number
                mini = 100000

                # set index of minimum frequency task to 0.
                miniind = 0

                # find the minimum frequency task
                # type(miniind) and frequency(mini).
                for j in range(1, m + 1):
                    if isRunning[j] and mini > freqarr[i][j]:
                        mini = freqarr[i][j]
                        miniind = j

                # If minimum frequency is zero then just stop
                # the task and start the present task in that
                # core. Cost for this is 1 unit.
                if mini == 0:
                    isRunning[miniind] = False
                    isRunning[ele] = True
                    cost += 1

                # If minimum frequency is nonzero then find
                # the farthest position where one of the
                # ongoing task will rehappen.
                # Stop that task and start present task
                # in that core.
                else:

                    # find out the farthest position
                    # using find function
                    farpos = find(arr, i, m, isRunning)
                    isRunning[arr[farpos]] = False
                    isRunning[ele] = True
                    cost += 1

    # return total cost
    return cost


# Driver Code
if __name__ == "__main__":
    # Test case 1
    n1, m1 = 3, 6
    arr1 = [1, 2, 1, 3, 4, 1]
    print(mincost(n1, m1, arr1))

    # Test case 2
    n2, m2 = 2, 6
    arr2 = [1, 2, 1, 3, 2, 1]
    print(mincost(n2, m2, arr2))

    # Test case 3
    n3, m3 = 3, 31
    arr3 = [7, 11, 17, 10, 7, 10, 2, 9,
            2, 18, 8, 10, 20, 10, 3, 20,
            17, 17, 17, 1, 15, 10, 8, 3,
            3, 18, 13, 2, 10, 10, 11]

    print(mincost(n3, m3, arr3))
