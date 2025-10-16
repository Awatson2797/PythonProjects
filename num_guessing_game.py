import random

running = True
num_to_guess = random.randint(1,100)
user_guess = None

while user_guess != num_to_guess:
    try:
        user_guess = int(input("Guess the number between 1 and 100:\n"))
        if user_guess < num_to_guess:
            print("Number is too low!")
        elif user_guess > num_to_guess:
            print("Number is too high!")
        else:
            print("Well done! Your guess is correct!")
            break
    except ValueError:
        print("Please enter a valid number")
        
