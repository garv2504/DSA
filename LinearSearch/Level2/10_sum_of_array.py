#You are given an array arr[] of integers. 
# Your task is to find the sum of all elements present in the array and return the result.

def sum_of_array(arr):
    sum = 0
    for element in arr:
        sum = sum + element
    
    return sum

print(sum_of_array([1, 2, 3, 4]))
print(sum_of_array([5]))
print(sum_of_array([10, 20, 30]))