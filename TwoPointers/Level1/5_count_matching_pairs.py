# You are given a string str. 
# Your task is to count how many matching pairs of characters are present when comparing characters from the beginning and the end of the string moving towards the center.

def count_matching_pairs(string):
    count = 0
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return count
        count += 1
        start += 1
        end -= 1

    return count

print(count_matching_pairs("racecar"))
print(count_matching_pairs("abba"))
print(count_matching_pairs("hello")) 