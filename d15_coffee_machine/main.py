
import store


def is_sufficient_resource(coffee_name):
    coffee_requirement = store.MENU[coffee_name]["ingredients"]
    is_sufficient_flag = True
    for item in coffee_requirement:
        if store.resources[item] < coffee_requirement[item]:
            print(f"Sorry there is not enough {item}.")
            is_sufficient_flag = True
    return is_sufficient_flag


def get_money():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    user_sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    print(f"### User give {round(user_sum, 2)}")
    return user_sum


def is_sufficient_money(coffee_name, user_money):
    coffee_cost = store.MENU[coffee_name]["cost"]
    if user_money < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def make_coffee(user_coffee, user_money):
    coffee_selected = store.MENU[user_coffee]
    coffee_cost = coffee_selected["cost"]
    store.money += coffee_cost
    user_money -= coffee_cost

    print(f"### coffee_selected={coffee_selected}, coffee_cost={coffee_cost}, store.money={store.money}, user_money="
          f"{round(user_money, 2)}")
    for item in coffee_selected["ingredients"]:
        store.resources[item] -= coffee_selected["ingredients"][item]
    print(f"Here is ${round(user_money, 2)} in change.")
    print(f"Here is your {user_coffee} ☕️. Enjoy!")
    return user_money


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    is_machine_on = True
    while is_machine_on:
        user_input = input("What would you like? (espresso/latte/cappuccino):")
        if user_input == "off":
            print("turn off")
            is_machine_on = False
        elif user_input == "report":
            print(f"""
Water: {store.resources["water"]}ml
Milk: {store.resources["milk"]}ml
Coffee: {store.resources["coffee"]}g
Money: ${store.money}
            """)
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            print(f"user want {user_input}")
            if is_sufficient_resource(user_input):
                print("resource sufficient")
                user_money = get_money()
                make_coffee(user_input, user_money)
        else:
            print(f"Invalid input: {user_input}")
