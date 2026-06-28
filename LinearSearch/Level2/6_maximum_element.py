# You are given an array arr[] of integers. 
# Your task is to find the maximum (largest) element present in the array and return it.

def find_maximum_element(arr):
    largest = -1

    for element in arr:
        if largest < element:
            largest = element

    return largest

print(find_maximum_element([1, 8, 7, 56, 90]))
print(find_maximum_element([5]))
print(find_maximum_element([10, 20, 15, 8]))