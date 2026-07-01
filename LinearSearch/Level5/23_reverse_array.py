# You are given an array arr[] of integers. 
# Your task is to reverse the order of the elements in the array and return the modified array.

#Brute Force - With extra storage

def reverse_array(arr):
    reversed_array = []
    n = len(arr) - 1

    while n >= 0:
        reversed_array.append(arr[n])
        n -= 1

    return reversed_array

print(reverse_array([1, 2, 3, 4, 5]))
print(reverse_array([10]))
print(reverse_array([7, 8]))


#Optimal Approach --> In place

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

print(reverse_array([1, 2, 3, 4, 5]))
print(reverse_array([10]))
print(reverse_array([7, 8]))