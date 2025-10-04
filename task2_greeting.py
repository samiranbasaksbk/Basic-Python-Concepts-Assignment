# Task 2: Personalized Greeting

# Taking user's first and last name as input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Combining first and last name
full_name = first_name + " " + last_name

# Displaying a personalized greeting
print(f"\nHello, {full_name}! Welcome to the world of Python programming! 😊")
