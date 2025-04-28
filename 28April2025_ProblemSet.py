"""
Q1: Product Catalog – Extract Unique Categories (Case-Insensitive)

Task:
Normalize product category names and extract unique ones, ignoring case.

Test Data:
categories = [
    "Electronics", "Home", "home", "electronics", "Books", "books", "Fashion", "FASHION"
]
Expected Output:
["electronics", "home", "books", "fashion"]
"""
def q1():
    categories = [
        "Electronics", "Home", "home", "electronics", "Books", "books", "Fashion", "FASHION"
    ]

    categories = [category.lower() for category in categories]
    # print(f"{categories}")

    print(f"Required list: {list(set(categories))}")


"""
Q2: Security System – Find Passwords Without Numbers

Task:
Find all passwords that do not contain any digits.

Test Data:
passwords = [
    "abc123", "password", "securePASS", "test1test", "NOdigitsHERE", "123456", "plainpassword"
]
Expected Output:
["password", "securePASS", "NOdigitsHERE", "plainpassword"]
"""
import re

def q2():
    passwords = [
        "abc123", "password", "securePASS", "test1test", "NOdigitsHERE", "123456", "plainpassword"
    ]

    final_list = []

    pattern = r"^[a-zA-Z]+"

    for password in passwords:
        match = re.fullmatch(pattern, password)

        if match:
            final_list.append(match.group())

    print(f"Final list: {final_list}")


"""
Q3: Employee Database – Standardize Employee IDs

Task:
Make sure employee IDs are uppercase and prefixed with 'EMP_'. If not, add it.

Test Data:
employee_ids = [
    "emp_123", "EMP_456", "123EMP", "emp_789", "EMP001"
]
Expected Output:
["EMP_123", "EMP_456", "EMP_123EMP", "EMP_789", "EMP_EMP001"]
"""

def q3():
    employee_ids = [
        "emp_123", "EMP_456", "123EMP", "emp_789", "EMP001"
    ]

    pattern = r"^emp_.*"

    employee_ids = [
        eid.upper() if re.fullmatch(pattern, eid, flags=re.IGNORECASE) else "EMP_" + eid.upper()
        for eid in employee_ids
    ]

    print(f"Required list: {employee_ids}")

"""
Q4: Message Cleaner – Remove All Punctuation

Task:
Remove all punctuation from user messages, keeping letters and spaces.

Test Data:
messages = [
    "Hello, world!", "What's up?", "Good job!!!", "Python > Java?", "Simple and clean."
]
Expected Output:
[
    "Hello world",
    "Whats up",
    "Good job",
    "Python  Java",
    "Simple and clean"
]
"""
def q4():
    messages = [
        "Hello, world!", "What's up?", "Good job!!!", "Python > Java?", "Simple and clean."
    ]

    final_list = []

    for message in messages:
        # print(f"{list(message)}", end='\n')

        tmp_list = list(message)
        tmp_string = ""

        char_list = [
            char for char in tmp_list if char.isspace() or char.isalpha()
        ]

        tmp_string = ''.join(char_list)

        final_list.append(tmp_string)

    print(f"Final list: {final_list}")



"""
Q5: Event Logger – Identify Error Events

Task:
Find all log lines containing 'error' (case-insensitive), even as part of a bigger word.

Test Data:
log_entries = [
    "System started successfully",
    "CriticalError encountered during load",
    "User logged out",
    "Disk ERROR detected",
    "Running diagnostics",
    "fatalerror in module"
]
Expected Output:
[
    "CriticalError encountered during load",
    "Disk ERROR detected",
    "fatalerror in module"
]
"""
def q5():
    log_entries = [
        "System started successfully",
        "CriticalError encountered during load",
        "User logged out",
        "Disk ERROR detected",
        "Running diagnostics",
        "fatalerror in module"
    ]

    final_list = []

    pattern = r".*error.*"

    for entry in log_entries:
        match = re.search(pattern, entry, flags=re.IGNORECASE)

        if match:
            # print(f"{match.group()}")
            final_list.append(match.group())

    print(f"Final list: {final_list}")


if __name__ == '__main__':
    q5()

