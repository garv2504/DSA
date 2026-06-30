# You are given an array arr[] of integers. 
# Your task is to find the frequency of every distinct element in the array, i.e., determine how many times each element appears.

def element_frequency(arr):
    counter = dict()

    for element in arr:
            counter[element] = counter.get(element, 0) + 1

    return counter

print(element_frequency([1, 2, 2, 3, 1]))
print(element_frequency([5, 5, 5]))
print(element_frequency([4, 2, 7]))