"""
1. Converting a List into a String
2. Adding Two List Elements Together
3. Comparing Two Strings for Anagrams
4. Checking for Palindrome Using Extended Slicing Technique
"""
def q1():
    # 1. Converting a List into a String
    lst = ["P", "Y", "T", "H", "O", "N", "IS","G","R","E","A","T"]

    str_list = ''.join(lst)
    print(f"The joined string is: {str_list}")

def q2():
    # 2. Adding Two List Elements Together
    """
    1. Ensure that both lists are of same size, flag error if not
    2. Iterate over one list, add element at current index from both lists
    3. Store this sum
    4. Once iteration is over, return list of sum.
    :return:
    """
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]

    try:
        if len(lst1) != len(lst2):
            raise Exception("List size mismatch!")
        else:
            res_list = []

            for index in range(0, len(lst1)):
                res_list.append(lst1[index] + lst2[index])

            print(f"Addition of the two lists returns: {res_list}")
    except Exception as e:
        print(e)

def q3():
    # 3. Comparing Two Strings for Anagrams
    """
    Anagrams? => silent and listen

    Conditions for anagrams:
    1. Length of strings is the same.
    2. Same frequency of characters
    3. All characters are rearranged

    sort() vs sorted()

    sort(<list>) -> sorts a list of characters
    sorted(<string>) -> sorts the characters in a string and returns a list
    """
    str1 = "silenttt"
    str2 = "listentt"

    # Method-1: Using sort()
    str1_list = list(str1)
    str2_list = list(str2)

    str1_list.sort(), str2_list.sort()

    if str1_list == str2_list:
        print("Anagram using sort() method!")
    else:
        print("Not an anagram using sort() method!")

    # Method-2: Using sorted()

    if sorted(str1) == sorted(str2):
        print("Anagram using sorted() method!")
    else:
        print("Not an anagram using sorted() method!")

    # Method-3: Without using in-built functions
    """
    Check two conditions:
    1. Length of string is same
    2. Frequency of chars is same
    """

    if len(str1) == len(str2):
        dict1 = {}
        dict2 = {}
        char_count = 0

        for char in str1:
            if char not in dict1.keys():
                dict1[char] = 1
            else:
                dict1[char] += 1

        print(dict1)

        for char in str2:
            if char not in dict2.keys():
                dict2[char] = 1
            else:
                dict2[char] += 1

        print(dict2)

        if dict1 == dict2:
            print("Anagram using longcut method!")
        else:
            print("Not an anagram using longcut method1")
    else:
        print("Not an anagram!")

def q4():
    # 4. Checking for Palindrome Using Extended Slicing Technique
    """
    A palindrome string is one which reads the same forward and backward
    """
    usr_string_list = ["madam", "racecar", "level", "varun"]

    for word in usr_string_list:
        word = word.lower()
        rev_word = word[::-1]

        if word == rev_word:
            print("Palindrome!")
        else:
            print("Not a palindrome!")

"""
5. Counting the White Spaces in a String
6. Counting Digits, Letters, and Spaces in a String
7. Counting Special Characters in a String
8. Removing All Whitespace in a String
9. Building a Pyramid in Python
10. Randomizing the Items of a List in Python
"""

def q5():
    """
    Given a string with white spaces, count number of white spaces

    1. Read the string character by character
    2. For every encounter of whitespace, increment counter by 1
    """
    usr_string = "P r ogramm in g "
    counter = 0

    for char in usr_string:
        if char == ' ':
            counter += 1

    print(f"The number of whitespaces in the string is: {counter}")

    print(" ------ Alternate method -------")

    print(f"Whitespace count by alternate method: {usr_string.count(' ')}")


def q6():
    """
    Counting Digits, Letters, and Spaces in a String

    1. Read the string character by character
    2. Check if character is a digit/letter or a whitespace.
    3. Increment counters accordingly
    """
    usr_string = 'Python is 1'
    counter_dict = {
        'Alphabet':0,
        'Digit':0,
        'Space':0
    }

    for char in usr_string:
        if char.isalpha():
            counter_dict['Alphabet'] += 1
        elif char.isdigit():
            counter_dict['Digit'] += 1
        elif char.isspace():
            counter_dict['Space'] += 1

    for key, value in counter_dict.items():
        print(f"{key} : {value}")

def q7():
    """
    Counting special characters in a string

    1. Read string character by character
    2. Create a list of special characters
    3. Check if traversed character is any of the special chars
    4. If yes, increment counter
    5. If not, move on
    """
    usr_string = "!@#$%^&*()"
    special_chars_list = ['!','@','#','$','%','^','&','*','(',')']
    counter = 0

    for char in usr_string:
        if char in special_chars_list:
            counter += 1

    print(f"The number of special characters in the string is: {counter}")

