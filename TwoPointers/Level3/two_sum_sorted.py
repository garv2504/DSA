# You are given a sorted array arr[] of integers and an integer target. 
# Your task is to find two elements whose sum is equal to target and return their indices.

def two_sum(arr, target):
    i = 0
    
    #Brute force approach with O(n2) time complexity and O(1) space complexity
    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr):
            if arr[i] + arr[j] == target:
                return [i, j]
            j += 1
        i += 1

    return [-1, -1]

#Optimal approach with O(n) time complexity and O(n) space complexity
def two_sum(arr, target):
    i = 0
    n = len(arr)

    dictionary = dict()

    while i < n:
        if arr[i] in dictionary:
            return [dictionary.get(arr[i]), i]
        else:
            dictionary[target - arr[i]] = i

        i += 1

    return [-1, -1]

#Optimized approach with O(n) time complexity and O(1) space complexity
def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([1, 2, 4, 6, 10], 8)) 
print(two_sum([1, 3, 5, 7], 20))