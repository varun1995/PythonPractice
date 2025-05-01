"""
Q1: Notification Service – Find Emails Without '@'

Task:
Your email validation system needs to filter out entries that do not contain the '@' symbol.

Test Data:
emails = [
    "user@example.com", "admin@", "contact", "info@mail.com", "@domain.com", "support@help.org"
]
Expected Output:
["admin@", "contact"]
"""
import re
def q1():
    emails = [
        "user@example.com", "admin@", "contact", "info@mail.com", "@domain.com", "support@help.org"
    ]

    pattern = r"^[^@]+$"

    for mail in emails:
        match = re.search(pattern, mail)

        if match:
            print(f"{match.group()}")


"""
Q2: User Analytics – Extract Names That Start With Vowels

Task:
You're analyzing user names and need to filter those that start with a vowel (case-insensitive).

Test Data:
names = ["Alice", "bob", "Eve", "ian", "Uma", "Charlie", "oliver"]
Expected Output:
["Alice", "Eve", "ian", "Uma", "oliver"]
"""
def q2():
    names = ["Alice", "bob", "Eve", "ian", "Uma", "Charlie", "oliver"]

    pattern = r"^[AEIOU].*$"

    final_list = []

    for name in names:
        match = re.search(pattern, name, flags=re.IGNORECASE)

        if match:
            # print(f"{match.group()}")
            final_list.append(match.group())

    print(f"Required list: {final_list}")

"""
Q3: Dashboard Formatter – Capitalize First Letter of Each Word

Task:
Given a dashboard label string, format it by capitalizing the first letter of each word.

Test Data:
labels = [
    "user activity", "error log", "system uptime", "disk usage", "CPU load"
]
Expected Output:
["User Activity", "Error Log", "System Uptime", "Disk Usage", "CPU Load"]
"""
def q3():
    labels = [
        "user activity", "error log", "system uptime", "disk usage", "CPU load"
    ]

    labels = [label.capitalize() for label in labels]

    print(f"Required list: {labels}")


"""
Q4: Metrics Aggregator – Sum Only Even Numbers

Task:
Your metrics system receives a list of numbers. Sum only the even ones.

Test Data:
values = [10, 15, 22, 7, 8, 13, 2]
Expected Output:
42
"""
def q4():
    values = [10, 15, 22, 7, 8, 13, 2]

    sum = 0

    for value in values:
        if value % 2 == 0:
            sum += value

    print(f"Final sum: {sum}")

"""
Q5: File Sanitizer – Remove Extra Dots from Filenames

Task:
You're processing filenames and need to ensure that each file has **only one dot** (before the extension).  
Remove all other dots from the filename.

Test Data:
filenames = [
    "my.file.name.txt", "report.final.version.doc", "summary.pdf", "log..txt", "justfile"
]
Expected Output:
["myfilename.txt", "reportfinalversion.doc", "summary.pdf", "log.txt", "justfile"]
"""
def q5():
    filenames = [
        "my.file.name.txt", "report.final.version.doc", "summary.pdf", "log..txt", "justfile"
    ]

    final_list = []
    pattern = r".*\..*$"

    for filename in filenames:
        if re.fullmatch(pattern, filename):
            tmp_list = filename.split(".")
            ext_str = tmp_list.pop(len(tmp_list)-1) # Pop and store the extension

            tmp_string = ''.join(tmp_list) + '.' + ext_str
            # print(f"{tmp_string}")

            final_list.append(tmp_string)
        else:
            final_list.append(filename)

    print(f"Final list: {final_list}")


if __name__ == '__main__':
    q5()

