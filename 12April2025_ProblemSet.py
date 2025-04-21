"""
### ✅ **1. Scenario: Bug Tracker – Normalize Priority Tags**

**Context**:
In your company’s bug tracker, priority tags come in inconsistent formats like `"High"`, `"high"`, `"HIGH"`, etc.
You’re tasked with writing a utility that converts all priority tags in a list to lowercase for normalization.

**Task**:
Write a function that converts all strings in a list to lowercase.

"""
import re


def q1():
    priority_tags = [
        "High", "MEDIUM", "low", "CRITICAL", "high", "Medium", "LOW", "Normal"
    ]

    # Expected Output:
    # ["high", "medium", "low", "critical", "high", "medium", "low", "normal"]

    final_list = [tag.lower() for tag in priority_tags]

    print(f"Final list 2: {final_list}")



"""
### ✅ **2. Scenario: IoT Data Stream – Identify Out-of-Range Temperatures**

**Context**:
Your IoT temperature sensors stream hourly readings from devices deployed across a warehouse. Any reading **below 10°C
or above 40°C** is considered **out of range** and should be flagged.

**Task**:
Given a list of temperature readings, return the ones that are out of range.

"""
def q2():
    temperature_readings = [
        9.5, 15.0, 41.2, 10.0, 39.9, 8.9, 40.0, 42.5, 30.0, 5.0
    ]

    # Out of range: <10 or >40
    # Expected Output:
    # [9.5, 41.2, 8.9, 42.5, 5.0]

    irregular_readings = [reading for reading in temperature_readings if reading < 10 or reading > 40]

    print(f"Irregular readings: {irregular_readings}")


"""

### ✅ **3. Scenario: HR Email Filter – Check if Subject Line Starts with “URGENT”**

**Context**:
You’re working on an HR email monitoring tool that flags subject lines starting with `"URGENT"` (case-insensitive) for
high-priority handling. These should be detected and forwarded.

**Task**:
Write a function that checks if a subject line starts with `"URGENT"`.

"""
def q3():
    subject_lines = [
        "URGENT: Security patch required",
        "urgent meeting with CEO",
        "Re: Urgent issue escalation",
        "Follow-up on Q3 goals",
        "URGENTLY needed resources",
        "URGENT request for approvals",
        "Reminder: URGENT call at 5PM"
    ]

    # Expected Matches (must **start with** "URGENT" case-insensitive):
    # ["URGENT: Security patch required", "urgent meeting with CEO", "URGENT request for approvals"]

    pattern = r"^urgent.*"

    req_list = []

    for subject in subject_lines:
        if re.fullmatch(pattern, subject.lower()):
            req_list.append(subject)

    print(f"Required list: {req_list}")


"""

### ✅ **4. Scenario: Dev Dashboard – Count Unique Service Names**

**Context**:
Your DevOps dashboard displays metrics for microservices by name. Due to repeated entries in logs, the same service may
appear multiple times. You need to count how many **unique service names** were deployed today.

**Task**:
Write a function that returns the count of unique strings in a list.

"""
def q4():
    service_names = [
        "auth-service", "payment-service", "user-service",
        "auth-service", "reporting", "analytics",
        "user-service", "auth-service", "logging"
    ]

    # Unique services: auth-service, payment-service, user-service, reporting, analytics, logging
    # Expected Output: 6

    unique_services = len(set(service_names))
    print(f"Number of unique services: {unique_services}")


"""
### ✅ **5. Scenario: Chat Assistant – Remove All Digits from User Input**

**Context**:
To prevent accidental leakage of phone numbers or IDs, your chat assistant is configured to **strip all numeric digits**
 from incoming messages before processing them.

**Task**:
Write a function that removes all digits from a given string.

"""
def q5():
    user_messages = [
        "Call me at 9876543210",
        "My ID is 1234ABC567",
        "No digits here!",
        "Date of birth: 12-08-1990",
        "Room 101, Floor 5",
        "OTP is 8942, use quickly"
    ]

    # Expected Output:
    # [
    #   "Call me at ",
    #   "My ID is ABC",
    #   "No digits here!",
    #   "Date of birth: --",
    #   "Room , Floor ",
    #   "OTP is , use quickly"
    # ]
    pattern = r"\d.*$"
    final_list = []

    for msg in user_messages:
        tmp_msg_list = msg.split()
        tmp_list = []

        for word in tmp_msg_list:
            if re.fullmatch(pattern, word):
                # print(f"Number found: {word}")
                continue
            else:
                tmp_list.append(word)

        final_string = ' '.join(tmp_list)
        final_list.append(final_string)

    print(f"Final list: {final_list}")


if __name__ == '__main__':
    q5()

