from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_on = True
while is_machine_on:
    user_input = input(f"What would you like? ({menu.get_items()}):")
    if user_input == "off":
        print("turn off")
        is_machine_on = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        print(f"user want {user_input}")
        menu_item = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(menu_item):
            print("resource sufficient")
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
    else:
        print(f"Invalid input: {user_input}")



