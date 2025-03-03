print("Hello, world!")
print("My favorite color is blue.")

user_name = input(
    "What is your name? "
)  # ask the user for their name and save it in user_name
print(
    f"Hello, {user_name or 'friend'}!"
)  # greet the user using their name or friend if user_name is empty
