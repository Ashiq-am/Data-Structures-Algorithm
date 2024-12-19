# Python program to delete an element
# from an unsorted array

# Declaring array and key to delete
arr = [10, 50, 30, 40, 20]
key = 30

print("Array before deletion:")
print(arr)

# deletes key if found in the array
# otherwise shows error not in list
arr.remove(key)
print("Array after deletion")
print(arr)


