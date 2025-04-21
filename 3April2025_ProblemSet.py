"""

### ✅ **1. Scenario: Reporting Tool – Format Float to 2 Decimal Places**

**Context**:
You are building a reporting utility for your company's finance dashboard. All monetary values must be
displayed with exactly **2 decimal places**, even if they are whole numbers.

**Task**:
Write a function that takes a float and returns it formatted as a string rounded to two decimal places.

"""


def q1():
    monetary_values = [
        125.5,  # Normal float with 1 decimal place
        99.999,  # Float with more than 2 decimal places
        50.0,  # Float with .0
        100,  # Integer (should still show as 100.00)
        0.1,  # Less than 1
        0.0,  # Exactly zero
        1234567.89123  # Large number with multiple decimal places
    ]

    updated_values = []

    for value in monetary_values:
        decimal_number = f"{value:.2f}"
        updated_values.append(decimal_number)

    print(f"Required values: {updated_values}")


"""

### ✅ **2. Scenario: ETL Pipeline – Replace Specific Words in Text**

**Context**:  
During text normalization in an ETL pipeline, you need to replace certain **restricted keywords** with a placeholder 
word `"REDACTED"` before storing data in the data lake.

**Task**:  
Given a string and a list of restricted words, replace all occurrences of those words with `"REDACTED"`.

"""
def q2():
    test_texts = [
        "The project is confidential and the budget is confidential too.",  # Multiple occurrences of the word
        "This document is classified and restricted.",  # Multiple restricted words
        "Normal operational data with no sensitive content.",  # No restricted words
        "classified classified classified",  # Only restricted words
        "",  # Empty string
        "The quick brown fox jumps over the lazy dog.",  # Irrelevant sentence with no match
    ]

    restricted_words = ["confidential", "classified", "restricted"]
    required_word = "REDACTED"

    final_list = []

    for text_str in test_texts:

        text_str = text_str.rstrip('.') # Removing the full stop at the end of a processed string

        if text_str.strip() != "":
            text_str_list = text_str.split()
            # print(text_str_list)
            tmp_stack = []

            for word in text_str_list:
                if word in restricted_words:
                    tmp_stack.append(required_word)
                else:
                    tmp_stack.append(word)

            redacted_string = ' '.join(tmp_stack)
            print(f"{redacted_string}")

            final_list.append(redacted_string)
        else:
            print(f"Cannot process empty string!")

"""

### ✅ **3. Scenario: User Registration – Validate Phone Numbers**

**Context**:  
You are working on a user onboarding system. Phone numbers must:
- Contain **exactly 10 digits**
- Not contain **letters** or **special characters**
- Optionally allow **spaces** which should be ignored during validation

**Task**:  
Write a function to validate if a phone number string meets these conditions.

"""
import re

def q3():
    phone_numbers = [
        "1234567890",  # Valid (exactly 10 digits)
        "123 456 7890",  # Valid (spaces allowed)
        "123-456-7890",  # Invalid (special character '-')
        "123456789",  # Invalid (only 9 digits)
        "12345678901",  # Invalid (11 digits)
        "12345abc90",  # Invalid (contains letters)
        "  0987654321   ",  # Valid (spaces around the number)
        "",  # Invalid (empty string)
        "0000000000",  # Valid (edge case: all zeros)
        "12 34 56 78 90",  # Valid (spaces spread out)
    ]

    # pattern = r"^[0-9\s]+$"
    pattern = r"\d{10}"

    for number in phone_numbers:

        number = number.strip().replace(" ", "") # Removing whitespaces at all places in the string

        if number != "" and re.fullmatch(pattern, number):
            if len(number) == 10:
                print("Valid string!")
        else:
            print("Invalid string!")


"""

### ✅ **4. Scenario: Log Analyzer – Extract Domain from URL**

**Context**:  
In your log analysis tool, you need to extract just the **domain name** (without `http`, `https`, or path) 
from URLs logged by the webserver.

**Task**:  
Given a URL string, return the domain name.

"""
def q4():
    url_samples = [
        "https://www.example.com/path/to/page?query=123",  # Standard HTTPS URL
        "http://example.org",  # Simple HTTP URL
        "https://subdomain.company.co.in/resource?id=789",  # Subdomain with country-code TLD
        "ftp://fileserver.com/files",  # Non-HTTP scheme (optional if your logic restricts to HTTP/HTTPS)
        "https://example.com/",  # Domain with trailing slash
        "www.testsite.net/home",  # Missing scheme
        "testsite.net",  # Bare domain
        "   https://whitespace.com   ",  # Leading and trailing spaces
        "",  # Empty string
        "https://192.168.1.1/admin",  # IP address as domain
    ]

    final_list = []

    for url in url_samples:
        url = url.strip()

        if url != "":
            first_strip_list = url.split('//')
            # print(first_strip_list)

            if len(first_strip_list) > 1:
                domain_raw = first_strip_list[1]

                domain_raw_strip_list = domain_raw.split('/')
                # print(domain_raw_strip_list)

                final_list.append(domain_raw_strip_list[0])

            else:
                domain_raw2 = first_strip_list[0]
                domain_raw_strip_list2 = domain_raw2.split('/')
                # print(domain_raw_strip_list2)

                final_list.append(domain_raw_strip_list2[0])
        else:
            pass

    print(f"Required list: {final_list}")


"""

### ✅ **5. Scenario: API Gateway – Sort and Deduplicate Request IDs**

**Context**:  
You are analyzing a list of API request IDs received in logs. Your goal is to:
- Remove duplicate IDs
- Sort them in ascending order

**Task**:  
Given a list of integers representing request IDs, return the sorted list with duplicates removed.

"""
def q5():
    request_ids_samples = [
        [102, 501, 102, 304, 501, 709, 120],  # Normal case with duplicates
        [1, 1, 1, 1],  # All elements are the same
        [500, 300, 200, 100],  # Already sorted in descending order
        [42],  # Single request ID
        [],  # Empty list
        [9, 7, 5, 5, 7, 3, 1],  # Mixed duplicates, unsorted
        [1000, 999, 1001, 1001, 999, 1002],  # Larger numbers with duplicates
        [0, 0, 0, 0],  # All zeros
    ]

    final_list = []

    for request in request_ids_samples:
        final_req = sorted(list(set(request)))
        final_list.append(final_req)

    print(f"Final list:{final_list}")

if __name__ == '__main__':
    q5()
