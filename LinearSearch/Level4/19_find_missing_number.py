# You are given an array arr[] containing n - 1 distinct integers from the range 1 to n. 
# Exactly one number is missing. 
# Your task is to find and return the missing number.

def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = (n*(n+1))//2
    sum = 0

    for element in arr:
        sum = sum + element
    
    return total_sum - sum

print(find_missing_number([1, 2, 4, 5]))
print(find_missing_number([2, 3, 1, 5]))
print(find_missing_number([1]))