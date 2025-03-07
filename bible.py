book = input("""What is the first book of the bible? 
a) Genesis
b) Exodus
c) Numbers
d) Leviticus
>> """).lower().strip()

options = ["a", "genesis", "b", "exodus", "c", "numbers", "d", "leviticus"]

if book in options:
    if book == "a" or book == "genesis":
        print("Correct!")
    else:
        print("Incorrect.")
else:
    print("Invalid option.")
