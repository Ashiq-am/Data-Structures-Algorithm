# Python 3 program to count number of occurrences of
# each element in the array in less than O(n) time

# A recursive function to count number of occurrences
# for each element in the array without traversing
# the whole array
def findFrequencyUtil(arr, low, high, freq):
    # If element at index low is equal to element
    # at index high in the array
    if (arr[low] == arr[high]):

        # increment the frequency of the element
        # by count of elements between high and low
        freq[arr[low]] += high - low + 1

    else:

        # Find mid and recurse for left
        # and right subarray
        mid = int((low + high) / 2)
        findFrequencyUtil(arr, low, mid, freq)
        findFrequencyUtil(arr, mid + 1, high, freq)

    # A wrapper over recursive function


# findFrequencyUtil(). It print number of
# occurrences of each element in the array.
def findFrequency(arr, n):
    # create a empty vector to store frequencies
    # and initialize it by 0. Size of vector is
    # maximum value (which is last value in sorted
    # array) plus 1.
    freq = [0 for i in range(n - 1 + 1)]

    # Fill the vector with frequency
    findFrequencyUtil(arr, 0, n - 1, freq)

    # Print the frequencies
    for i in range(0, arr[n - 1] + 1, 1):
        if (freq[i] != 0):
            print("Element", i, "occurs",
                  freq[i], "times")

        # Driver Code


if __name__ == '__main__':
    arr = [1, 1, 1, 2, 3, 3, 5,
           5, 8, 8, 8, 9, 9, 10]
    n = len(arr)
    findFrequency(arr, n)
