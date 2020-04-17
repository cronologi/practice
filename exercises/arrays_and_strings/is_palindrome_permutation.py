# Given a string, wrtie a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is same forwards
# and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE:
# Input     Tact Coa
# Output    True (permutations: "taco cat", "atco cta", etc.)


def is_palindrome_permutation(text: str) -> bool:
    hashtable = {}
    char_array = list(text)

    for c in char_array:
        if c != " ":
            c = c.lower()
            hashtable[c] = hashtable.get(c, 0) + 1

    odd_char_found = False
    for v in hashtable.values():
        if v % 2 == 1:
            if odd_char_found:
                return False
            odd_char_found = True

    return True


result = is_palindrome_permutation("level")
print(result)
