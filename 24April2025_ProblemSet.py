"""
### ✅ **1. Scenario: Subscription Platform – Remove Trailing Zeros from Decimal Prices**

**Task**:
You receive price strings from a third-party billing API like `"49.00"`, `"19.90"`, `"25.50"`. Your UI team wants to
display them cleanly by removing any **trailing zeros after the decimal point** (e.g., `"49.00"` → `"49"`, `"19.90"` → `"19.9"`).

Strategy:
1. Split each string based on "."
2. If the trailing part % 10 == 0 => slice it
3. Else append it and create final string
"""
def q1():
    price_inputs = ["49.00", "19.90", "25.50", "100.01", "33.99", "75.0", "101.10010"]
    # Expected Output:
    # ["49", "19.9", "25.5", "100.01", "33.99", "75"]

    final_list = []

    for price in price_inputs:
        tmp_price_list = price.split(".") # ['49','00']
        print(f"{tmp_price_list}")

        if int(tmp_price_list[1]) % 10 == 0:
            condition_1_quotient = int(tmp_price_list[1]) // 10

            tmp_string = str(tmp_price_list[0]) + '.' + str(condition_1_quotient)
            final_list.append(tmp_string)
        else:
            tmp_string = '.'.join(tmp_price_list)
            final_list.append(tmp_string)

    print(f"Final required list: {final_list}")


"""

### ✅ **2. Scenario: Monitoring Agent – Detect Repeating CPU Usage Patterns**

**Task**:  
You’re analyzing CPU load data recorded every minute. Your script should detect if **any value appears more than once**
 (i.e., pattern repeat) in the list.

"""
def q2():
    cpu_usages = [
        [45, 60, 70, 80, 60, 90],  # 60 repeats
        [10, 20, 30, 40, 50],  # all unique
        [99, 99, 99],  # repeated multiple times
        []  # empty list
    ]
    # Expected Output:
    # [True, False, True, False]
    final_list = []

    for data in cpu_usages:
        traversed_set = set()
        duplicate_set = set()

        for ele in data:
            if ele in traversed_set:
                duplicate_set.add(ele)
            else:
                traversed_set.add(ele)

        if len(duplicate_set) == 0:
            final_list.append("False") # All unique elements
        else:
            final_list.append("True")

    print(f"Final list: {final_list}")



"""

### ✅ **3. Scenario: Survey Response Cleaner – Collapse Multiple Spaces to One**

**Task**:  
Users fill out text fields in surveys, often typing with excessive spaces. Normalize strings by collapsing **all 
multiple spaces into a single space**, and also **strip leading/trailing spaces**.

"""
def q3():
    survey_inputs = [
        "I   love     this product  ",
        "   Very  useful tool!   ",
        "Multiple     spaces     here",
        "Already clean",
        ""
    ]
    # Expected Output:
    # ["I love this product", "Very useful tool!", "Multiple spaces here", "Already clean", ""]

    final_list = []

    for usr_input in survey_inputs:
        usr_input = usr_input.strip()

        if usr_input != "":
            tmp_list = usr_input.split(" ")
            # print(f"{tmp_list}")

            tmp_str_list = [ele for ele in tmp_list if ele != '']
            final_string = ' '.join(tmp_str_list)
            # print(f"{final_string}")

            final_list.append(final_string)
        else:
            final_list.append("")

    print(f"Final list: {final_list}")


"""

### ✅ **4. Scenario: File Sync – Compare File Lists Case-Insensitively**

**Task**:  
You're syncing files between platforms. Compare two lists of filenames and return the ones that **exist in both**, 
ignoring case.

"""
def q4():
    local_files = ["report.docx", "data.csv", "summary.pdf", "Invoice.PDF"]
    remote_files = ["REPORT.DOCX", "Data.csv", "invoice.pdf", "README.md"]
    # Expected Output:
    # ["report.docx", "data.csv", "Invoice.PDF"]

    local_files_lc = [ele.lower() for ele in local_files]
    print(f"Local files: {local_files_lc}")

    remote_files_lc = [ele.lower() for ele in remote_files]
    print(f"Remote files: {remote_files_lc}")

    trav_set = set()
    dup_set = set()

    for file_name in local_files_lc:
        if file_name in remote_files_lc:
            dup_set.add(file_name)
        else:
            trav_set.add(file_name)

    print(f"Required list: {list(dup_set)}")

"""
### ✅ **5. Scenario: Workflow Engine – Extract Keys from Condition String**

**Task**:  
You’re parsing workflow conditions like: `"user.age > 18 and user.country == 'US'"`. Extract all **dot-separated keys** 
before any comparison or operator.

"""
import re
def q5():
    conditions = [
        "user.age > 18 and user.country == 'US'",
        "session.duration >= 30 or session.device == 'mobile'",
        "event.status != 'failed'",
        "no.operators"
    ]
    # Expected Output:
    # [
    #   ["user.age", "user.country"],
    #   ["session.duration", "session.device"],
    #   ["event.status"],
    #   ["no.operators"]
    # ]

    pattern = r"[a-zA-Z]+\.[a-zA-Z]+" # \. => matches literal dot
    final_list = []

    for condition in conditions:
        match = re.findall(pattern, condition)

        if match:
            final_list.append(match)

    print(f"Final list: {final_list}")


if __name__ == '__main__':
    q5()


