"""Python program to practice using functions"""


def greeting() -> None:
    """Prints a friendly greeting for the user"""
    print("Hello!")


def greeting_with_name(name) -> None:
    """Prints a personalized greeting for the user"""
    print(f"Hey, {name}!")


user_name: str = input("What is your name: ").title()

# greeting()
greeting_with_name(user_name)
