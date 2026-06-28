#You are given an array arr[] of integers. 
# Your task is to find the second smallest distinct element present in the array. 
# If a second smallest distinct element does not exist, return -1.

def second_smallest_element(arr):
    smallest = float('inf')
    second_smallest = float('inf')

    for element in arr:
        #element > second_smallest > smallest
        if smallest > element:
            second_smallest = smallest
            smallest = element
        # second_smallest > element > smallest
        elif second_smallest > element and element > smallest:
            second_smallest = element

    if second_smallest == float('inf'):
        return -1

    return second_smallest
 
print(second_smallest_element([12, 35, 1, 10, 34, 1]))
print(second_smallest_element([10, 10, 10]))
print(second_smallest_element([5, 8]))