"""
Problem 1: Find the First Non-Repeating Character in a String
Problem Explanation
You are given a string s consisting of lowercase English letters.
Your task is to find and return the first non-repeating character in the string.
If all characters repeat, return "_".
Example
plaintext
Copy
Edit
Input: s = "abacabad"
Output: "c"
Explanation:
- The non-repeating characters are: 'c' and 'd'
- 'c' appears first in the string.
"""
from collections import Counter

def first_non_repeating_char(usrStr):

    # Create a dict with character count
    # char_count = Counter(usrStr)
    # print(char_count)

    char_count = {}

    for char in usrStr:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in usrStr:
        if char_count[char] == 1:
            return char

    return '_'


print(first_non_repeating_char("abacabad"))  # Output: "c"
print(first_non_repeating_char("abacaba"))   # Output: "d"
print(first_non_repeating_char("aabbcc"))    # Output: "_"



