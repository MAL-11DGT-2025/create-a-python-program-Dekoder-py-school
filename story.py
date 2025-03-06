def tell_a_story(age, name, car, food, whanau, game):
    print(f"Kia Ora {name}! I also enjoy playing {game}. I think {age} is the right age to learn to drive a {car}. I don't mind {food}. I think {whanau}'s the worst too!")


age = input("How old are you: ")
name = input("What's your name: ")
car = input("What's your favorite car: ")
food = input("What's your favorite food: ")
whanau = input("What is the worst whanau / house: ")
game = input("What's your favorite game: ")

tell_a_story(age, name, car, food, whanau, game)