def q8():
    """
---
### 🧼 Project: ChatSanitizer 3000

You're part of a team developing **ChatSanitizer 3000**,
a backend service for a futuristic messaging app where users can
send voice-to-text messages that get *auto-formatted*. Unfortunately, the voice-to-text engine
sometimes adds a **lot of unnecessary whitespace** in weird places—extra spaces, tabs, even newlines.

Your task?
Write a function that takes in a user’s transcribed message and **cleans it up by removing all whitespace**,
so it can be passed into the next layer of processing like translation, emoji replacement,
or even sarcasm detection (yes, that’s real in 2042).

---

### 💻 Example

```python
Input:  "   Hello    World \n How are   you?  "
Output: "HelloWorldHowareyou?"
```
---
### ✅ Requirements
- Remove **all types** of whitespace: spaces, tabs, newlines, etc.
- No fancy libraries—just standard Python.
    """
    usr_string = "   Hello    World \n How are   you?  "
    new_string_list = []

    for ele in usr_string:
        if ele.isspace():
            continue
        else:
            new_string_list.append(ele)

    new_string = ''.join(new_string_list)
    print(f"String without whitespace chars: {new_string}")


def q9():
    """
    Scenario: The Pharaoh’s Architect
    You're a legendary architect in Ancient Egypt, hired by the Pharaoh to build a grand pyramid made of stone blocks.
    The blocks must be stacked in a symmetrical pyramid form — each level must have an odd number of blocks, centered
    perfectly, and the top should start with 1 block, increasing by 2 blocks per level (i.e., 1, 3, 5…).

    The Pharaoh gives you the height of the pyramid (number of levels), and your task is to generate the pyramid design
    in Python to show the royal engineers.

    Strategy:
    1. Number of spaces = height - level - 1
    2. Number of blocks = 2 * level + 1
    3. Iterate for given pyramid height.
    """
    pyramid_height = 7

    for level in range(pyramid_height):
        count_spaces = pyramid_height - level - 1
        block_count = 2 * level + 1

        print(' ' * count_spaces + '*' * block_count)




import random

def q10():
    """
    Project: LootBox Shuffler 2.0
    You're working at a game studio building an epic loot box system for a fantasy RPG.
    Players open treasure chests, and behind the scenes, your server randomly shuffles the loot table before
    selecting items to give that “surprise” factor.

    Your task is to implement the logic that randomizes the items in a list—so that every time a chest is opened,
    the order of potential items is different

    Challenges:
    1. Return the shuffled list
    2. Return a new shuffled list without modifying the original
    3. Shuffle with a fixed seed for reproducible results (great for testing)

    Strategy:
    1. random.shuffle(<list>) => randomizes the list in-place and returns None i.e it modifies the original list
    2. Apply random.shuffle(<list>) on a copy of the original list
    3. To ensure predictable shuffling, apply a seed value using the random.seed() function before shuffling
    """
    loot = ['Sword', 'Shield', 'Potion', 'Gold', 'Bow']
    loot_copy = loot

    print(" --- Challenge-1 ---")
    random.shuffle(loot_copy)
    print(f"Shuffled list: {loot_copy}")

    print(" --- Challenge-2 ---")
    random.seed(12)
    random.shuffle(loot)

    print(f"Shuffled list: {loot}")


"""
11. Find the Largest Element in a List
12. Remove Duplicates from a List
13. Factorial of a Number
14. Merge Two Sorted Lists
15. Find the First Non-Repeating Character
"""

def q11():
    """
    You are the Race Coordinator of an underground robot racing championship 🏎️🤖 held in a secret desert location.
    Each robot logs its top speed during the race, and you receive a list of their max speeds in km/h.

    Your job is to identify the fastest robot by finding the largest value in the list of recorded speeds
    """
    robot_speeds = [127, 245, 199, 310, 278]
    current_max = 0

    for speed in robot_speeds:
        if speed > current_max:
            current_max = speed

    print(f"The max value in the given list: {current_max}")

def q12():
    """
---

### 🎧 **Scenario: DJ NoRepeat’s Party Playlist**

You’re the assistant to the famous **DJ NoRepeat**, who’s about to perform at the biggest electronic music festival of
the year. He’s preparing his playlist, but in his excitement, he added some of the same tracks multiple times.

Your job is to clean up the playlist by **removing duplicate song entries**, so that each track plays only once.
DJ NoRepeat is very particular about **track order**, so your solution should ideally keep the original order of
first occurrences.

---

### 📀 Example Input:
```
["Bass Drop", "Neon Lights", "Bass Drop", "Skyline", "Neon Lights", "Dreamscape"]
```

---

### 🎶 Output:
```
["Bass Drop", "Neon Lights", "Skyline", "Dreamscape"]
```
    """
    playlist = ["Bass Drop", "Neon Lights", "Bass Drop", "Skyline", "Neon Lights", "Dreamscape"]

    unq_playlist = list(set(playlist))

    print(f"Unique tracks: {unq_playlist}")


