# You are given an array arr[] of integers. 
# Your task is to count how many odd numbers are present in the array and return the count.

def count_odd_numbers(arr):
    count = 0

    for element in arr:
        #Check if element is odd
        if element%2 != 0:
            count = count + 1

    return count

print(count_odd_numbers([1, 2, 3, 4, 5, 6]))
print(count_odd_numbers([1, 3, 5, 7]))
print(count_odd_numbers([2, 4, 6]))