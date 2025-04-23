"""
### ✅ **1. Scenario: Document Scanner – Extract File Extension**

**Task**:
Write a function that extracts the file extension from a given filename string. If there’s no extension, return an empty
string.

"""
def q1():
    file_names = [
        "report.docx",
        "data.csv",
        "archive.tar.gz",
        "README",
        "image.jpeg",
        "script.py",
        "logfile.",
        "backup"
    ]
    # Expected Output:
    # ["docx", "csv", "gz", "", "jpeg", "py", "", ""]

    final_list = []

    for name in file_names:
        tmp_list = name.split(".")

        if len(tmp_list) > 1:
            final_list.append(tmp_list[len(tmp_list)-1])
        else:
            final_list.append("")

    print(f"Required list: {final_list}")

"""
### ✅ **2. Scenario: System Monitor – Check If All Services Are Up**

**Task**:  
Write a function that returns `True` if all elements in the list are `"up"` (case-insensitive), else `False`.
"""
def q2():
    service_statuses = [
        ["up", "up", "up"],
        ["UP", "Up", "UP"],
        ["up", "down", "up"],
        ["Up", "DOWN", "UP"],
        []
    ]
    # Expected Output:
    # [True, True, False, False, True]

    pattern = "up"
    final_list = []

    for status_list in service_statuses:
        count = 0
        for status in status_list:
            if status.lower() == pattern:
                count += 1
        if count == len(status_list):
            final_list.append("True")
        else:
            final_list.append("False")

    print(f"Final list: {final_list}")


"""

### ✅ **3. Scenario: Chat Cleaner – Remove Special Characters Except Letters and Spaces**

**Task**:  
Write a function that removes all non-alphabetic, non-space characters from a string.
"""
import re
def q3():
    messages = [
        "Hi there! How's it going? :)",
        "User123 logged in @ 10:00AM",
        "*** SYSTEM ALERT ***",
        "Welcome!!!",
        "Normal text"
    ]
    # Expected Output:
    # [
    #   "Hi there Hows it going ",
    #   "User logged in  AM",
    #   " SYSTEM ALERT ",
    #   "Welcome",
    #   "Normal text"
    # ]

    # Regex pattern to find chars that are not chars or spaces.
    pattern = r"[^a-zA-Z ]"

    final_list = []

    for msg in messages:
        tmp_msg = re.sub(pattern, "", msg)
        final_list.append(tmp_msg)

    print(f"Final list: {final_list}")

"""

### ✅ **4. Scenario: API Logger – Group Endpoints by Method**

**Task**:  
Write a function that returns a dictionary where each key is an HTTP method (`GET`, `POST`, etc.), and its 
value is a list of associated endpoints.
"""
def q4():
    api_logs = [
        ("GET", "/users"),
        ("POST", "/login"),
        ("GET", "/status"),
        ("PUT", "/profile"),
        ("POST", "/logout"),
        ("GET", "/metrics")
    ]
    # Expected Output:
    # {
    #   "GET": ["/users", "/status", "/metrics"],
    #   "POST": ["/login", "/logout"],
    #   "PUT": ["/profile"]
    # }

    final_dict = {}

    for method, path in api_logs:

        if method not in final_dict:
            final_dict[method] = []
        else:
            final_dict[method].append(path)

    print(f"Final dict: {final_dict}")


"""

### ✅ **5. Scenario: Feedback Dashboard – Detect Duplicate Comments**

**Task**:  
Write a function that returns a list of duplicate comments (ignoring case).

"""
def q5():
    comments = [
        "Great product!",
        "great product!",
        "Needs improvement.",
        "Excellent work.",
        "NEEDS IMPROVEMENT.",
        "Great product",
        "excellent work.",
        "Excellent Work."
    ]
    # Expected Output:
    # ["great product!", "Needs improvement.", "Excellent work."]
    traversed_set = set()
    duplicate_set = set()

    for comment in comments:
        if comment.lower() in traversed_set:
            duplicate_set.add(comment.lower())
        else:
            traversed_set.add(comment.lower())

    print(f"List of duplicate comments: {list(duplicate_set)}")


if __name__ == '__main__':
    q5()

