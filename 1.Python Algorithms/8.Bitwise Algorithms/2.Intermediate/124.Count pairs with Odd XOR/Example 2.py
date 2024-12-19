# Python 3 program to count
# pairs in array whose XOR is odd

# A function will
# return number of pair
# whose XOR is odd
def countXorPair(arr, n):
    # To store count of
    # odd and even numbers
    odd = 0
    even = 0

    for i in range(n):

        # Increase even if number is
        # even otherwise increase odd
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    # Return number of pairs
    return odd * even


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3]
    n = len(arr)
    print(countXorPair(arr, n))

# This code is contributed
# by ChitraNayal
