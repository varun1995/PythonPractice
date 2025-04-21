"""
### ✅ **1. Scenario: Config Parser – Count Word Occurrences**

**Context**:
You are developing a lightweight configuration parser for a DevOps tool. As part of parsing free-text fields,
you need to **count how many times each word** appears in a given string. This will be used for log summarization and
configuration analysis.

**Task**:
Write a function that takes a string and returns a dictionary with each word and its count.

#### Q1:
```python
config_text = "enable logging logging error reporting logging enabled"
```

1. Split the string into a list of words.
2. Iterate through the list, count the occurrance of each word as you encounter it.
"""
def q1():
    config_text = "enable logging logging error reporting logging enabled"
    word_count_dict = {}

    list_words = config_text.split()
    print(f"Word list: {list_words}")

    for word in list_words:
        if word in word_count_dict.keys():
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    print(f"Word count dictionary: {word_count_dict}")


"""
### ✅ **2. Scenario: Data Preprocessing – Remove Special Characters**

**Context**:  
Before ingesting product reviews into a text analytics system, you are asked to **sanitize** them by removing all 
special characters (punctuation, symbols, etc.) except alphabets and numbers.

**Task**:  
Write a function that takes a string and returns it after removing all characters except letters and numbers.

#### Q2:
review = "Excellent!! Product -- works @100% well."


Strategy:
1. Create an empty string, empty list
2. Iterate over the entire user string, if the character is a digit/letter, add to the list
    Else ignore the character
   Continue till end of string
3. Once the list if populated, join it back into a string and return it

"""
def q2():
    test_reviews = [
        "Excellent!! Product -- works @100% well.",  # Mixed punctuation and symbols
        "Best-in-class; highly-recommended!!",  # Hyphens and semicolons
        "5 stars ***** worth every penny!!!",  # Repeated special characters
        "Simple & Effective (no-frills).",  # Parentheses and ampersand
        "   ",  # Only spaces
        "",  # Empty string
        "Price: $499, Discount: 20% OFF!",  # Currency symbols and percentage
        "Available NOW!!! Hurry-Up --> Limited_Stock",  # Uppercase, exclamations, arrows, underscores
    ]

    final_list = []

    for review in test_reviews:
        tmp_list = []
        tmp_str = []

        if review.strip() != "":
            for char in review:
                if char.isalnum() or char.isspace():
                    tmp_list.append(char)

            tmp_str = ''.join(tmp_list)
            print(f"String formed: {tmp_str}")

            final_list.append(tmp_str)
        else:
            print(f"Empty string encountered and ignored!")

    print(f"Final list:{final_list}")



