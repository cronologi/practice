# Write a method to replace all spaces in a string with "%20". You may assume that the string has sufficient space
# at the end to hold the additional characters, and that you are given the "true" length of the string.
# EXAMPLE:
# Input     "Mr John Smith      ", 13
# Output    "Mr%20John%20Smith"

def urlify(text):
    return text.replace(" ", "%20")

text = "Davor Ema"
text = urlify(text)
print(text)

def urlify2(string, length):
    charArr = list(string)
    j = len(charArr) - 1

    for i in range(length - 1, -1 , -1):
        if(charArr[i] != ' '):
            charArr[j] = charArr[i]
            j -= 1
        else:
            charArr[j] = '0'
            charArr[j - 1] = '2'
            charArr[j - 2] = '%'
            j -= 3

    return "".join(charArr)

text = "Mr John Smith    "
text = urlify2(text, 13)
print(text)