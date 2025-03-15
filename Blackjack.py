import random
from art import logo
print(logo)

play = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while play:
    should_you_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if should_you_play == "y":
        # Initial hands
        player_hand = random.sample(cards, 2)
        computer_hand = random.sample(cards, 2)

        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")

        another_card = "y"
        while another_card == "y":
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y":
                player_hand.append(random.choice(cards))
                print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
                if sum(player_hand) > 21:
                    print("You went over 21! You lose.")
                    break

        # Computer's turn
        while sum(computer_hand) < 17:
            computer_hand.append(random.choice(cards))

        print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
        print(f"Computer's final hand: {computer_hand}, final score {sum(computer_hand)}")

        # Determine the winner
        if sum(player_hand) > 21:
            print("You lose! 😭")
        elif sum(computer_hand) > 21 or sum(player_hand) > sum(computer_hand):
            print("You win! 😃")
        elif sum(player_hand) == sum(computer_hand):
            print("It's a draw. 🙃")
        else:
            print("You lose!")

    else:
        print("Goodbye.")
        play = False