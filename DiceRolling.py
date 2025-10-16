import random
running = True
while running:
    user_input = input("Roll the dice? y/n\n").lower()
    if user_input == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1},{die2})")
    elif user_input == "n":
        print("Thank you for playing! Goodbye")
        break
    else:
        print("Not a valid choice!")