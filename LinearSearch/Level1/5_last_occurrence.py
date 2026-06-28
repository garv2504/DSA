# You are given an array arr[] of integers and an integer x. 
# Your task is to find the last occurrence of x in the array. 
# If x is present, return its index; otherwise, return -1.

def check_last_occurrence(arr, x):
    pos = -1

    for i in range(0, len(arr)):
        if x == arr[i]:
            pos = i

    return pos

print(check_last_occurrence([1, 2, 3, 2, 4], 2))
print(check_last_occurrence([5, 5, 5, 5], 5))
print(check_last_occurrence([10, 20, 30], 40))