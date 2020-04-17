# Given a string, wrtie a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is same forwards
# and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE:
# Input     Tact Coa
# Output    True (permutations: "taco cat", "atco cta", etc.)


def is_palindrome_permutation(text: str) -> bool:
    hashtable = {}
    char_array = list(text)
    length = 0

    for c in char_array:
        if c != " ":
            c = c.lower()
            hashtable[c] = hashtable.get(c, 0) + 1
            length += 1

    is_char_array_length_even = length % 2 == 0

    if is_char_array_length_even:
        return all(v % 2 == 0 for v in hashtable.values())
    else:
        odd_char_found = False
        for v in hashtable.values():
            if v % 2 != 0 and odd_char_found == False:
                odd_char_found = True
            elif v % 2 != 0 and odd_char_found == True:
                return False
        return True


result = is_palindrome_permutation("Tact Coa")
print(result)
