# You are given a string str. 
# Your task is to check whether the string is a palindrome. 
# A string is a palindrome if it reads the same from left to right and from right to left.

def check_string_palindrome(string):
    start = 0
    end = len(string) - 1


    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True

print(check_string_palindrome("madam"))
print(check_string_palindrome("racecar"))
print(check_string_palindrome("hello"))