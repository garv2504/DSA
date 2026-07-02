# You are given an array arr[] of integers. 
# Your task is to find the length of the longest continuous increasing sequence in the array.

def longest_increasing_continuous_subsequence(arr):
    count = 1
    flag = 0

    if not arr:
        return 0

    for i in range(0, len(arr)-1):
        if arr[i] < arr[i+1]:
            count += 1
        elif flag < count:
            flag = count
            count = 1
        else:
            count = 1

    if flag < count:
        flag = count
    return flag

print(longest_increasing_continuous_subsequence([1, 2, 3, 2, 3, 4, 5]))
print(longest_increasing_continuous_subsequence([5, 4, 3, 2]))
print(longest_increasing_continuous_subsequence([1, 2, 3, 1, 2]))
