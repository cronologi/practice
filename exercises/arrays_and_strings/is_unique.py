# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?


def is_unique(string):
    temp_dict = {}
    for char in string:
        if char in temp_dict:
            return False
        temp_dict[char] = None
    return True

state = is_unique("Davor")
print(state)
    
