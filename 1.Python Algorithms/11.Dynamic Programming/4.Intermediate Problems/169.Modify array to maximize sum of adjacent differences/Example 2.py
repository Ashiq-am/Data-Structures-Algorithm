def maximumDifferenceSum(arr, n):
    prev_change, prev_nochange = 0, 0





    for i in range(1, n):
        change = max(prev_change, arr[i - 1] - 1 + prev_nochange)
        nochange = max(prev_nochange + abs(arr[i] - arr[i - 1]), arr[i] - 1 + prev_change)

        prev_change = change
        prev_nochange = nochange


    return max(prev_change, prev_nochange)

if __name__ == '__main__':
    arr = [3, 2, 1, 4, 5]
    N = len(arr)
    print(maximumDifferenceSum(arr, N))
