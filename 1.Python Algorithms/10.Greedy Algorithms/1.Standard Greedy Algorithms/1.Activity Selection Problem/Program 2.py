''' Python program for activity selection problem
when input activities may not be sorted.'''


def MaxActivities(arr, n):
    selected = []

    # Sort jobs according to finish time
    Activity.sort(key=lambda x: x[1])

    # The first activity always gets selected
    i = 0
    selected.append(arr[i])

    for j in range(1, n):
        '''If this activity has start time greater than or
               equal to the finish time of previously selected
               activity, then select it'''


        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j


    return selected


# Driver code
Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
n = len(Activity)
selected = MaxActivities(Activity, n)
print("Following activities are selected :")
print(selected)
