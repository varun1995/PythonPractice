"""
Problem 2: Increment a Number Represented as an Array of Digits
Problem Explanation
You are given an array of integers digits, where each integer represents a single digit of a number.
The digits together form a positive integer.
Your task is to increment the number by 1 and return the result as an array.

Example

Input: digits = [1, 2, 3]
Output: [1, 2, 4]
Explanation: 123 + 1 = 124, so return [1, 2, 4]

Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]
Explanation: 999 + 1 = 1000, so return [1, 0, 0, 0]
"""
def plus_one(num_list):

    # Convert list of numbers into list of strings
    # num_str_list = map(str, num_list)
    # print(num_str_list)

    # for num in num_str_list:
    #     print(type(num))

    # Join the list of strings to create a single number
    # joined_num = int("".join(num_str_list))
    # print(joined_num)

    # Add one to this number
    # joined_num += 1
    # print(joined_num)

    # Split the number back to a list of numbers
    # new_num_list = [int(x) for x in str(joined_num)]
    # print(new_num_list)

    # Concise solution

    new_number = int("".join(map(str, num_list))) + 1
    # print(f"New num: {new_number}")

    return [int(x) for x in str(new_number)]

    # return new_num_list



print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]
print(plus_one([9, 9, 9]))  # Output: [1, 0, 0, 0]
print(plus_one([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]