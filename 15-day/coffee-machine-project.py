MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "Money":0
}

# CODING START

loop = True

while loop:

    # DATA STATUS
    resources_water = resources["water"]
    resources_milk = resources["milk"]
    resources_coffee = resources["coffee"]

    user_input = input("What whould you like? (espresso/latte/cappuccino): ")
    # REPORT STATUS
    def report():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {resources['Money']}")

    # COMPARE DATA
    def compare():
        espresso_water = MENU["espresso"]["ingredients"]["water"]
        espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
        espresso_cost = MENU["espresso"]["cost"]

        print("Please insert coins.")
        total = int(input(f"How many quarters?: ")) * 0.25
        total += int(input(f"How many dimes?: ")) * 0.1
        total += int(input(f"How many nickles?: ")) * 0.05
        total += int(input(f"How many pennies?: ")) * 0.01

        if total >= espresso_cost:
            if resources_water >= espresso_water:
                if resources_coffee >= espresso_coffee:
                    print(f"Here is ${round(total - espresso_cost, 2)} in change. ")
                    print("Here is your espresso ☕. Enjoy! ")
                    resources["water"] -= espresso_water
                    resources["coffee"] -= espresso_coffee
                    resources["Money"] += espresso_cost
                else:
                    print("Sorry, there not enough coffee.")
            else:
                print("Sorry, there not enough water.")
        else:
            print("Sorry that's not enough money. Money refunded.")

    if user_input == "report":
        report()

    elif user_input == "espresso":
        compare()
    elif user_input == "latte":
        latte_water = MENU["latte"]["ingredients"]["water"]
        latte_milk = MENU["latte"]["ingredients"]["milk"]
        latte_coffee = MENU["latte"]["ingredients"]["coffee"]
        latte_cost = MENU["latte"]["cost"]

        print("Please insert coins.")
        total = int(input(f"How many quarters?: ")) * 0.25
        total += int(input(f"How many dimes?: ")) * 0.1
        total += int(input(f"How many nickles?: ")) * 0.05
        total += int(input(f"How many pennies?: ")) * 0.01
        if total >= latte_cost:
            if resources_water >= latte_water:
                if resources_coffee >= latte_coffee:
                    if resources_milk >= latte_milk:
                        print(f"Here is ${round(total - latte_cost, 2)} in change. ")
                        print("Here is your espresso ☕. Enjoy! ")
                        resources["water"] -= latte_water
                        resources["milk"] -= latte_milk
                        resources["coffee"] -= latte_coffee
                        resources["Money"] += latte_cost
                    else:
                        print("Sorry, there not enough milk.")
                else:
                    print("Sorry, there not enough coffee.")
            else:
                print("Sorry, there not enough water.")
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif user_input == "cappuccino":
        cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
        cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
        cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        cappuccino_cost = MENU["cappuccino"]["cost"]

        print("Please insert coins.")
        total = int(input(f"How many quarters?: ")) * 0.25
        total += int(input(f"How many dimes?: ")) * 0.1
        total += int(input(f"How many nickles?: ")) * 0.05
        total += int(input(f"How many pennies?: ")) * 0.01
        if total >= cappuccino_cost:
            if resources_water >= cappuccino_water:
                if resources_coffee >= cappuccino_coffee:
                    if resources_milk >= cappuccino_milk:
                        print(f"Here is ${round(total - cappuccino_cost, 2)} in change. ")
                        print("Here is your espresso ☕. Enjoy! ")
                        resources["water"] -= cappuccino_water
                        resources["milk"] -= cappuccino_milk
                        resources["coffee"] -= cappuccino_coffee
                        resources["Money"] += cappuccino_cost
                    else:
                        print("Sorry, there not enough milk.")
                else:
                    print("Sorry, there not enough coffee.")
            else:
                print("Sorry, there not enough water.")
        else:
            print("Sorry that's not enough money. Money refunded.")
