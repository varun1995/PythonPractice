
def q1():
    """
    ### ✅ **1. Scenario: Bug Tracker – Reverse Ticket IDs**

    **Context**:
    You’re working on a utility that obfuscates ticket IDs before sending them to external clients.
    The system requires each alphanumeric ticket ID to be **reversed** before transmission, as part of a
    lightweight transformation layer.

    **Task**:
    Write a function that takes a string (ticket ID) and returns it reversed.
    """
    usr_string = "abcd"

    new_string = usr_string[::-1]

    print(f"Reversed string:{new_string}")

def q2():
    """
    ### ✅ **2. Scenario: Data Cleaning – Remove Repetitive Metrics**

    **Context**:
    You’re processing performance test results from an API monitoring tool. Due to retry logic, some entries were
    logged multiple times. You need to clean the metric list so it contains **only unique values**,
    retaining only **first occurrences**.

    **Task**:
    Write a function that removes duplicate entries from a list but **preserves the original order**.
    """
    api_metrics = [
        "200 OK",  # normal response
        "Timeout",  # transient failure
        "200 OK",  # duplicate
        "500 Internal Error",  # server failure
        "Timeout",  # duplicate
        "403 Forbidden",  # auth failure
        "200 OK",  # duplicate
        "500 Internal Error"  # duplicate
    ]

    traversed_ele = list()
    dup_ele = set()

    for ele in api_metrics:
        if ele in traversed_ele:
            dup_ele.add(ele)
        else:
            traversed_ele.append(ele)

    print(f"The list without duplicates: {traversed_ele}")


def q3():
    """
    ### ✅ **3. Scenario: Search Auto-Correct – Anagram Checker**

    **Context**:
    In a search module for your company’s knowledge base, you’ve added an “auto-correct” feature.
    To improve results, you want to **suggest alternate spellings** only if they are anagrams of the input keyword.

    **Task**:
    Write a function that returns whether two strings are anagrams of each other.

    Anagram condition:
    - same length string with just the characters re-arranged

    """
    test_pairs = [
        ("search", "resach"),  # ✅ Valid anagram
        ("service", "iceserv"),  # ✅ Valid anagram
        ("query", "requy"),  # ✅ Valid anagram
        ("API", "PAI"),  # ✅ Valid anagram (if case-insensitive)
        ("database", "base data"),  # ❌ Not an anagram due to space (depends on whether spaces are ignored)
        ("backend", "frontend"),  # ❌ Not an anagram
        ("system", "system"),  # ✅ Valid anagram (word is the same)
        ("login", "loginn"),  # ❌ Not an anagram (extra character)
        ("Cloud", "loudc"),  # ✅ Valid anagram (if case-insensitive)
        ("test", "tess"),  # ❌ Not an anagram (different letter counts)
    ]

    for pair in test_pairs:
        if sorted(pair[0].lower()) == sorted(pair[1].lower()):
            print("Anagram")
        else:
            print("Not an anagram!")


def q4():
    """
    ### ✅ **4. Scenario: Metadata Sanitization – Count Unique Words**

    **Context**:
    You’re building a metadata analysis tool for product descriptions in an e-commerce platform.
    Before tagging, you need to **count how many unique words** are present in the cleaned-up description string.

    **Task**:
    Write a function that returns the count of unique words in a given sentence string.

    1. Split the string into words
    2. Read through the list of words
    3. If it is unique, store in a different list
    4. If it is not, store in a different list
    """
    product_descriptions = [
        "Premium quality leather wallet with RFID protection",  # Normal case
        "Elegant wooden wooden dining table set with chairs",  # Contains duplicate word 'wooden'
        "  Lightweight  and   durable    suitcase for travel  ",  # Irregular spacing
        "Discounted smartphone with fast fast charging support",  # Duplicate word 'fast'
        "",  # Empty description
        "High-end gaming laptop",  # All unique words
        "Noise-cancelling wireless wireless headphones",  # Duplicate word 'wireless'
        "Limited-edition",  # Single word with hyphen
        "256GB SSD 512GB SSD 1TB HDD storage combo",  # Contains numbers and storage sizes
    ]

    for desc in product_descriptions:
        dup_words = set()
        traversed_words = set()

        if desc != "":
            str_list = desc.split()
            # print(str_list)

            for word in str_list:
                if word.lower() in traversed_words:
                    traversed_words.remove(word)
                else:
                    traversed_words.add(word)

            print(f"Unique words: {traversed_words}")
            print(f"Count of unique words: {len(traversed_words)}")
        else:
            print("Empty description!")


def q5():
    """
    ### ✅ **5. Scenario: Alert System – Find Most Frequent Log Type**

    **Context**:
    Your logging framework captures logs from distributed services.
    You need to build a utility that finds the **most frequently occurring log message type**, so you can prioritize alerts.

    **Task**:
    Given a list of log message strings, return the one that occurs the most number of times.

    1. Split the string according to log type.
    2. Create a key value pair to track the number of times a certain log type occurs
    3. Return log type with max value

    """
    log_entries = [
        "INFO User login successful",  # INFO
        "ERROR Database connection failed",  # ERROR
        "INFO Session token generated",  # INFO
        "WARNING Disk usage at 85%",  # WARNING
        "INFO User logout successful",  # INFO
        "ERROR Timeout during data fetch",  # ERROR
        "WARNING CPU temperature high",  # WARNING
        "INFO Scheduled backup completed",  # INFO
        "DEBUG Cache refresh triggered",  # DEBUG
        "ERROR User data validation failed",  # ERROR
        "INFO User password changed",  # INFO
    ]

    count_dict = {}

    for log in log_entries:
        log_str_list = log.lower().split()

        log_key = log_str_list[0]

        if log_key in count_dict:
            count_dict[log_key] += 1
        else:
            count_dict[log_key] = 1

    for key, value in count_dict.items():
        print(f"{key} : {value}")

    max_key = max(count_dict, key=count_dict.get)
    print(f"Max value: {max_key} : {count_dict[max_key]}")



if __name__ == '__main__':
    q5()

