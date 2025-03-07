book = input("""What is the first book of the bible? 
a) Genesis
b) Exodus
c) Numbers
d) Leviticus
>> """).lower().strip()

correct_options = ["a", "genesis", "a) genesis", "a)"]
incorrect_options = ["b", "exodus", "b) exodus", "b)", "c", "numbers", "c) numbers", "c)", "d", "leviticus", "d) leviticus", "d)"]


if book in correct_options:
    print("Correct!")
elif book in incorrect_options:
    print("Incorrect.")
else:
    print("Invalid option.")
