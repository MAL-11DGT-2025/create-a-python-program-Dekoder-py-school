"""Python program to practice using functions"""


def greeting() -> None:
    """Prints a friendly greeting for the user"""
    print("Hello!")


def personal_greeting(name: str) -> None:
    """Prints a personalized greeting for the user"""
    print(f"Hey, {name}!")


def add(a: int, b: int) -> None:
    print(a + b)


# user_name: str = input("What is your name: ").title()

# greeting()
# personal_greeting(user_name)
add(5, 10)
add(23, 104)
add(55, 1120)
