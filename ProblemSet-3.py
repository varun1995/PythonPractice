"""
Problem list:
1. Write a function to count the number of unique digits in a number -
eg 111 -> 1
 121 -> 2
 123 -> 3

2. Program to flatten the list
 Input: l1 = [1,[2,3, [4, 5]]]
 Output: l1 = [1,2,3,4,5]

3. Find duplicates in a list.
4. Check if a string has matching brackets
{[()]}  # True
{[(])}  # False
"""


def q1():
    """
    Find number of unique digits in a number
    111 -> 1
    121 -> 2
    123 -> 3
    :return:
    """
    usr_num = 121

    unq_digits_set = set()

    for digit in str(usr_num):
        unq_digits_set.add(digit)

    print("Num of unique digits in given number: " + str(len(unq_digits_set)))


def q2(l1):
    """
    Program to flatten the list

    1. Iterate through the list
    2. If element is of type 'list', recursively flatten it
    3. If not, add to result list
    :return:
    """

    result = []

    for ele in l1:
        if isinstance(ele, list):
            result += q2(ele)
        else:
            result.append(ele)

    return result


def q3(ele_list):
    """
    Find the duplicates in a list

    1. Create two sets - one for tracking traversed elements and another for tracking duplicate elements.
    2. Traverse the list, if the current element is encountered for the first time, add it to the 'seen' set
    3. If the element has already been encountered, add it to the duplicates set.
    4. Once all elements are traversed, return the duplicates set as a list.
    :return:
    """
    traversed_ele_set = set()
    duplicate_ele_set = set()

    for ele in ele_list:
        if ele in traversed_ele_set:
            duplicate_ele_set.add(ele)
        else:
            traversed_ele_set.add(ele)

    return list(duplicate_ele_set)

def q4_is_balanced(s):
    """
    4. Check if a string has matching brackets
    {[()]}  # True
    {[(])}  # False

    Strategy:
    1. Create a empty stack to store opening brackets as they are encountered.
    2. Create a dictionary mapping closing brackets to their corresponding opening brackets
    3. Iterate through the string of brackets
        For every opening bracket encountered, store it onto a stack.
        On encountering a closing bracket, pop the topmost element from the stack.
            Check if it matches with the mapping present in the dict.
            If not, it means that the brackets were closed incorrectly => return false
    4. Once the string is traversed completely, if the stack is empty, it means that all brackets were correctly matched
            Hence return True
    """

    stack = []  # Stack to keep track of opening brackets
    mapping = {')': '(', '}': '{', ']': '['}  # Dictionary to match closing with opening brackets

    for char in s:
        if char in mapping:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'  # Pop the last opening bracket (if stack is not empty)
            if mapping[char] != top_element:  # If it doesn't match the expected opening bracket
                return False
        else:
            stack.append(char)  # Push opening bracket onto the stack

    return not stack  # If stack is empty at the end, it's balanced






if __name__ == '__main__':
    # Q2
    # l1 = [1, [2, 3, [4, 5]]]
    # flattened_list = q2(l1)
    # print(f"Flattened list: {flattened_list}")

    # Q3
    # nums = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 8, 9, 9, 1, 2, 34, 5]
    # duplicates = q3(nums)
    # print(f"List of duplicates:{duplicates}")

    # Q4 Test Cases
    print(q4_is_balanced("{[()]}"))  # True
    print(q4_is_balanced("{[(])}"))  # False
    print(q4_is_balanced("()[]{}"))  # True
    print(q4_is_balanced("({[)]}"))  # False
    print(q4_is_balanced("{[()][]}"))  # True

