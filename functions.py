"""Python program to practice using functions"""


def greeting() -> None:
    """Prints a friendly greeting for the user"""
    print("Hello!")


def personal_greeting(name: str) -> None:
    """Prints a personalized greeting for the user"""
    print(f"Hey, {name}!")


def add(a: int, b: int) -> None:
    """Add two numbers together and print the result"""
    print(a + b)


def subtract(a: int, b: int) -> None:
    """Subtract one number from the other and print the result"""
    print(a - b)


# user_name: str = input("What is your name: ").title()

# greeting()
# personal_greeting(user_name)
# add(5, 10)
# add(1, 2)
# add(2, 3)
subtract(10, 12)
subtract(5, 3)
subtract(12, 12)
