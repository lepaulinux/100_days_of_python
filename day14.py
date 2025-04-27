import random  # Importing the random module to make random selections from the list
from game_data import data  # Importing the data list from an external file
import art  # Importing the art module for visual elements
import os
# Initialize the player's score
score = 0

# Game loop condition
compare_choice = True

# Select a random item from data for the first comparison
compare_a = random.choice(data)

# Start the game loop
while compare_choice:
    os.system('clear')

    print(art.logo)  # Print the game logo

    # Display the first comparison item
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")

    print(art.vs)  # Print the "VS" graphic

    # Select a new random item for comparison
    compare_b = random.choice(data)

    # Display the second comparison item
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")

    # Get user's choice and convert it to lowercase for case-insensitive comparison
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower counts for easier comparison
    a_followers = compare_a['follower_count']
    b_followers = compare_b['follower_count']

    # Check if the user's choice is correct
    if (user_choice == "a" and a_followers > b_followers) or (user_choice == "b" and b_followers > a_followers):
        score += 1  # Increase score
        print(f"You're right! Current score: {score}.")
        compare_a = compare_b  # Keep the winner for the next round
    else:  # If the user is wrong
        compare_choice = False  # Exit the loop
        print(f"Sorry, that's wrong. Final score: {score}")



