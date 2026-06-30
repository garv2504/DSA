# You are given an array arr[] of integers. 
# Your task is to find all distinct duplicate elements present in the array. 
# If no duplicate elements exist, return an empty array.

def find_duplicate_elements(arr):
    unique_set = set()
    duplicate_set = set()
    for element in arr:
        if element in unique_set:
            duplicate_set.add(element)
        else:
            unique_set.add(element)

    return list(duplicate_set)

print(find_duplicate_elements([1, 2, 3, 2, 4, 1]))
print(find_duplicate_elements([5, 5, 5]))
print(find_duplicate_elements([1, 2, 3, 4]))