# You are given an array arr[] of integers. 
# Your task is to check whether the array contains any duplicate elements. 
# If at least one element appears more than once, return true; otherwise, return false.

#Method-1
def check_duplicate_elements(arr) -> bool:
    unique_lst = []
    for element in arr:
        #Lookup takes O(n2) time for list as it does linear search which takes O(n)
        if element in unique_lst:
            return True
        unique_lst.append(element)
        
    return False

def check_duplicate_elements(arr) -> bool:
    unique_array = set()
    for element in arr:
        #Lookup takes O(n) time for set as it does searching via hashing which takes O(1) time
        if element in unique_array:
            return True
        unique_array.add(element)
        
    return False

print(check_duplicate_elements([1, 2, 3, 4]))
print(check_duplicate_elements([1, 2, 3, 2]))
print(check_duplicate_elements([5, 5, 5]))
