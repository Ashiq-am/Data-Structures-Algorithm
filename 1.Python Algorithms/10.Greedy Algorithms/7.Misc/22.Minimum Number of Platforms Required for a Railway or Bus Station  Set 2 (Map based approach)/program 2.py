# Python3 program to find minimum number
# of platforms required on a railway station
def minPlatform(arrival, departure, n):
    # As time range from 0 to 2359 in
    # 24 hour clock, we declare an array
    # for values from 0 to 2360
    platform = [0] * 2631
    requiredPlatform = 1

    for i in range(n):
        # Increment the platforms for arrival
        platform[arrival[i]] += 1

        # Once train departs we decrease the
        # platform count
        platform[departure[i] + 1] -= 1

    # We are running loop till 2361 because
    # maximum time value in a day can be 23:60
    for i in range(1, 2631):
        # Taking cumulative sum of
        # platform give us required
        # number of platform fro every minute
        platform[i] = platform[i] + platform[i - 1]
        requiredPlatform = max(requiredPlatform,
                               platform[i])

    return requiredPlatform


# Driver code
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print("Minimum Number of Platforms Required = ",minPlatform(arr, dep, n))
