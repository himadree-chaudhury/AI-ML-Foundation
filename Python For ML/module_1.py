#  Python does not require a semicolon at the end of each line. It uses indentation to define code blocks.
# *Data Types: In Python all are class objects
#  int, float, str, list, tuple, dict, set, bool
#  e.g., x = 5 (int), y = 3.14 (float), name = "Alice" (str), is_active = True (bool)
print(type(5))          # <class 'int'>

# *Built in data structures: Tons of built-in data structures in Python
#  list: ordered, mutable, allows duplicates
my_list = [1, 2, 3, 4, 5]
#  tuple: ordered, immutable, allows duplicates
my_tuple = (1, 2, 3, 4, 5)
#  dict: unordered, mutable, key-value pairs
my_dict = {"name": "Alice", "age": 30}
#  set: unordered, mutable, unique values
my_set = {1, 2, 3, 4, 5}

# Comprehensions: A concise way to create lists, sets, or dictionaries
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
conditional_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
squared_dict = {x: x**2 for x in range(1,10,3)}  # {1: 1, 4: 16, 7: 49}
squared_set = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
# Slicing: Extracting a portion of a list or string
middle_slicing = my_list[1:4]  # [2, 3, 4]
reverse_slicing = my_list[::-1]  # [5, 4, 3, 2, 1]
last_slicing = my_list[-3:]  # [3, 4, 5]
step_slicing = my_list[::2]  # [1, 3, 5]


# Loops and Conditionals
#  for loop: iterate over a sequence (list, tuple, string)
for i in range(5):  #range(5) generates numbers from 0 to 4, range(1, 5) generates numbers from 1 to 4, range(1, 10, 2) generates odd numbers from 1 to 9
    if i % 2 == 0:
        print(f"{i} is even")   # f->formatted string literals, makes it easier to embed expressions inside string literals
    elif i % 2 != 0:
        print(f"{i} is odd")
    else:
        print(f"{i} is zero")
    print(i)  # 0, 1, 2, 3, 4

#  while loop: repeat as long as a condition is true
count = 0
while count < 5:
    print(count)
    count += 1

# Nested Data Structures
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_dict = {"person1": {"name": "Alice", "age": 30}, "person2": {"name": "Bob", "age": 25}}
print(nested_list[1][2])  # 6
print(nested_dict["person1"]["name"])  # Alice


# Problem: Analyze User Order Data
# Given a list of user dictionaries, where each user has a list of orders, perform the following analyses:
# Calculate and print the total amount spent by each user.
# Create a list of all order amounts across all users.
# Create a dictionary mapping each user's ID to the number of orders they have placed.


# --- DEMO: Combining Nested Structures with Control Flow and Comprehensions ---

# Sample data: list of user dictionaries with a list of orders for each user
users_data = [
    {"user_id": 1, "name": "Alice", "orders": [{"order_id": "A1", "amount": 150}, {"order_id": "A2", "amount": 200}]},
    {"user_id": 2, "name": "Bob", "orders": [{"order_id": "B1", "amount": 50}]},
    {"user_id": 3, "name": "Charlie", "orders": []}
]

# # Calculate the total amount spent by each user using a loop
# print("Total amount spent by each user (using loop):")
# for user in users_data:
#     total_spent = 0
#     for order in user.get("orders", []): # Use .get() for safe access
#         total_spent += order.get("amount", 0) # Use .get() for safe access
#     print(f"{user.get('name', 'N/A')}: ${total_spent}")

# # Get a list of all order amounts across all users using a nested comprehension
# all_order_amounts = [order.get("amount", 0) for user in users_data for order in user.get("orders", [])]
# print("\nAll order amounts:", all_order_amounts)

# # Create a dictionary mapping user_id to the number of orders using a dictionary comprehension
# orders_count_by_user = {user.get("user_id"): len(user.get("orders", [])) for user in users_data}
# print("Number of orders per user:", orders_count_by_user)