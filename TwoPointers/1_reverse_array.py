# You are given an array arr[] of integers. 
# Your task is to reverse the order of the elements in the array using the two-pointer technique and return the modified array.

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr

print(reverse_array([1, 2, 3, 4, 5]))
print(reverse_array([10]))
print(reverse_array([7, 8]))