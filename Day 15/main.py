MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: Print report.
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO: Check resources sufficient?
def checkresources(choice, flag):
    for i in resources:
        if resources[i] < MENU[choice]["ingredients"][i]:
            print(f"Sorry, there is not enough {i}.")
            flag = 1
            break


# TODO: Process coins.
def coins():
    print("Please insert coins.")
    quarter = float(input("how many quarters? "))
    dime = float(input("how many dimes? "))
    nickle = float(input("how many nickles? "))
    penny = float(input("how many pennies? "))
    money = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (penny * 0.01)
    return money


# TODO: Check transaction successful?

# TODO: Make Coffee.
money = 0
while True:
    flag = 0
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        report()
    elif choice == "off":
        break
    else:
        checkresources(choice, flag)
        if flag == 1:
            continue
        amount = coins()
        if amount < MENU[choice]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif amount >= MENU[choice]['cost']:
            change = amount - MENU[choice]['cost']
            money += MENU[choice]['cost']
            for i in resources:
                resources[i] -= MENU[choice]["ingredients"][i]
            print(f"Here is ${round(change, 2)} in change.")
            print(f"Here is your {choice} ☕️. Enjoy!")
