# Dictionary containing the menu options and their details
MENU = {
    "espresso": {  # Espresso option
        "ingredients": {  # Ingredients required for espresso
            "water": 50,  # 50ml of water
            "coffee": 18,  # 18g of coffee
        },
        "cost": 1.5,  # Cost of an espresso in dollars
    },
    "latte": {  # Latte option
        "ingredients": {  # Ingredients required for latte
            "water": 200,  # 200ml of water
            "milk": 150,  # 150ml of milk
            "coffee": 24,  # 24g of coffee
        },
        "cost": 2.5,  # Cost of a latte in dollars
    },
    "cappuccino": {  # Cappuccino option
        "ingredients": {  # Ingredients required for cappuccino
            "water": 250,  # 250ml of water
            "milk": 100,  # 100ml of milk
            "coffee": 24,  # 24g of coffee
        },
        "cost": 3.0,  # Cost of a cappuccino in dollars
    }
}

# Dictionary storing the current available resources
resources = {
    "water": 300,  # 300ml of water available
    "milk": 200,  # 200ml of milk available
    "coffee": 100,  # 100g of coffee available
}

# Variable to track the total profit earned
profit = 0

# Function to check if there are enough resources to make the chosen drink
def is_resource_sufficient(order_ingredients):
    """Returns True if there are enough resources to make the drink, otherwise False."""
    for item in order_ingredients:  # Loop through each ingredient in the drink
        if order_ingredients[item] >= resources[item]:  # Check if the resource is insufficient
            print(f"Sorry, there is not enough {item}.")  # Notify the user of insufficient resource
            return False  # Return False if an ingredient is lacking
    return True  # Return True if all ingredients are available

# Function to process user payment in coins
def process_coins():
    """Returns the total value of the coins inserted by the user."""
    print("Please insert coins.")  # Prompt the user to insert coins
    total = int(input("How many quarters?: ")) * 0.25  # Convert quarters to dollars
    total += int(input("How many dimes?: ")) * 0.10  # Convert dimes to dollars
    total += int(input("How many nickels?: ")) * 0.05  # Convert nickels to dollars
    total += int(input("How many pennies?: ")) * 0.01  # Convert pennies to dollars
    return total  # Return the total amount inserted

# Function to check if the transaction was successful
def is_transaction_successful(money_received, drink_cost):
    """Returns True if the payment is sufficient, otherwise refunds the money and returns False."""
    if money_received >= drink_cost:  # Check if the user inserted enough money
        change = round(money_received - drink_cost, 2)  # Calculate change to return
        print(f"Here is ${change} in change.")  # Inform the user about their change
        global profit  # Access the global profit variable
        profit += drink_cost  # Add the cost of the drink to the profit
        return True  # Return True if the transaction is successful
    else:
        print("Sorry, that's not enough money. Money refunded.")  # Notify insufficient payment
        return False  # Return False if the payment was insufficient

# Function to make the coffee and deduct ingredients from resources
def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from resources and serves the coffee."""
    for item in order_ingredients:  # Loop through each ingredient
        resources[item] -= order_ingredients[item]  # Deduct the used amount from resources
    print(f"Here is your {drink_name}. ☕ Enjoy!")  # Serve the coffee

# Main program loop to keep the coffee machine running
is_on = True  # Variable to keep track of the machine's status
while is_on:
    # Ask the user for their drink choice
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # If the user enters "off", turn off the coffee machine
    if choice == "off":
        is_on = False

    # If the user enters "report", print the current resource levels and profit
    elif choice == "report":
        print(f"Water: {resources['water']}ml")  # Display available water
        print(f"Milk: {resources['milk']}ml")  # Display available milk
        print(f"Coffee: {resources['coffee']}g")  # Display available coffee
        print(f"Money: ${profit}")  # Display total profit

    # If the user selects a valid coffee option
    else:
        drink = MENU[choice]  # Retrieve the drink details from the menu

        # Check if there are enough resources to make the drink
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()  # Process the user's payment
            if is_transaction_successful(payment, drink["cost"]):  # Validate the transaction
                make_coffee(choice, drink["ingredients"])  # Make and serve the coffee
