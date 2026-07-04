# You are given an array arr[] containing only 0s and 1s. 
# Your task is to sort the array in non-decreasing order, so that all 0s appear before all 1s.

def sort_0s_and_1s(arr):
    i = 0
    j = 0

    while j < len(arr):
        if arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else:
            j += 1

    return arr

print(sort_0s_and_1s([0, 1, 1, 0, 1, 0]))
print(sort_0s_and_1s([1, 1, 1]))
print(sort_0s_and_1s([0, 0, 0]))