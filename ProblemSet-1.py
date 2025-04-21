"""
1. Converting an Integer into Decimals
2. Converting a String of Integers into Decimals
3. Reversing a String using an Extended Slicing Technique
4. Counting Vowels in a Given Word
5. Counting Consonants in a Given Word
6. Counting the Number of Occurrences of a Character in a String
7. Writing Fibonacci Series
8. Finding the Maximum Number in a List
9. Finding the Minimum Number in a List
10. Finding the Middle Element in a List
"""
import decimal

def q1():
    # 1. Converting an Integer into Decimals
    test_int = 123

    req_deci = decimal.Decimal(test_int)
    print("Type of number: "+str(type(req_deci)))

def q2():
    # 2. Converting a String of Integers into Decimals
    test_str = '123456'

    req_deci = decimal.Decimal(test_str)
    print("Type of number: " + str(type(req_deci)))

def q3():
    # 3. Reversing a String using an Extended Slicing Technique
    given_str = 'Hello my name is Varun!'

    rev_str = given_str[::-1]

    print(rev_str)

def q4():
    # 4. Counting Vowels in a Given Word
    """
    1. Convert the user string into lowercase
    2. Iterate over the string, check if character matches with list of vowels
    3. Increment counter everytime such a match is successful
    """
    user_str = "Hello, my name is Varunsingh Sisodia!"
    vowel_list = ['a','e','i','o','u']
    vowel_count = 0

    user_str_lower = user_str.lower()

    for character in user_str_lower:
        if character in vowel_list:
            vowel_count += 1

    print(f"Given string: '{user_str}' has {vowel_count} vowels!!")


def q5():
    # 5. Counting Consonants in a Given Word
    """
    1. Convert the user string into lowercase
    2. Iterate over the string, check if character matches with list of vowels
    3. Increment counter everytime such a match is NOT successful
    """
    user_str = "Hello, my name is Varunsingh Sisodia!"
    vowel_list = ['a','e','i','o','u']
    cons_count = 0

    user_str_lower = user_str.lower()

    for character in user_str_lower:
        if character not in vowel_list:
            cons_count += 1

    print(f"Given string: '{user_str}' has {cons_count} consonents!!")

def q6():
    # 6. Counting the Number of Occurrences of a Character in a String
    """
    1. Iterate over the user string character by character.
    2. Everytime we encounter the given character, increment counter by 1
    3. Return value in counter once the entire string is parsed
    :return:
    """
    user_str = "Hello, my name is Varunsingh Sisoadia!"
    req_char = 'a'
    char_count = 0

    for character in user_str.lower():
        if character == req_char:
            char_count += 1

    print(f"The character {req_char} occurs {char_count} times in the given string!")

def q7():
    # 7. Writing Fibonacci Series
    """
    Fibonacci series: 0,1,1,2,3,5,8....

    1. Create a default list [0,1]
    2. Iterate over a certain range, append the sum of the last two list elements into the list
    3. Continue process till range is iterated
    """
    fib_list = [0,1]

    for i in range(5):
        curr_sum = fib_list[-1] + fib_list[-2]
        print(f"Current sum: {curr_sum}")

        fib_list.append(curr_sum)
        print(f"Fib series: {fib_list}")

    # Converting list of integers to string
    fib_str = ', '.join(str(e) for e in fib_list)
    print(f"Fibonacci series: {fib_str}")


def q8():
    # 8. Finding the Maximum Number in a List
    """
    1. Let the max number initially be 0
    2. Iterate over the list of numbers, if the number encountered > 0, make it the new max.
    3. Continue iterating, if number > current max, it is the new max
    4. The number which is the current max once the loop ends is the required answer.
    """
    numberList = [15, 85, 35, 89, 125, 356, 0, 12345, 34, 99]
    current_max = 0

    for number in numberList:
        if number > current_max:
            current_max = number

    print(f"The max of all numbers is: {current_max}")

def q9():
    # 9. Finding the Minimum Number in a List
    """
    1. Let the min number initially be inf
    2. Iterate over the list of numbers, if the number encountered < inf, make it the new min.
    3. Continue iterating, if number > current min, it is the new min
    4. The number which is the current min once the loop ends is the required answer.
    """
    numberList = [15, 85, 35, 89, 125, 356, 10, 12345, 4, 99]
    curr_min = float('inf')

    for number in numberList:
        if number < curr_min:
            curr_min = number

    print(f"The min of all numbers is: {curr_min}")

def q10():
    # 10. Finding the Middle Element in a List
    """
    Even numbered list: [10,20,30,40] =>
    Odd numbered list: [10,20,30,40,50] => number at index = len(list)//2
    """
    numberList = [15, 85, 35, 89, 125, 356, 10, 12345, 4, 99, 456,67]

    middle_index = len(numberList) // 2

    print(f"Middle number in list: {numberList[middle_index]}")


if __name__ == '__main__':
    q10()

