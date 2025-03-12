def add(a: int, b: int) -> None:
    print(a + b)


operation = input("Enter a operator (+, -, *, /): ")
a = int(input("First number: "))
b = int(input("Second number: "))

if operation == "+":
    add(a, b)
