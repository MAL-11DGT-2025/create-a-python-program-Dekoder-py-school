book = input("""What is the first book of the bible? 
a) Genesis
b) Exodus
c) Numbers
d) Leviticus
>> """).lower().strip()

options = ["a", "genesis", "a) genesis", "b", "exodus", "b) exodus", "c", "numbers", "c) numbers", "d", "leviticus", "d) leviticus"]

if book in options:
    if book == options[0] or book == options[1] or book == options[2]:
        print("Correct!")
    else:
        print("Incorrect.")
else:
    print("Invalid option.")
