# You are given an array arr[] of integers. 
# Your task is to move all the 0s to the end of the array while maintaining the relative order of the non-zero elements.

def move_zeroes_to_end(arr):
    i = 0
    j = 0
    while j < len(arr):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else:
            j += 1

    return arr


print(move_zeroes_to_end([0, 1, 0, 3, 12]))
print(move_zeroes_to_end([1, 2, 3]))
print(move_zeroes_to_end([0, 0, 5]))