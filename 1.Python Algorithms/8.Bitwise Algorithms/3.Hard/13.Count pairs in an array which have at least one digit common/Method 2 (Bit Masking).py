# Python3 Program to count pairs in an array
# with some common digit

# This function calculates the mask frequencies
# for every present in the array
def calculateMaskFrequencies(arr, n, freq):
    # Iterate over the array
    for i in range(n):

        num = arr[i]

        # Creating an empty mask
        mask = 0

        # Extracting every digit of the number
        # and updating corresponding bit in the
        # mask
        while (num > 0):
            mask = mask | (1 << (num % 10))
            num //= 10

        # Update the frequency array
        freq[mask] = freq.get(mask, 0) + 1


# Function return the number of valid pairs
def countPairs(arr, n):
    # Store the mask frequencies
    freq = dict()

    calculateMaskFrequencies(arr, n, freq)

    numberOfPairs = 0

    # Considering every possible pair of masks
    # and calculate pairs according to their
    # frequencies
    for i in range(1024):

        x = 0

        if i in freq.keys():
            x = freq[i]

        numberOfPairs += (x * (x - 1)) // 2

        for j in range(i + 1, 1024):

            y = 0

            if j in freq.keys():
                y = freq[j]

            # if it contains a common digit
            if (i & j):
                numberOfPairs += (x * y)

    return numberOfPairs


# Driver Code
arr = [10, 12, 24]
n = len(arr)
print(countPairs(arr, n))


