# You are given an array arr[] of integers and an integer x. 
# Your task is to find the first occurrence of x in the array. 
# If x is present, return its index; otherwise, return -1.

def check_first_occurrence(arr, x):
    for i in range(0, len(arr)):
        if x == arr[i]:
            return i
        
    return -1

print(check_first_occurrence([1, 2, 3, 2, 4], 2))
print(check_first_occurrence([5, 5, 5, 5], 5))
print(check_first_occurrence([10, 20, 30], 40))