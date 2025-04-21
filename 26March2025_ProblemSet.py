"""
---

### ✅ **1. Scenario: Bug Tracker – Reverse Ticket IDs**

**Context**:
You’re working on a utility that obfuscates ticket IDs before sending them to external clients.
The system requires each alphanumeric ticket ID to be **reversed** before transmission, as part of a
lightweight transformation layer.

**Task**:
Write a function that takes a string (ticket ID) and returns it reversed.

---

### ✅ **2. Scenario: Data Cleaning – Remove Repetitive Metrics**

**Context**:
You’re processing performance test results from an API monitoring tool. Due to retry logic, some entries were
 logged multiple times. You need to clean the metric list so it contains **only unique values**,
 retaining only **first occurrences**.

**Task**:
Write a function that removes duplicate entries from a list but **preserves the original order**.

---

### ✅ **3. Scenario: Search Auto-Correct – Anagram Checker**

**Context**:
In a search module for your company’s knowledge base, you’ve added an “auto-correct” feature.
To improve results, you want to **suggest alternate spellings** only if they are anagrams of the input keyword.

**Task**:
Write a function that returns whether two strings are anagrams of each other.

---

### ✅ **4. Scenario: Metadata Sanitization – Count Unique Words**

**Context**:
You’re building a metadata analysis tool for product descriptions in an e-commerce platform.
Before tagging, you need to **count how many unique words** are present in the cleaned-up description string.

**Task**:
Write a function that returns the count of unique words in a given sentence string.

---

### ✅ **5. Scenario: Alert System – Find Most Frequent Log Type**

**Context**:
Your logging framework captures logs from distributed services.
You need to build a utility that finds the **most frequently occurring log message type**, so you can prioritize alerts.

**Task**:
Given a list of log message strings, return the one that occurs the most number of times.

---
"""