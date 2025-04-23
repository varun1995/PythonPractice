"""
### ✅ **1. Scenario: CRM System – Remove Duplicate Contacts (Keep First Occurrence)**

**Context**:
Your CRM system imports contact data from different sources. Some contacts are duplicated based on their names.
You’re building a cleanup script to remove duplicate names **while keeping only the first occurrence**.

**Task**:
Write a function that takes a list of names and returns a list with duplicates removed, preserving the original order.

"""
def q1():
    contact_names = [
        "Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve", "Frank", "Alice"
    ]

    # Expected Output:
    # ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

    distinct_contact_names = list(set(contact_names))

    print(f"Required list: {distinct_contact_names}")


"""
### ✅ **2. Scenario: Log Formatter – Pad Single-Digit Values**

**Context**:
You’re formatting timestamps in logs. All numeric values like hours, minutes, and seconds must be represented with 
**2 digits** (e.g., `08` instead of `8`).

**Task**:
Write a function that takes a list of integers and returns them as **2-digit strings**, left-padded with 0 if needed.

"""
def q2():
    time_values = [
        1, 5, 10, 0, 23, 8
    ]

    # Expected Output:
    # ["01", "05", "10", "00", "23", "08"]

    final_list = []

    for time_val in time_values:
        if int(time_val) % 10 == int(time_val):
            time_val = "0" + str(time_val)
            # print(f"{time_val}")
            final_list.append(time_val)
        else:
            final_list.append(time_val)

    print(f"Final list: {final_list}")


"""

### ✅ **3. Scenario: Chat Profanity Monitor – Count Banned Word Matches**

**Context**:
Your customer service chatbot flags any incoming message that contains banned words. You need to count how many **banned 
words** are present in each message (case-insensitive).

**Task**:
Write a function that takes a string and a list of banned words, and returns how many banned words appear in the message.
"""
def q3():
    banned_words = ["damn", "idiot", "stupid"]

    messages = [
        "That was a damn stupid idea.",
        "No profanity here.",
        "You are an IDIOT!",
        "Absolutely DAMN ridiculous!",
        "Just stop it already."
    ]

    # Expected Output (counts):
    # [2, 0, 1, 1, 0]

    final_dict = {}

    for msg in messages:
        count = 0
        for word in banned_words:
            if word.lower() in msg.lower():
                count += 1
        final_dict[msg] = count

    print(f"Required details: {final_dict}")


"""
### ✅ **4. Scenario: Deployment Tool – Extract Filename from Path**

**Context**:
Your deployment automation tool works with file paths and needs to extract just the **filename** from a full path string
 (e.g., `/home/deploy/app/config.yaml` → `config.yaml`).

**Task**:
Write a function that extracts the filename from a full file path string.
"""
import re
def q4():
    file_paths = [
        "/home/user/documents/report.docx",
        "C:\\Users\\Admin\\Desktop\\data.csv",
        "./logs/system.log",
        "/var/www/html/index.html",
        "setup.py"
    ]

    # Expected Output:
    # ["report.docx", "data.csv", "system.log", "index.html", "setup.py"]

    final_list = []

    pattern = r"[^\\/]+$"

    for path in file_paths:
        match = re.search(pattern, path)

        if match:
            # print(f"Found file name: {match.group()}")
            final_list.append(match.group())

    print(f"Final list:{final_list}")

"""

### ✅ **5. Scenario: Code Review Bot – Highlight TODO Comments**

**Context**:
In your codebase, developers use comments like # TODO: Refactor this, and you want your static analysis bot to extract
all such TODO lines from a list of code lines.

**Task**:
Write a function that returns all lines from a list of strings that contain `"TODO"` (case-insensitive match).
"""
def q5():
    code_lines = [
        "# TODO: Refactor this module",
        "print('Hello World')",
        "# FIXME: This is broken",
        "# todo: update configuration handling",
        "def calculate(): pass",
        "# ToDo: Check edge cases",
        "# DONE: Completed work"
    ]

    # Expected Output:
    # ["# TODO: Refactor this module", "# todo: update configuration handling", "# ToDo: Check edge cases"]

    pattern = "# todo"

    final_list = []

    for line in code_lines:
        split_list = line.split(':')
        # print(f"{split_list}")

        if split_list[0].lower() == pattern:
            joined_line = ':'.join(split_list)
            final_list.append(joined_line)

    print(f"Final list:{final_list}")


if __name__ == '__main__':
    q5()




