#You are given an array arr[] of integers. 
# Your task is to move all negative numbers to the beginning of the array while maintaining the relative order of the remaining elements.

#Method1 --> If relative order is required to maintain
def move_negative(arr):
    i = 0
    j = 0
    n = len(arr)

    while j < n:
        if arr[j] < 0:
            temp = arr[j]
            for k in range(j, i, -1):
                arr[k] = arr[k-1]
            arr[i] = temp
            i += 1
            j += 1
        else:
            j += 1

    return arr

print(move_negative([1, -2, 3, -4, 5, -6]))
print(move_negative([-1, -2, -3]))
print(move_negative([2, 4, 6]))

#Method2 --> If relative order is not required to maintain
def move_negative_to_left(arr):
    i = 0
    j = 0

    while j < len(arr):
        if arr[j] != 0:
            j += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    
    return arr

print(move_negative([1, -2, 3, -4, 5, -6]))
print(move_negative([-1, -2, -3]))
print(move_negative([2, 4, 6]))