import random
from art import logo

# Print the game logo (assuming 'art' module is installed and 'logo' exists)
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number between 1 and 100 (inclusive)
number = random.randint(1, 100)

# Ask for difficulty level
attempts = 0
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Set the number of attempts based on difficulty level
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Invalid entry. Restart the game and choose a valid difficulty.")
    exit()  # Exit the program if an invalid input is entered

# Game loop
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")

    try:
        guess = int(input("Make a guess: "))  # Ensure the input is a valid integer
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  # Skip to the next iteration if input is not a number

    # Check the guess
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {number}.")
        break  # Exit the loop if the guess is correct

    # Reduce attempts only if the guess is incorrect
    attempts -= 1

    if attempts == 0:
        print(f"You've run out of guesses. The number was {number}.")