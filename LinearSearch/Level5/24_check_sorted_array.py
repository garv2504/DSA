#You are given an array arr[] of integers. 
# Your task is to check whether the array is sorted in non-decreasing (ascending) order. 
# If it is sorted, return true; otherwise, return false.

def check_sorted(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i+1]:
            return False
        i += 1
    return True

print(check_sorted([1, 2, 3, 4, 5]))
print(check_sorted([1, 2, 2, 4]))
print(check_sorted([3, 1, 2]))