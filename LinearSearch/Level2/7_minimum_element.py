# You are given an array arr[] of integers. 
# Your task is to find the minimum (smallest) element present in the array and return it.

def find_minimum_element(arr):
    smallest = float('inf')

    for element in arr:
        if smallest > element:
            smallest = element

    return smallest

print(find_minimum_element([1, 8, 7, 56, 90]))
print(find_minimum_element([5]))
print(find_minimum_element([10, 20, 15, 8]))