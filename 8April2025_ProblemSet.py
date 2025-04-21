"""
### ✅ **1. Scenario: User Profile Cleaner – Remove Empty Fields**

**Context**:
In a user profile management tool, some fields (like `middle_name`, `bio`, `nickname`) are left blank or contain only spaces.
Before saving the profile, you need to filter out all **empty or whitespace-only values** from a list of strings.

**Task**:
Write a function that removes all empty or whitespace-only strings from a list.

"""
import re


def q1():
    profile_fields = [
        "John",  # Valid
        "   ",  # Whitespace only
        "Doe",  # Valid
        "",  # Empty string
        "john.doe@example.com",  # Valid
        "    ",  # Whitespace only
        "Engineer",  # Valid
        "\n",  # Newline character (treated as whitespace)
        "   QA Lead  ",  # Has extra spaces, but not empty
        "\t",  # Tab character (whitespace)
    ]

    final_list = []

    for profile in profile_fields:
        profile = profile.strip()

        if profile != "":
            final_list.append(profile)

    print(f"Final list: {final_list}")


"""

### ✅ **2. Scenario: CSV Data Importer – Find the Maximum Value in a Column**

**Context**:
You're importing numeric data from a CSV file into a data warehouse. You want to identify the **maximum value** in a
column before transformation. The values are stored in a list of integers or floats.

**Task**:
Write a function that returns the maximum value from a list of numbers.

"""
def q2():
    numeric_values = [
        75, 103, 89, 150.5, 42, 99, 150.5, 88.75, 145
    ]

    # Expected Output: 150.5

    current_max = 0

    for value in numeric_values:
        if value > current_max:
            current_max = value

    print(f"Max value: {current_max}")


"""

### ✅ **3. Scenario: Internal Tool – Detect Duplicate File Names**

**Context**:
In your company’s internal file management system, files uploaded by users can have duplicate names. You want to identify
 and return all file names that appear **more than once** in the uploaded list.

**Task**:
Write a function that returns a list of file names that appear multiple times.

"""
def q3():
    uploaded_files = [
        "invoice.pdf",
        "profile.jpg",
        "document.docx",
        "invoice.pdf",  # Duplicate
        "image1.png",
        "notes.txt",
        "profile.jpg",  # Duplicate
        "image2.png",
        "presentation.pptx"
    ]

    # Expected Output: ["invoice.pdf", "profile.jpg"]

    traversed_set = set()
    duplicate_set = set()

    for file_name in uploaded_files:
        if file_name in traversed_set:
            duplicate_set.add(file_name)
        else:
            traversed_set.add(file_name)

    print(f"Duplicate files: {list(duplicate_set)}")



"""

### ✅ **4. Scenario: Access Control System – Validate User ID Format**

**Context**:
User IDs in your system must follow this rule:
- Start with `"user_"`, followed by **exactly 4 digits**

You need to validate whether a given user ID string matches this format.

**Task**:
Write a function that checks if a user ID is valid.

"""
def q4():
    user_ids = [
        "user_1234",  # Valid
        "user_12",  # Invalid (only 2 digits)
        "admin_1234",  # Invalid (wrong prefix)
        "user_12345",  # Invalid (5 digits)
        " user_5678 ",  # Invalid unless trimmed first
        "user_0001",  # Valid
        "USER_9999",  # Invalid if case-sensitive
        "user_12a4"  # Invalid (contains letter)
    ]

    final_dict = {}

    pattern = r"^user_\d{4}$"

    for usr_id in user_ids:
        if re.fullmatch(pattern, usr_id):
            final_dict[usr_id] = "Valid"
        else:
            final_dict[usr_id] = "Invalid"

    print(f"Required dict: {final_dict}")


"""

### ✅ **5. Scenario: Chat Bot Profanity Filter – Replace Banned Words**

**Context**:
You’re working on a chatbot used in a customer-facing portal. You need to scan each message and replace all **banned words**
 with `"***"` before it is displayed publicly.

**Task**:
Given a message string and a list of banned words, replace each occurrence of a banned word with `"***"`
(case-insensitive match).

"""
def q5():
    banned_words = ["damn", "idiot", "stupid"]

    messages = [
        "That was a damn good match!",  # Contains "damn"
        "Don't be an idiot about it.",  # Contains "idiot"
        "I think that’s a stupid idea.",  # Contains "stupid"
        "No bad words here.",  # Clean
        "You're not an IDIOT, just misinformed.",  # Case-insensitive match
        "The stupidest thing is calling someone stupid"  # Multiple matches
    ]

    # Expected Output:
    # [
    #   "That was a *** good match!",
    #   "Don't be an *** about it.",
    #   "I think that’s a *** idea.",
    #   "No bad words here.",
    #   "You're not an ***, just misinformed.",
    #   "The ***est thing is calling someone ***"
    # ]

    for message in messages:
        tmp_list = []
        final_list = []

        tmp_list = message.split()

        for word in tmp_list:

            if word in banned_words:
                final_list.append("***")
            else:
                final_list.append(word)

        final_string = ' '.join(final_list)
        print(f"Final string: {final_string}")



if __name__ == '__main__':
    q5()


