# You are given an array arr[] of integers. 
# Your task is to count how many negative numbers are present in the array and return the count.

def average_of_array(arr):
    n = len(arr)
    sum = 0

    for element in arr:
        sum = sum + element

    return (sum/n)

print(average_of_array([1, 2, 3, 4]))
print(average_of_array([5]))
print(average_of_array([10, 20, 30]))