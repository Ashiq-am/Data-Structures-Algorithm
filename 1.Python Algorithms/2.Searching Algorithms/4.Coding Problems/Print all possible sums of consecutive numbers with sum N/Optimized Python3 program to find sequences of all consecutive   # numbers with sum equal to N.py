# Optimized Python3 program to find sequences of all consecutive
# numbers with sum equal to N
def findConsecutive(N):
    start = 1
    end = 1
    sum = 1

    while start <= N / 2:

        if sum < N:
            end += 1
            sum += end

        if sum > N:
            sum -= start
            start += 1

        if sum == N:

            for i in range(start, end + 1):
                print(i, end=' ')
            print()
            sum -= start
            start += 1


# Driver code
N = 125
findConsecutive(N)
