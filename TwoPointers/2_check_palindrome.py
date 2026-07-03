#You are given an array arr[] of integers. 
# Your task is to check whether the array is a palindrome. 
# An array is a palindrome if it reads the same from left to right and from right to left.

def check_palindrome(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        if arr[start] != arr[end]:
            return False
        start += 1
        end -= 1

    return True

print(check_palindrome([1, 2, 3, 2, 1]))
print(check_palindrome([1, 2, 2, 1]))
print(check_palindrome([1, 2, 3]))