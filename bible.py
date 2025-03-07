book = input("""What is the first book of the bible? 
a) Genesis
b) Exodus
c) Numbers
d) Leviticus
>> """).lower().strip()

options = ["a", "genesis", "a) genesis", "b", "exodus", "b) exodus", "c", "numbers", "c) numbers", "d", "leviticus", "d) leviticus"]

if book in options:
    if book == "a" or book == "genesis":
        print("Correct!")
    else:
        print("Incorrect.")
else:
    print("Invalid option.")
