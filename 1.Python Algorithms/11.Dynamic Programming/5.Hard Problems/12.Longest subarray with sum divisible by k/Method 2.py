# function to find the longest subarray
#  with sum divisible by k
def longSubarrWthSumDivByK(arr, n, k):
    # unordered map 'um' implemented as
    # hash table
    um = {}

    # 'mod_arr[i]' stores (sum[0..i] % k)
    max = 0
    curr_sum = 0

    for i in range(0, n):
        curr_sum += arr[i]
        mod = ((curr_sum % k) + k) % k
        # if true then sum(0..i) is divisible by k
        if mod == 0:
            # update 'max'
            max = i + 1

        # if value 'mod_arr[i]' not present in 'um'
        # then store it in 'um' with index of its
        # first occurrence
        elif mod in um.keys():
            if max < (i - um[mod]):
                max = i - um[mod]

        else:
            um[mod] = i

    # required length of longest subarray with
    # sum divisible by 'k'
    return max


arr = [2, 7, 6, 1, 4, 5]
n = len(arr)
k = 3
print(longSubarrWthSumDivByK(arr, n, k))