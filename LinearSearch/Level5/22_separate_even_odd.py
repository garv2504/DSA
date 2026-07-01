# You are given an array arr[] of integers. 
# Your task is to rearrange the array such that all even numbers appear before all odd numbers. 
# The relative order of elements does not matter unless specified.

#Brute Force Approach
#T.C. --> O(n)
#S.C. --> O(n)

def separate_even_odd(arr):
    result = []

    for element in arr:
        if element % 2 == 0:
            result.append(element)

    for element in arr:
        if element % 2 != 0:
            result.append(element)

    return result

print(separate_even_odd([1, 2, 3, 4, 5, 6]))
print(separate_even_odd([1, 3, 5]))
print(separate_even_odd([2, 4, 6]))

#Optimal Approach
#T.C. --> O(n)
#S.C --> O(1)

def separate_even_odd(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] % 2 == 0:
            left += 1
        elif arr[right] % 2 != 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

print(separate_even_odd([1, 2, 3, 4, 5, 6]))
print(separate_even_odd([1, 3, 5]))
print(separate_even_odd([2, 4, 6]))