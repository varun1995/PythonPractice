def concept1():
    """
    Unpacking
    :return:
    """
    # Basic unpacking
    a,b,c = [1,2,3]
    print(f"a:{a}, b: {b}, c:{c}")

    # Extended iterable unpacking with *
    a,*b,c = [12,13,14,15,16,17]

    print(f"a:{a}, b:{b}, c:{c}")

    # Ignoring values '_' anonymous variable
    a, _, c = [1,2,3]

    # Unpacking nested structures
    data = ("Alice", (25, "Engineer"))
    name, (age, profession) = data

    print(f"Hi, I am {name}, {age} years old and an {profession}")

    # Unpacking in function arguments
    def print_names(*names):
        for fname in names:
            print(fname)

    print_names("Alice", "Bob", "Charlie","Darryl")

    # Combining lists with unpacking *
    list1 = [1,2,3]
    list2 = [4,5,6]
    list3 = [6,7,8]

    final_list = [*list1, *list2, *list3]
    print(f"{final_list}")

    print("Elements of list2: ", *list2)

    # Combining dicts with unpacking **
    dict1 = {"a":1, "b":2}
    dict2 = {"c":3, "d":4}

    final_dict = {**dict1, **dict2}
    print(f"Combined dict: {final_dict}")

    # Inline swap using unpacking!
    x = 10
    y = 20

    print(f"Before swapping: x:{x}, y:{y}")

    x, y = y, x

    print(f"After swapping: x:{x}, y:{y}")

"""
Q1: Basic Unpacking – Assign values from a tuple to variables

Task:
Unpack a tuple of three values into variables `x`, `y`, and `z`.

Test Data:
coordinates = (10, 20, 30)
Expected: x = 10, y = 20, z = 30
"""
def q1():
    coordinates = (10, 20, 30)

    x, y, z = coordinates

    print(f"Unpacked variables: {x}, {y}, {z}")

"""
Q2: Extended Unpacking – Capture middle elements with *

Task:
Unpack the first and last name, and store any middle names in a list using *.

Test Data:
full_name = ["John", "Jacob", "Jingleheimer", "Smith"]
Expected: first = "John", middle = ["Jacob", "Jingleheimer"], last = "Smith"
"""
def q2():
    full_name = ["John", "Jacob", "Jingleheimer", "Smith"]

    first, *middle, last = full_name

    print(f"First name: {first}, Middle name: {middle}, Last name: {last}")


"""
Q3: Ignore Values – Use _ to skip unneeded elements

Task:
Unpack a 4-element list, keeping only the first and last values.

Test Data:
data = [100, 200, 300, 400]
Expected: first = 100, last = 400
"""
def q3():
    data = [100, 200, 300, 400]

    first, _, _, last = data

    print(f"First: {first}, Last: {last}")

"""
Q4: Nested Structure Unpacking – Destructure within destructure

Task:
Unpack the given employee record to extract name, age, and city.

Test Data:
employee = ("Alice", (30, "New York"))
Expected: name = "Alice", age = 30, city = "New York"
"""
def q4():
    employee = ("Alice", (30, "New York"))

    name, (age, city) = employee

    print(f"My name is {name}, I am {age} years old and I live in {city}")

"""
Q5: Function Argument Unpacking – Use *args

Task:
Define a function that prints all the car brands passed to it using *args.

Test Data:
brands = ["Toyota", "Honda", "BMW"]
Expected: Output each brand on a new line
"""
def q5():
    brands = ["Toyota", "Honda", "BMW"]

    def print_brands(*brand):
        for brand in brands:
            print(f"{brand}")

    print_brands(brands)

"""
Q6: List Merging – Combine multiple lists using *

Task:
Combine three lists into a single list using unpacking.

Test Data:
a = [1, 2], b = [3, 4], c = [5, 6]
Expected Output: [1, 2, 3, 4, 5, 6]
"""
def q6():
    a = [1, 2]
    b = [3, 4]
    c = [5, 6]

    final_list = [*a, *b, *c]

    print(f"Final list: {final_list}")

"""
Q7: Dictionary Merging – Combine two dicts using **

Task:
Merge dict1 and dict2 using unpacking.

Test Data:
dict1 = {"x": 1}, dict2 = {"y": 2}
Expected Output: {"x": 1, "y": 2}
"""
def q7():
    dict1 = {"x": 1}
    dict2 = {"y": 2}

    combined_dict = {**dict1, **dict2}

    print(f"Combined dict: {combined_dict}")

"""
Q8: Print List Elements Inline – Use * in function call

Task:
Print all elements of the list `nums` on the same line using unpacking.

Test Data:
nums = [10, 20, 30, 40]
Expected Output: 10 20 30 40
"""
def q8():
    nums = [10, 20, 30, 40]

    print(*nums)

"""
Q9: Inline Swapping – Swap two values using unpacking

Task:
Swap `a` and `b` without using a third variable.

Test Data:
a = 5, b = 10
Expected: a = 10, b = 5
"""
def q9():
    a = 5
    b = 10

    print(f"Before swapping: a = {a}, b = {b}")

    a, b = b, a

    print(f"After swapping: a = {a}, b = {b}")

"""
Q10: Starred Unpacking with Multiple Iterables – Advanced merge

Task:
Merge three lists and extract the first item, middle chunk, and last item using unpacking.

Test Data:
data = [100, 200, 300, 400, 500, 600]
Expected: first = 100, middle = [200, 300, 400, 500], last = 600
"""
def q10():
    data = [100, 200, 300, 400, 500, 600]

    first, *middle, last = data

    print(f"First: {first}, Middle: {middle}, Last: {last}")


if __name__ == '__main__':
    # concept1()
    q10()









