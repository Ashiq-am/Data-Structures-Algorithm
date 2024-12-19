# Python3 Program to count pairs in
# an array with some common digit

# Returns true if the pair is
# valid, otherwise false
def checkValidPair(num1, num2):
    # converting integers to strings
    s1 = str(num1)
    s2 = str(num2)

    # Iterate over the strings and check if
    # a character in first string is also
    # present in second string, return true
    for i in range(len(s1)):
        for j in range(len(s2)):
            if (s1[i] == s2[j]):
                return True

    # No common digit found
    return False


# Returns the number of valid pairs
def countPairs(arr, n):
    numberOfPairs = 0

    # Iterate over all possible pairs
    for i in range(n):
        for j in range(i + 1, n):
            if (checkValidPair(arr[i], arr[j])):
                numberOfPairs += 1

    return numberOfPairs


# Driver Code
if __name__ == "__main__":
    arr = [10, 12, 24]
    n = len(arr)
    print(countPairs(arr, n))
