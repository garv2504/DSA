# You are given an array arr[] of integers and an integer x. 
# Your task is to count how many times x appears in the array and return that count.

def check_number_occurrence(arr, x):
    count = 0

    for element in arr:
        if x == element:
            count += 1

    return count

print(check_number_occurrence([1, 2, 3, 2, 4, 2], 2))
print(check_number_occurrence([5, 5, 5, 5], 5))
print(check_number_occurrence([10, 20, 30], 40))