def q13(mission_num):
    """
---

### 🚀 **Scenario: Launch Countdown Control – Space Factorial**

You're the **Mission Control Analyst** at **StarReach Aerospace**, and there's a secret formula used to calculate
the **launch code** for a space probe. The formula involves computing the **factorial of a security number**
assigned to each mission.

Each digit of the final launch code is derived from the **factorial of the mission number**,
which represents the number of secure systems that must initialize sequentially before liftoff.

For example, if the mission number is `5`, then the total sequence count is calculated as:

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

This number (`120`) is then encoded into the launch system.

---

### 🧪 Example Input:
```
Mission number: 5
```

---

### ✅ Output:
```
Launch sequence initiated with code: 120
```
Your next mission awaits, Commander. 🧑‍🚀✨
    """
    if mission_num == 0:
        return 1
    else:
        # print("Inside!")
        return mission_num * q13(mission_num-1)


def q14():
    """
Scenario: Merging Sorted Log Files
You are working on a log aggregation service. Two microservices (Service A and Service B)
generate sorted logs based on timestamps. Each log entry is a tuple containing (timestamp, log_message)
and both services independently maintain their sorted lists.

Your task is to merge the logs from both services into a single list, ensuring the combined log is still sorted by
timestamp. This merged list will be used to display a unified trace in your observability dashboard.

Example:
# Logs from Service A
logs_a = [
    ("2025-03-22T10:01:05", "Auth token validated"),
    ("2025-03-22T10:01:07", "User profile loaded"),
    ("2025-03-22T10:01:12", "Session refreshed"),
]

# Logs from Service B
logs_b = [
    ("2025-03-22T10:01:06", "Cache hit for user ID"),
    ("2025-03-22T10:01:09", "DB query executed"),
]
Expected Output:
[
    ("2025-03-22T10:01:05", "Auth token validated"),
    ("2025-03-22T10:01:06", "Cache hit for user ID"),
    ("2025-03-22T10:01:07", "User profile loaded"),
    ("2025-03-22T10:01:09", "DB query executed"),
    ("2025-03-22T10:01:12", "Session refreshed"),
]

Strategy:
1. Combine two lists using concat operator.
2. Apply sort method

    """
    logs_a = [
        ("2025-03-22T10:01:05", "Auth token validated"),
        ("2025-03-22T10:01:07", "User profile loaded"),
        ("2025-03-22T10:01:12", "Session refreshed"),
    ]

    # Logs from Service B
    logs_b = [
        ("2025-03-22T10:01:06", "Cache hit for user ID"),
        ("2025-03-22T10:01:09", "DB query executed"),
    ]

    combined_logs = logs_a + logs_b
    print(f"Combined logs before sorting:{combined_logs}")

    combined_logs_sorted = sorted(combined_logs) # Sorted function will by default sort based on the first value in the tuple i.e the timestamp
    print(f"Combined logs sorted: {combined_logs_sorted}")

def q15():
    """
### Scenario: User Support Ticket Classifier

You’re building a backend tool that automatically classifies **customer support tickets** based on their issue descriptions.
The goal is to identify **distinctive keywords** that help categorize the ticket quickly.

To optimize keyword extraction, your system tries to find the **first non-repeating character** in the entire support
description string — this helps eliminate generic or spammy entries that might be repeated often.

This character is used as an internal signal for identifying potential **unique identifiers** in short phrases or logs
submitted by users.

---

### Example:

```python
support_ticket = "login issue reported again"
```

### Expected Output:
```
First non-repeating character: 'l'
```

(*'l' appears only once and comes before any other non-repeating character.*)

---

You might extend this logic to:
- Case-insensitive processing (`'A'` vs `'a'`)
- Ignoring whitespace or special characters
- Handling Unicode text from global support systems
    """
    string_list = ["LOGin ISsue Reported again","technical escalation","email email email","café au lait","","aaaaaa","  "]

    for usr_string in string_list:
        print(f"String being inspected:{usr_string}")

        if usr_string == "" or usr_string == " ":
            print(f"User has not entered anything!")
        else:
            usr_string_lc = usr_string.lower()
            char_count_dict = {}

            for char in usr_string_lc:
                if char not in char_count_dict.keys():
                    char_count_dict[char] = 1
                else:
                    char_count_dict[char] += 1

            # print(f"Char count dictionary:{char_count_dict}")

            for key in char_count_dict.keys():
                if char_count_dict[key] == 1:
                    print(f"The first non-repeating character is: {key}")
                    break




if __name__ == '__main__':
    # launch_code = q13(12)
    # print(f"The launch code is: {launch_code}")

    q15()

