# You are given an array arr[] of integers and an integer x. 
# Your task is to check whether x exists in the array. 
# If it exists, return the index of its first occurrence; otherwise, return -1.

def check_element_exists(arr, x):
    for i in range(0, len(arr)):
        if x == arr[i]:
            return i
        
    return -1

print(check_element_exists([1, 2, 3, 4], 3))
print(check_element_exists([10, 8, 30, 4, 5], 5))
print(check_element_exists([10, 8, 30], 6))