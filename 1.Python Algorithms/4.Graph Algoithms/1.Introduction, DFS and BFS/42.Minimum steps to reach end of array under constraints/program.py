# Python 3 program to find minimum jumps to reach end# of array

# Method returns minimum step to reach end of array
def getMinStepToReachEnd(arr, N):
    # visit boolean array checks whether current index
    # is previously visited
    visit = [False for i in range(N)]

    # distance array stores distance of current
    # index from starting index
    distance = [0 for i in range(N)]

    # digit vector stores indices where a
    # particular number resides
    digit = [[0 for i in range(N)] for j in range(10)]

    # storing indices of each number in digit vector
    for i in range(1, N):
        digit[arr[i]].append(i)

    # for starting index distance will be zero
    distance[0] = 0
    visit[0] = True

    # Creating a queue and inserting index 0.
    q = []
    q.append(0)

    # loop untill queue in not empty
    while (len(q) > 0):

        # Get an item from queue, q.
        idx = q[0]
        q.remove(q[0])

        # If we reached to last index break from loop
        if (idx == N - 1):
            break

        # Find value of dequeued index
        d = arr[idx]

        # looping for all indices with value as d.
        for i in range(len(digit[d])):
            nextidx = digit[d][i]
            if (visit[nextidx] == False):
                visit[nextidx] = True
                q.append(nextidx)

                # update the distance of this nextidx
                distance[nextidx] = distance[idx] + 1

        # clear all indices for digit d, because all
        # of them are processed

        # checking condition for previous index
        if (idx - 1 >= 0 and visit[idx - 1] == False):
            visit[idx - 1] = True
            q.append(idx - 1)
            distance[idx - 1] = distance[idx] + 1

        # checking condition for next index
        if (idx + 1 < N and visit[idx + 1] == False):
            visit[idx + 1] = True
            q.append(idx + 1)
            distance[idx + 1] = distance[idx] + 1

    # N-1th position has the final result
    return distance[N - 1]


# driver code to test above methods
if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 6, 0, 1, 2, 3, 4, 5, 7]
    N = len(arr)
    print(getMinStepToReachEnd(arr, N))
