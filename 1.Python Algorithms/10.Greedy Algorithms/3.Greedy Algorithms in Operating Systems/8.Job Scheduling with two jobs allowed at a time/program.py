# Python3 program to check if all
# jobs can be scheduled if two jobs
# are allowed at a time.

def checkJobs(startin, endin, n):
    # making a pair of starting and
    # ending time of job
    a = []
    for i in range(0, n):
        a.append([startin[i], endin[i]])

    # sorting according to starting
    # time of job
    a.sort()

    # starting first and second job
    # simultaneously
    tv1 = a[0][1]
    tv2 = a[1][1]

    for i in range(2, n):

        # Checking if starting time of next
        # new job is greater than ending time
        # of currently scheduled first job
        if (a[i][0] >= tv1):

            tv1 = tv2
            tv2 = a[i][1]

        # Checking if starting time of next
        # new job is greater than ending time
        # of ocurrently scheduled second job
        elif (a[i][0] >= tv2):
            tv2 = a[i][1]

        else:
            return 0

    return 1


# Driver Code
if __name__ == '__main__':
    startin = [1, 2, 4]  # starting time of jobs
    endin = [2, 3, 5]  # ending times of jobs
    n = 3
    print(checkJobs(startin, endin, n))
