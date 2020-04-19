# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE:
# pale, ple -> True
# pales, pale -> True
# pale, bale -> True
# pale, bake -> False


def is_one_edit_away(string_one: str, string_two: str) -> bool:
    char_array_one = list(string_one)
    char_array_two = list(string_two)

    if len(char_array_one) == len(char_array_two):
        return one_edit_replace(char_array_one, char_array_two)
    elif len(char_array_one) + 1 == len(char_array_two):
        return one_edit_insert_or_delete(char_array_one, char_array_two)
    elif len(char_array_one) - 1 == len(char_array_two):
        return one_edit_insert_or_delete(char_array_two, char_array_one)

    return False


def one_edit_insert_or_delete(char_array_smaller: list, char_array_longer: list) -> bool:
    index_smaller = 0
    index_longer = 0

    while index_smaller < len(char_array_smaller) and index_longer < len(char_array_longer):
        if char_array_smaller[index_smaller] != char_array_longer[index_longer]:
            if index_smaller != index_longer:
                return False
            index_smaller += 1
        else:
            index_smaller += 1
            index_longer += 1

    return True


def one_edit_replace(char_array_one: list, char_array_two: list) -> bool:
    difference_found = False

    for idx, val in enumerate(char_array_one):
        if char_array_one[idx] != char_array_two[idx]:
            if difference_found:
                return False
        difference_found = True

    return True


print(is_one_edit_away("pales", "pale"))
