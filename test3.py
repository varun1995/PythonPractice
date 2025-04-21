"""
Problem 3: Reverse the Order of Words in a Sentence
Problem Explanation
You are given a sentence as a string.
Your task is to reverse the order of words but keep the words themselves unchanged.
You can assume that:
The input does not have leading, trailing, or repeating spaces.
Example

Input: sentence = "Man bites dog"
Output: "dog bites Man"
The words remain the same, but their order is reversed.

Algorithm:
1. Split the given string into a list of words.
2. Reverse the order of the words in the list words[::-1]
3. Join the words back into a list and return it
"""


def reverse_words(usr_str):
    # Step-1: Convert given string into a list of strings
    word_list = usr_str.split()
    # print(f"Original list of words: {word_list}")

    # Step-2: Reverse order of words in the list
    rev_word_list = word_list[::-1]
    # print(f"Reversed list of words: {rev_word_list}")

    # Step-3: Combine this list back to a string
    rev_string = " ".join(rev_word_list)

    return rev_string


def alternate(usr_string):
    return " ".join(reversed(usr_string.split()))


# Example usage
print(reverse_words("Man bites dog"))  # Output: "dog bites Man"
print(reverse_words("Hello world"))  # Output: "world Hello"
print(reverse_words("Python is fun"))  # Output: "fun is Python"

print(alternate("Man bites dog and cat"))  # Output: "dog bites Man"
print(alternate("Hello world, bye world"))  # Output: "world Hello"
print(alternate("Python is fun and interesting"))  # Output: "fun is Python"
