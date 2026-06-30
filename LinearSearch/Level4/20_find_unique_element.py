# You are given an array arr[] of integers where every element appears twice except for one element that appears only once. 
# Your task is to find and return the unique element.

#if every element appears more than twice except one.
def find_unique_element(arr):
    hash_table = dict()

    for element in arr:
            hash_table[element] = hash_table.get(element, 0) + 1

    for element in hash_table:
        if hash_table[element] == 1:
            return element
        
#if every element appears exactly twice except one.
def find_unique_element(arr):
    result = 0

    for element in arr:
        result = result ^ element

    return result
        
print(find_unique_element([2, 3, 5, 4, 5, 3, 4]))
print(find_unique_element([7, 1, 1]))
print(find_unique_element([9]))