# You are given an array arr[] of integers. 
# Your task is to rearrange the array such that all even numbers appear before all odd numbers.

def separate_odd_even(arr):
    i = 0
    j = 0
    while j < len(arr):
        if arr[j] % 2 == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else:
            j += 1

    return arr

print(separate_odd_even([2, 9, 6, 7, 8, 4, 4, 3, 1, 9]))
print(separate_odd_even([1, 2, 3, 4, 5, 6]))
print(separate_odd_even([1, 3, 5]))
print(separate_odd_even([2, 4, 6]))