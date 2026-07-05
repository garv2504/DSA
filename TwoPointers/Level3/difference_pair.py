#You are given a sorted array arr[] of integers and an integer diff. 
# Your task is to find a pair of elements whose absolute difference is equal to diff.

def difference_pair(arr, diff):
    left = 0
    right = 1

    while right < len(arr):
        current = arr[right] - arr[left]
        
        if left == right:
            right += 1
        elif current == diff:
            return [left, right]
        elif current < diff:
            right += 1
        else:
            left += 1

    return [-1, -1]

print(difference_pair([1, 3, 5, 8, 10], 2))
print(difference_pair([2, 4, 6, 8], 5))
print(difference_pair([1, 2, 3, 4, 5], 4))