# Python3 program to check if any
# valid sequence is divisible by M

def isPossible(n, index, Sum, M, arr, dp):
    global MAX
    # Base case
    if index == n:
        # check if sum is divisible by M
        if (Sum % M) == 0:
            return True
        return False

    # check if the current state
    # is already computed
    if dp[index][Sum] != -1:
        return dp[index][Sum]

    # 1.Try placing '+'
    placeAdd = isPossible(n, index + 1,
                          Sum + arr[index], M, arr, dp)

    # 2. Try placing '-'
    placeMinus = isPossible(n, index + 1,
                            Sum - arr[index], M, arr, dp)

    # calculate value of res for recursive case
    res = placeAdd or placeMinus

    # store the value for res for current
    # states and return for parent call
    dp[index][Sum] = res
    return res


MAX = 1000
arr = [1, 2, 3, 4, 6]
n = len(arr)
M = 4
dp = [[-1] * MAX for i in range(n + 1)]
res = isPossible(n, 0, 0, M, arr, dp)

if res:
    print(True)
else:
    print(False)
