# Python3 program for the above approach
from turtledemo.sorting_animate import partition


def quickSort(arr, low, high):
    if (low < high):
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
