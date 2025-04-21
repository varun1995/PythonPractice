"""
### ✅ **1. Scenario: Billing Dashboard – Filter Zero-Value Transactions**

**Context**:
In your company's billing system, a few transactions are recorded with `0.0` amount due to system tests or voided entries.
 You are building a filter to remove these zero-value entries from the transaction log before displaying the final invoice summary.

**Task**:
Write a function that takes a list of transaction amounts (floats) and returns a list with all `0.0` values removed.

"""
def q1():
    transaction_amounts = [
        1200.50, 0.0, 350.75, 0.0, 875.25, 0.0, 99.99, 1500.00
    ]

    # Expected Output:
    # [1200.50, 350.75, 875.25, 99.99, 1500.00]

    to_delete = 0.0
    final_list = []

    for amount in transaction_amounts:
        if amount == float(to_delete):
            continue
        else:
            final_list.append(amount)

    print(f"Final list of transactions: {final_list}")

"""

### ✅ **2. Scenario: DevOps Audit Tool – Count Status Occurrences**

**Context**:  
You're building an internal audit tool that parses a status report file and counts how many times each status appears 
(e.g., `"PASS"`, `"FAIL"`, `"SKIPPED"`). These status tags are stored in a list of strings.

**Task**:  
Write a function that returns a dictionary with the count of each status label.

"""
def q2():
    status_log = [
        "PASS", "FAIL", "PASS", "SKIPPED", "FAIL", "PASS", "PASS", "SKIPPED", "FAIL", "PASS"
    ]

    # Expected Output:
    # {"PASS": 5, "FAIL": 3, "SKIPPED": 2}

    count_dict = {}

    for status in status_log:
        if status in count_dict:
            count_dict[status] += 1
        else:
            count_dict[status] = 1

    print(f"Count of status: {count_dict}")


"""

### ✅ **3. Scenario: Text Editor Plugin – Convert Snake Case to Camel Case**

**Context**:  
You’re developing a plugin for an internal code editor. The plugin should help developers quickly convert variable names
 from `snake_case` to `camelCase` for better consistency in frontend code.

**Task**:  
Write a function that takes a snake_case string and returns it in camelCase format.

"""
def q3():
    snake_case_inputs = [
        "user_id_for_user_company",  # userId
        "email_address",  # emailAddress
        "access_token",  # accessToken
        "created_at",  # createdAt
        "first_name"  # firstName
    ]

    final_list = []

    for input_val in snake_case_inputs:
        camel_case_string = ""

        split_input_list = input_val.split('_')
        # print(f"Split string: {split_input_list}")

        for index in range(len(split_input_list)):
            if index % 2 != 0:
                split_input_list[index] = split_input_list[index].capitalize()
            else:
                continue

        camel_case_string = ''.join(split_input_list)
        # print(f"Camel case string: {camel_case_string}")

        final_list.append(camel_case_string)

    print(f"Final list: {final_list}")

"""

### ✅ **4. Scenario: Data Ingestion Validation – Check All Elements Are Integers**

**Context**:  
Before ingesting raw data into your analytics platform, a validation step checks that all entries in a dataset are 
**integers only**. If any element is not an integer, it should be flagged.

**Task**:  
Write a function that returns `True` if all elements in a list are integers, otherwise `False`.

"""
def q4():
    test_lists = [
        [1, 2, 3, 4, 5],  # All integers → True
        [1, "2", 3, 4],  # Contains a string → False
        [10, 20, 30.0],  # Contains a float → False
        [],  # Empty list → True (by convention)
        [100, True, 200],  # Contains boolean → Should return True (bool is subclass of int)
    ]

    for ele_list in test_lists:
        count = 0

        for ele in ele_list:
            if isinstance(ele, int):
                count += 1

        if count == len(ele_list):
            print(True)
        else:
            print(False)


"""

### ✅ **5. Scenario: Email Notification System – Extract Subject Lines with Keywords**

**Context**:  
Your system monitors outgoing email subject lines. You need to extract all subjects that **contain a specific keyword** 
(case-insensitive) such as `"invoice"` or `"alert"` from a list of subject strings.

**Task**:  
Write a function that takes a list of subject lines and a keyword, and returns only the matching subjects.

"""
def q5():
    subject_lines = [
        "Invoice generated for March",
        "Alert: Low disk space on server",
        "Meeting Notes - Sprint Planning",
        "Reminder: Submit timesheet",
        "Invoice overdue: Action required",
        "System Alert - CPU usage high",
        "Casual Friday announcement"
    ]

    keyword = "alert"

    final_list = []

    for title in subject_lines:
        title = title.lower()
        tmp_list = title.split()
        # print(tmp_list)
        # tmp_string = ""

        tmp_list = [word.strip('.,:;!?()[]{}') for word in tmp_list]

        # print(tmp_list)

        if keyword in tmp_list:
            tmp_string = ' '.join(tmp_list)
            final_list.append(tmp_string)

    print(f"Final list: {final_list}")


if __name__ == '__main__':
    q5()



