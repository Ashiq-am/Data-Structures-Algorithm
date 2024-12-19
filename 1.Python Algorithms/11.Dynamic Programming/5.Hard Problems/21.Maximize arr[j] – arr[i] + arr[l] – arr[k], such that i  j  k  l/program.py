# A Python3 Program to find maximum value of
# arr[l] - arr[k] + arr[j] - arr[i] and i < j < k < l,
# given that the array has atleast 4 elements

# A Dynamic Programming based function to find
# maximum value of arr[l] - arr[k] + arr[j] - arr[i]
# is maximum and i < j < k < l
def findMaxValue(arr, n):
    # If the array has less than 4 elements
    if n < 4:
        print("The array should have atlest 4 elements")
        return MIN

    # We create 4 DP tables
    table1, table2 = [MIN] * (n + 1), [MIN] * n
    table3, table4 = [MIN] * (n - 1), [MIN] * (n - 2)

    # table1[] stores the maximum value of arr[l]
    for i in range(n - 1, -1, -1):
        table1[i] = max(table1[i + 1], arr[i])

    # table2[] stores the maximum
    # value of arr[l] - arr[k]
    for i in range(n - 2, -1, -1):
        table2[i] = max(table2[i + 1],
                        table1[i + 1] - arr[i])

    # table3[] stores the maximum value of
    # arr[l] - arr[k] + arr[j]
    for i in range(n - 3, -1, -1):
        table3[i] = max(table3[i + 1],
                        table2[i + 1] + arr[i])

    # table4[] stores the maximum value of
    # arr[l] - arr[k] + arr[j] - arr[i]
    for i in range(n - 4, -1, -1):
        table4[i] = max(table4[i + 1],
                        table3[i + 1] - arr[i])

    # maximum value would be present in table4[0]
    return table4[0]


# Driver Code
if __name__ == "__main__":
    arr = [4, 8, 9, 2, 20]
    n = len(arr)

    # To represent minus infinite
    MIN = -100000000

    print(findMaxValue(arr, n))