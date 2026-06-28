# You are given an array arr[] of integers. 
# Your task is to find the second largest distinct element present in the array. 
# If a second largest distinct element does not exist, return -1.

def second_largest_distinct(arr):
    largest = -1
    second_largest = -1

    for element in arr:
        #element > largest > second_largest
        if largest < element:
            second_largest = largest
            largest = element
        #largest > element > second_largest
        elif second_largest < element and element < largest:
            second_largest = element

    return second_largest

print(second_largest_distinct([12, 35, 1, 10, 34, 1]))
print(second_largest_distinct([10, 10, 10]))
print(second_largest_distinct([5, 8]))