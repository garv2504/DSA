# You are given an array arr[] of integers and an integer x. 
# Your task is to check whether x is present in the array. 
# If it is present, return the index of its first occurrence; otherwise, return -1.

def find_element(arr, x):
    for i in range(0, len(arr)):
        if x == arr[i]:
            return i
        
    return -1

print(find_element([1, 2, 3, 4], 3))
print(find_element([10, 8, 30, 4, 5], 5))
print(find_element([10, 8, 30], 6))