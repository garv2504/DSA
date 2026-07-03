# You are given a string str. 
# Your task is to reverse the order of its characters and return the reversed string.

def reverse_string(string):
    list_string = list(string)

    start = 0
    end = len(list_string) - 1

    while start < end:
        list_string[start], list_string[end] = list_string[end], list_string[start]
        start += 1
        end -= 1

    return "".join(list_string)

print(reverse_string("hello"))
print(reverse_string("a"))
print(reverse_string("OpenAI"))