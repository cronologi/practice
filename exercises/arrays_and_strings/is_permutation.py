# Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    dict1, dict2 = {}, {}
    for i in range(0, len(string1)):
        dict1[string1[i]] = None
        dict2[string2[i]] = None
    return dict1.keys() == dict2.keys()

state = is_permutation("ABC", "BCA")
print(state)