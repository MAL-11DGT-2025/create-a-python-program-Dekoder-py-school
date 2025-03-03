# print("Hello, world!")
# print("My favorite color is blue.")

user_name = input(
    "What is your name? "
)  # ask the user for their name and save it in user_name
print(
    f"Hello, {user_name.title() or 'friend'}!"
)  # greet the user using their name or friend if user_name is empty

while True:
    user_age_string = input("Enter your age (in years): ")
    # try to convert the user's age input to an int, if it fails try again.
    try:
        user_age = int(user_age_string)
        break
    except ValueError:  # meaning the user has typed something that cannot be a number
        print("Please enter only numbers!")
        continue

if user_age >= 55:
    print(f"Wow! {user_age} is pretty old!")
else:
    print(f"{user_age} is pretty young!")
