# Python3 program to find maximum number
# of customers that can be satisfied
v = []


# print maximum number of satisfied
# customers and their indexes
def solve(n, d, a, b, arr):
    first, second = 0, 1

    # Creating an vector of pair of
    # total demand and customer number
    for i in range(n):
        m = arr[i][0]
        t = arr[i][1]
        v.append([a * m + b * t, i + 1])

    # Sorting the customers according
    # to their total demand
    v.sort()

    ans = []

    # Taking the first k customers that
    # can be satisfied by total amount d
    for i in range(n):
        if v[i][first] <= d:
            ans.append(v[i][second])
            d -= v[i][first]

    print(len(ans))
    for i in range(len(ans)):
        print(ans[i], end=" ")


# Driver Code
if __name__ == '__main__':
    # Initializing variables
    n = 5
    d = 5
    a = 1
    b = 1
    arr = [[2, 0], [3, 2],
           [4, 4], [10, 0],
           [0, 1]]

    solve(n, d, a, b, arr)
