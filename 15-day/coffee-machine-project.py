from data import MENU, resources

loop = True
while loop:

    # DATA STATUS
    resources_water = resources["water"]
    resources_milk = resources["milk"]
    resources_coffee = resources["coffee"]

    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    # REPORT STATUS

    def report():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {resources['Money']}")

    # COMPARE DATA
    def compare(coffee_type):
        milk = MENU[coffee_type]["ingredients"]["milk"]
        water = MENU[coffee_type]["ingredients"]["water"]
        coffee = MENU[coffee_type]["ingredients"]["coffee"]
        cost = MENU[coffee_type]["cost"]

        print("Please insert coins.")
        total = int(input(f"How many quarters?: ")) * 0.25
        total += int(input(f"How many dimes?: ")) * 0.1
        total += int(input(f"How many nickles?: ")) * 0.05
        total += int(input(f"How many pennies?: ")) * 0.01

        if total >= cost:
            if resources_water >= water:
                if resources_coffee >= coffee:
                    if resources_milk >= milk:
                        print(f"Here is ${round(total - cost, 2)} in change. ")
                        print("Here is your espresso ☕. Enjoy! ")
                        resources["water"] -= water
                        resources["milk"] -= milk
                        resources["coffee"] -= coffee
                        resources["Money"] += cost
                    else:
                        print("Sorry, there not enough milk.")
                else:
                    print("Sorry, there not enough coffee.")
            else:
                print("Sorry, there not enough water.")
        else:
            print("Sorry that's not enough money. Money refunded.")

    if user_input == "report":
        report()
    elif user_input == "espresso":
        compare("espresso")
    elif user_input == "latte":
        compare("latte")
    elif user_input == "cappuccino":
        compare("cappuccino")
