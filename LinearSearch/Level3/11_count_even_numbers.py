# You are given an array arr[] of integers. 
# Your task is to count how many even numbers are present in the array and return the count.

def count_even_numbers(arr):
    count = 0

    for element in arr:
        #Check if number is even
        if element % 2 == 0:
            count = count + 1
    
    return count

print(count_even_numbers([1, 2, 3, 4, 5, 6]))
print(count_even_numbers([2, 4, 6, 8]))
print(count_even_numbers([1, 3, 5]))