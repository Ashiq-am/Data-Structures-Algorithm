# Python program for Find the two non-repeating elements in
# an array of repeating elements/ Unique Numbers 2

# This function prints the two non-repeating elements in an
# array of repeating elements
def get2NonRepeatingNos(arr, n):
    # Create a Set to store the numbers
    s = set()
    for i in range(n):

        # Iterate through the array and check if each
        # element is present or not in the set. If the
        # element is present, remove it from the array
        # otherwise add it to the set

        if (arr[i] in s):
            s.remove(arr[i])
        else:
            s.add(arr[i])
    print("The 2 non repeating numbers are :", end=" ")
    for it in s:
        print(it, end=" ")
    print()


# Driver code
arr = [2, 3, 7, 9, 11, 2, 3, 11]
n = len(arr)
get2NonRepeatingNos(arr, n)

# This code is contributed by shinjanpatra
