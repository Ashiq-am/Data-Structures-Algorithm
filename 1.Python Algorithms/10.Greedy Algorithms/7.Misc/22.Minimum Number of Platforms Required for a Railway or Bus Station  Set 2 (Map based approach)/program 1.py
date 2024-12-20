# Python3 program to find minimum number
# of platforms required on a railway station
def findPlatform(arr, dep, n):
    # Inserting all the arr. and dep. times
    # in the array times
    times = []
    for i in range(n):
        times.append([dep[i], 'd'])
        times.append([arr[i], 'a'])

    # Sort the array
    times = sorted(times, key=lambda x: x[1])
    times = sorted(times, key=lambda x: x[0])

    result, plat_needed = 0, 0

    for i in range(2 * n):

        # If its 'a' then add 1 to plat_needed
        # else minus 1 from plat_needed.
        if times[i][1] == 'a':
            plat_needed += 1
            result = max(plat_needed, result)
        else:
            plat_needed -= 1

    return result


# Driver code
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print("Minimum Number of Platforms Required =",findPlatform(arr, dep, n))
