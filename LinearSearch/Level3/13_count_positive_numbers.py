# You are given an array arr[] of integers. 
# Your task is to count how many positive numbers are present in the array and return the count.

def count_positive_numbers(arr):
    count = 0

    for element in arr:
        if element > 0:
            count = count + 1

    return count

print(count_positive_numbers([1, -2, 3, 0, 5]))
print(count_positive_numbers([-1, -2, -3]))
print(count_positive_numbers([2, 4, 6]))