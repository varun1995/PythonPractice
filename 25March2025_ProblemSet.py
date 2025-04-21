"""
✅ 1. Scenario: CRM Dashboard – Summarize Sales
Project Context:
You're working on a CRM system where regional sales data is tracked daily for every salesperson.
The frontend requires a real-time widget that shows total sales per user from a list of daily values.

Task:
Write a function that takes a list of numbers and returns their total sum.

✅ 2. Scenario: Localization Testing – Reverse Language Tokens
Project Context:
You're assigned to test the new language translation module. The system uses reversed strings to
simulate a “mirror-language” for testing UIs with right-to-left scripts. You need to verify if your function
correctly reverses strings for a test case.

Task:
Given a string, return its reversed version.

✅ 3. Scenario: QA Automation – Anagram Validation
Project Context:
Your automated test suite validates user input normalization. In one case, the app allows users to rearrange
character tiles to form words. The backend validates if the newly formed word is a valid anagram of the original.

Task:
Write a function that takes two strings and returns whether they are anagrams of each other.

✅ 4. Scenario: Data Integration – Filter Palindromes from Feed
Project Context:
You’re integrating a third-party logging system that sends random labels. You’ve noticed a bug where the
system sometimes sends palindromes as labels which confuse your deduplication logic.
These need to be filtered out before storing them.

Task:
Write a function that takes a list of strings and returns only the ones that are palindromes.

✅ 5. Scenario: DevOps Tooling – Find Second Highest Uptime
Project Context:
Your internal dashboard tracks server uptimes across environments. For reporting purposes, you’re asked to highlight
the second highest uptime for comparative reliability assessment.

Task:
Given a list of server uptime values (numbers), return the second highest number.
"""
def q1():
    """
    ✅ 1. Scenario: CRM Dashboard – Summarize Sales
    Project Context:
    You're working on a CRM system where regional sales data is tracked daily for every salesperson.
    The frontend requires a real-time widget that shows total sales per user from a list of daily values.

    Task:
    Write a function that takes a list of numbers and returns their total sum.
    """
    usr_list = [1,2,3,4,5]
    sum = 0

    for number in usr_list:
        sum += number

    print(f"Sum of elements: {sum}")

def q2():
    """
    ✅ 2. Scenario: Localization Testing – Reverse Language Tokens
    Project Context:
    You're assigned to test the new language translation module. The system uses reversed strings to
    simulate a “mirror-language” for testing UIs with right-to-left scripts. You need to verify if your function
    correctly reverses strings for a test case.

    Task:
    Given a string, return its reversed version.
    """
    usr_string = "I am the ruler of my mind!"
    rev_usr_string = usr_string[::-1]

    print(f"The reverse of the string is:{rev_usr_string}")

def q3():
    """
    ✅ 3. Scenario: QA Automation – Anagram Validation
    Project Context:
    Your automated test suite validates user input normalization. In one case, the app allows users to rearrange
    character tiles to form words. The backend validates if the newly formed word is a valid anagram of the original.

    Task:
    Write a function that takes two strings and returns whether they are anagrams of each other.

    Strategy:
    Anagram => silent listen

    Conditions for an anagram:
    1. Same letters
    2. String of same length
    3. Rearranged letters
    """
    str1 = "triangle"
    str2 = "integral"

    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())

    if str1 == str2:
        print("Anagram")
    else:
        print("Not an anagram!")


def q4():
    """
    ✅ 4. Scenario: Data Integration – Filter Palindromes from Feed
    Project Context:
    You’re integrating a third-party logging system that sends random labels. You’ve noticed a bug where the
    system sometimes sends palindromes as labels which confuse your deduplication logic.
    These need to be filtered out before storing them.

    Task:
    Write a function that takes a list of strings and returns only the ones that are palindromes.
    """
    labels = [
        "radar",
        "error202",
        "level",
        "devops",
        "civic",
        "Status",
        "noon",
        "root",
    ]

    for label in labels:
        if label == label[::-1]:
            print(f"{label} is a palindrome!")
        else:
            print(f"{label} is not a palindrome!")

def q5():
    """
    ✅ 5. Scenario: DevOps Tooling – Find Second Highest Uptime
    Project Context:
    Your internal dashboard tracks server uptimes across environments. For reporting purposes, you’re asked to highlight
    the second highest uptime for comparative reliability assessment.

    Task:
    Given a list of server uptime values (numbers), return the second highest number.

    1. There must be least be two values in the list, if not return None.
    2. If the list contains all same elements, return None.
    """
    test_cases = [
        [4, 2, 8, 5, 9, 1],  # ✅ Normal data, expected second highest: 8
        [10, 10, 8, 7, 7, 3],  # 🟨 Duplicates, expected: 8
        [6, 6, 6, 6],  # 🔁 All same, expected: None or handled as invalid
        [15],  # 🔻 Only one element, expected: None or error
        [100, 90, 80, 70],  # 📉 Descending order, expected: 90
        [3, 5, 8, 12, 20],  # 📈 Ascending order, expected: 12
        [1, 2],  # Minimal valid input, expected: 1
        [-5, -10, -3, -8],  # ⚠️ Negative uptimes (for stress test), expected: -5
    ]

    for test_list in test_cases:
        if len(test_list) < 2:
            print(f"Error, requires at least two elements!")
        elif len(set(test_list)) == 1:
            print(f"Error, all elements are the same!!")
        else:
            test_list_unq = list(set(test_list))
            print(f"Unique elements: {test_list_unq}")
            test_list_unq.sort()

            print(f"Second highest time: {test_list_unq[-2]}")



if __name__ == '__main__':
    q5()

