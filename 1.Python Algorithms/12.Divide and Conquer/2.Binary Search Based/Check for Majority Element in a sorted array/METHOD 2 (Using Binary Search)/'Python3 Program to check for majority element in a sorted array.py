'''Python3 Program to check for majority element in a sorted array'''


# This function returns true if the x is present more than n / 2
# times in arr[] of size n */
def isMajority(arr, n, x):
    # Find the index of first occurrence of x in arr[] */
    i = _binarySearch(arr, 0, n - 1, x)

    # If element is not present at all, return false*/
    if i == -1:
        return False

    # check if the element is present more than n / 2 times */
    if ((i + n // 2) <= (n - 1)) and arr[i + n // 2] == x:
        return True
    else:
        return False


# If x is present in arr[low...high] then returns the index of
# first occurrence of x, otherwise returns -1 */
def _binarySearch(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2  # low + (high - low)//2;

        ''' Check if arr[mid] is the first occurrence of x. 
            arr[mid] is first occurrence if x is one of the following 
            is true: 
            (i) mid == 0 and arr[mid] == x 
            (ii) arr[mid-1] < x and arr[mid] == x'''

        if (mid == 0 or x > arr[mid - 1]) and (arr[mid] == x):
            return mid
        elif x > arr[mid]:
            return _binarySearch(arr, (mid + 1), high, x)
        else:
            return _binarySearch(arr, low, (mid - 1), x)
    return -1


# Driver program to check above functions */
arr = [1, 2, 3, 3, 3, 3, 10]
n = len(arr)
x = 3
if (isMajority(arr, n, x)):
    print("% d appears more than % d times in arr[]"
          % (x, n // 2))
else:
    print("% d does not appear more than % d times in arr[]"% (x, n // 2))
