from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem()
coffee = CoffeeMaker()
money = MoneyMachine()

cost = 0
while True:
    flag = 0
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        coffee.report()
    elif choice == "off":
        break
    else:
        if coffee.is_resource_sufficient(choice):
            continue
        y = money.process_coins()
        if money.make_payment():
            continue
        else:
            coffee.make_coffee(menu_item)
