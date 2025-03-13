from art import logo
print(logo)
import os
def clear_screen():
    if os.name == 'posix':  # Linux/macOS
        os.system('clear || echo -e "\033c"')  # Uses 'clear', but falls back to ANSI escape codes if 'clear' fails


# TODO-1: Ask the user for input
bids = {}  # Dictionary to store bidders' names and their bid amounts

while True:
    name = input("What is your name: ")  # Get the bidder's name
    bid = int(input("What is your bid $"))  # Convert bid to integer
    others = input("Are there any other bidders? Type 'y' for Yes or 'n' for No: ").lower()  # Check for more bidders
    clear_screen()

    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid  # Store name as key and bid as integer value

    if others == "n":  # If no more bidders, exit loop
        break

# TODO-4: Compare bids in dictionary
max_bidder = max(bids, key=bids.get)  # Finds the key (name) with the highest bid
max_value = bids[max_bidder]  # Gets the highest bid amount

print(f"The winner is {max_bidder} with a bid of ${max_value}.")  # Display winner