"""
### ✅ **3. Scenario: Feature Store – Check if Feature Set is a Subset**

**Context**:  
You are working on a **feature validation** tool. During model training, you need to confirm whether the set of required
 features is actually present in the available feature set exported from the data warehouse.

**Task**:  
Given two lists (required_features and available_features), check if required_features is a subset of available_features.

test_cases = [
    # Case 1: Valid subset
    {
        "required_features": ["age", "salary", "experience"],
        "available_features": ["name", "age", "salary", "experience", "location"]
    },

    # Case 2: Not a subset (missing "education")
    {
        "required_features": ["age", "salary", "education"],
        "available_features": ["age", "salary", "experience", "location"]
    },

    # Case 3: Exact match (both lists are the same)
    {
        "required_features": ["age", "salary", "experience"],
        "available_features": ["age", "salary", "experience"]
    },

    # Case 4: Empty required features (always a subset)
    {
        "required_features": [],
        "available_features": ["age", "salary", "experience", "location"]
    },

    # Case 5: Empty available features (required is non-empty → always False)
    {
        "required_features": ["age"],
        "available_features": []
    },

    # Case 6: Case sensitivity check
    {
        "required_features": ["Age", "Salary"],
        "available_features": ["age", "salary", "experience"]
        # Depending on case sensitivity, this may fail
    }
]

"""
def q3():
    test_cases = [
        # Case 1: Valid subset
        {
            "required_features": ["age", "salary", "experience"],
            "available_features": ["name", "age", "salary", "experience", "location"]
        },

        # Case 2: Not a subset (missing "education")
        {
            "required_features": ["age", "salary", "education"],
            "available_features": ["age", "salary", "experience", "location"]
        },

        # Case 3: Exact match (both lists are the same)
        {
            "required_features": ["age", "salary", "experience"],
            "available_features": ["age", "salary", "experience"]
        },

        # Case 4: Empty required features (always a subset)
        {
            "required_features": [],
            "available_features": ["age", "salary", "experience", "location"]
        },

        # Case 5: Empty available features (required is non-empty → always False)
        {
            "required_features": ["age"],
            "available_features": []
        },

        # Case 6: Case sensitivity check
        {
            "required_features": ["Age", "Salary"],
            "available_features": ["age", "salary", "experience"]
            # Depending on case sensitivity, this may fail
        }]

    for case in test_cases:
        counter = 0

        case_length = len(case["required_features"])
        # print(f"Required features count: {case_length}")

        if case_length == 0:
            print("Is a substring!")
        else:
            for index in range(case_length):
                if case["required_features"][index] in case["available_features"]:
                    counter += 1

            if len(case["required_features"]) == counter:
                print(f"Is a substring!")
            else:
                print(f"Not a substring!")




"""
### ✅ **4. Scenario: Log Processor – Extract Integers from Log Messages**

**Context**:  
Your log processing system needs to extract all the **numbers** embedded inside unstructured log messages. These numbers
 will later be used for monitoring and threshold checks.

**Task**:  
Write a function that returns all the integers present in a given string.

"""
def q4():
    log_messages = [
        "User 123 connected in 42ms after 3 retries.",  # Multiple numbers
        "Session established successfully.",  # No numbers
        "Disk space left: 500 GB, Used: 1500 GB",  # Multiple large numbers
        "Backup completed at 03:15:45",  # Time-like numbers
        "Error code 404 encountered at line 57.",  # Error code + line number
        "CPU load is at 99 percent, temperature is 78 degrees",  # Percentages and temperatures
        "   ",  # Only spaces
        "",  # Empty log message
        "Event ID: EVT-00123",  # Embedded numbers with prefix
        "100% completed in 0 seconds.",  # Zero handling
    ]

    final_list = []

    for log in log_messages:
        tmp_list = []

        for char in log:
            if char.isnumeric():
                tmp_list.append(char)

        final_list.append(tmp_list)

    print(final_list)


"""
### ✅ **5. Scenario: Subscription Service – Validate Email Format**

**Context**:  
You are asked to build an email validation function for a subscription service. The validation must check if the given 
string:
- Has **at least one character** before the `@`
- Has an `@`
- Has at least one `.` after the `@`

**Task**:  
Write a function to verify if the given string is a **valid email format**.

"""
import re

def q5():
    test_emails = [
        "john.doe@example.com",  # Valid
        "user123@company.org",  # Valid
        "alice_smith99@sub.domain.co",  # Valid (subdomain)
        "bob@",  # Invalid (no domain)
        "@example.com",  # Invalid (no local part)
        "carol.example.com",  # Invalid (missing '@')
        "dave@.com",  # Invalid (missing domain name)
        "eve@domain",  # Invalid (missing dot)
        "frank@domain.",  # Invalid (dot at the end)
        "   frank@domain.com   ",  # Valid but may need trimming
        "",  # Invalid (empty string)
        "grace@domain.c"  # Valid (very short TLD, but technically allowed)
    ]

    pattern = r"^[^@]+@[^\s@]+\.[^\s@]+$"

    for email in test_emails:
        if re.fullmatch(pattern, email):
            print("Pattern matched!")
        else:
            print("Pattern not matched!")


if __name__ == '__main__':
    q5()