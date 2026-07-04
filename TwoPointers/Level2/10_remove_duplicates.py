# You are given a sorted array arr[] of integers. 
# Your task is to remove all duplicate elements so that each distinct element appears only once, and return the modified array.

def remove_duplicate_elements(arr):
    if len(arr) == 1:
        return arr
        
    i = 0
    j = 1
    
    while j < len(arr):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
            j += 1
        else:
            j += 1
            
    return arr[0:i+1]
    
print(remove_duplicate_elements([1, 1, 2, 2, 3, 4, 4]))
print(remove_duplicate_elements([5, 5, 5]))
print(remove_duplicate_elements([1, 2, 3]))