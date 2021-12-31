from replit import clear
import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)
    num1 = float(input("Enter the first number?: "))
    for symbol in operations:
        print(symbol)

    exit = True

    while exit:

        operation_symbol = input("Pick an operation ?: ")
        num2 = float(input("Enter the next number?: "))

        result = operations[operation_symbol]
        answer = result(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # ask_user = Input(f"Type 'y' to continue calculating with {answer}, or type new to start new calculator, or type 'n' to exit.: ")
        ask_user = input(f"Type 'y' with old value, 'new' new calculator, or 'n' to exit.: ")
        if ask_user == "y":
            num1 = answer
        elif ask_user == "new":
            clear()
            calculator()
        else:
            exit = False


calculator()