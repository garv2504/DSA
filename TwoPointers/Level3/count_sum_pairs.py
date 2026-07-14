# You are given an array arr[] of integers and an integer target.
# Your task is to count the total number of pairs whose sum is equal to target.

def count_pair(arr, target):
    frequency = {}
    count = 0

    for element in arr:
        complement = target - element

        if complement in frequency:
            count += frequency[complement]

        frequency[element] = frequency.get(element, 0) + 1

    return count

print(count_pair([1, 5, 7, 1], 6))
print(count_pair([1, 2, 3, 4, 5], 7))
print(count_pair([2, 4, 6], 20))
print(count_pair([3, 3, 3], 6))