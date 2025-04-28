"""
### ✅ **1. Scenario: URL Rewriter – Replace HTTPS with HTTP**

**Task**:
You're building a proxy tool that rewrites all incoming URLs to use `http` instead of `https` for a staging environment.

"""
def q1():
    urls = [
        "https://example.com",
        "http://legacy.site.org",
        "https://secure.portal.net/login",
        "https://docs.python.org"
    ]
    # Expected Output:
    # [
    #   "http://example.com",
    #   "http://legacy.site.org",
    #   "http://secure.portal.net/login",
    #   "http://docs.python.org"
    # ]

    pattern = r"https"

    final_list = []

    for url in urls:
        tmp_list = url.split(":")

        if tmp_list[0] == pattern:
            tmp_list.pop(0)
            tmp_list.insert(0, "http")
            # print(f"{tmp_list}")

        tmp_string = ':'.join(tmp_list)
        final_list.append(tmp_string)

    print(f"Final list: {final_list}")


"""
### ✅ **2. Scenario: Terminal Logger – Count Uppercase Words**

**Task**:  
In a CLI logger, uppercase words (like `ERROR`, `WARN`, `INFO`) signal log severity. You want to count how many **fully 
uppercase words** appear in each log line.

"""
def q2():
    logs = [
        "INFO: Service started successfully",
        "ERROR: Failed to connect to DB",
        "WARN: Disk usage at 90%",
        "Server RESTART scheduled",
        "Everything is fine"
    ]
    # Expected Output:
    # [1, 1, 1, 1, 0]
    count_list = []

    for log in logs:
        count = 0
        word_list = log.split()

        for word in word_list:
            word = word.strip(":%")
            if word.isupper():
                count += 1

        count_list.append(count)

    print(f"Final list: {count_list}")



"""

### ✅ **3. Scenario: Inventory System – Filter Product Codes with Prefix**

**Task**:  
Filter a list of product codes to include only those that start with a given prefix (e.g., `"SKU_"`).

"""
import re
def q3():
    product_codes = [
        "SKU_1234", "sku_5678", "ID_9999", "SKU_0001", "sku_8888"
    ]
    prefix = r"^SKU_.*"
    # Expected Output (case-sensitive):
    # ["SKU_1234", "SKU_0001"]

    final_list = []

    for code in product_codes:
        match = re.search(prefix, code)

        if match:
            final_list.append(match.group())

    print(f"Final list: {final_list}")


"""

### ✅ **4. Scenario: Data Warehouse – Truncate Table Names to 10 Characters**

**Task**:  
Your data pipeline requires that all table names be a maximum of 10 characters. You need to truncate each name accordingly.

"""
def q4():
    table_names = [
        "transactions", "user_profiles", "logs", "data_snapshot", "raw"
    ]
    # Expected Output:
    # ["transactio", "user_profi", "logs", "data_snaps", "raw"]

    final_list = []

    for name in table_names:
        count = 0
        tmp_list = []

        for char in name:
            count += 1

            if count <= 10:
                tmp_list.append(char)

        tmp_str = ''.join(tmp_list)

        final_list.append(tmp_str)

    print(f"Final list: {final_list}")

"""

### ✅ **5. Scenario: Text Search – Find All Words Containing “cat”**

**Task**:  
In a document indexer, you want to extract all words that **contain the substring `"cat"`**, regardless of case.

"""
import re
def q5():
    sentences = [
        "The category of this catalog is catastrophic.",
        "Catch the caterpillar!",
        "Dogs are not included.",
        "Concatenation is a fancy word.",
        "A CAT walked across the roof."
    ]
    # Expected Output:
    # [
    #   ["category", "catalog", "catastrophic"],
    #   ["Catch", "caterpillar"],
    #   [],
    #   ["Concatenation"],
    #   ["CAT"]
    #  ]

    pattern = r"\w*cat\w*"
    final_list = []

    for sentence in sentences:
        matches = re.findall(pattern=pattern, string=sentence, flags=re.IGNORECASE)

        print(f"Match list: {matches}")
        final_list.append(matches)

    print(f"Final list: {final_list}")


if __name__ == '__main__':
    q5()


