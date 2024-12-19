# Python3 code for above approach

# Function to find Index
def find_extra_element_index(arrA, arrB):
    # Calculating extra element
    extra_element = sum(arrA) - sum(arrB)

    # returns index of extra element
    return arrA.index(extra_element)


# Driver Code
arrA = [2, 4, 6, 8, 10, 12, 13]
arrB = [2, 4, 6, 8, 10, 12]
print(find_extra_element_index(arrA, arrB))

# This code is contributed by Dravid
