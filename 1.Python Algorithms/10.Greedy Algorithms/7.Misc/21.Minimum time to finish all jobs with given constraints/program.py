# Python program to find minimum
# time to finish all jobs with
# given number of assignees

# Utility function to get maximum
# element in job[0..n-1]
def getMax(arr, n):
    result = arr[0]
    for i in range(1, n):
        if arr[i] > result:
            result = arr[i]
    return result


# Returns true if it is possible
# to finish jobs[] within given
# time 'time'
def isPossible(time, K, job, n):
    # cnt is count of current
    # assignees required for jobs
    cnt = 1

    # time assigned to current assignee
    curr_time = 0

    i = 0
    while i < n:

        # If time assigned to current
        # assignee exceeds max, increment
        # count of assignees.
        if curr_time + job[i] > time:
            curr_time = 0
            cnt += 1
        else:

            # Else add time of job to current
            # time and move to next job.
            curr_time += job[i]
            i += 1

    # Returns true if count is smaller than k
    return cnt <= K


# Returns minimum time required
# to finish given array of jobs
# k --> number of assignees
# T --> Time required by every assignee to finish 1 unit
# m --> Number of jobs
def findMinTime(K, T, job, n):
    # Set start and end for binary search
    # end provides an upper limit on time
    end = 0
    start = 0
    for i in range(n):
        end += job[i]

    ans = end  # Initialize answer

    # Find the job that takes maximum time
    job_max = getMax(job, n)

    # Do binary search for minimum feasible time
    while start <= end:
        mid = int((start + end) / 2)

        # If it is possible to finish jobs in mid time
        if mid >= job_max and isPossible(mid, K, job, n):
            ans = min(ans, mid)  # Update answer
            end = mid - 1
        else:
            start = mid + 1

    return ans * T


# Driver program
if __name__ == '__main__':
    job = [10, 7, 8, 12, 6, 8]
    n = len(job)
    k = 4
    T = 5
    print(findMinTime(k, T, job, n))
