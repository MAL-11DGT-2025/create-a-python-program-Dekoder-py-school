def add(a: int, b: int) -> None:
    print(a + b)


def subtract(a: int, b: int) -> None:
    print(a - b)


operation = input("Enter a operator (+, -, *, /): ").strip()
a = int(input("First number: "))
b = int(input("Second number: "))

if operation == "+":
    add(a, b)
elif operation == "-":
    subtract(a, b)
