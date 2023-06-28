import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please insert a number larger than 0 next time. ')
        quit()
else:
    print("Please type a number next time. ")
    quit()

random_number = random.randrange(0, top_of_range)
quesses = 0

while True:
    quesses += 1
    user_quess = input("Make a quess: ")
    if user_quess.isdigit():
        user_quess = int(user_quess)
    else:
        print("Please type a number next time. ")
        continue

    if user_quess == random_number:
        print("Congrats")
        break
    elif user_quess > random_number:
         print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", quesses, "quesses.")
