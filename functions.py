"""Python program to practice using functions"""


def greeting() -> None:
    """Prints a friendly greeting for the user"""
    print("Hello!")


def personal_greeting(name) -> None:
    """Prints a personalized greeting for the user"""
    print(f"Hey, {name}!")


user_name: str = input("What is your name: ").title()

# greeting()
personal_greeting(user_name)
