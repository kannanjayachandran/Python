import random as r

MAX_LINES = 3

MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3


symbols_machine = {
    "👑": 2,
    "🪙": 4,
    "💰": 6,
    "💵": 8,
}


def slot_spin(rows, cols, symbols_machine):

    available_symbols = []

    for symbol, symbol_count in symbols_machine.items():

        for _ in range(symbol_count):
            available_symbols.append(symbol)

    columns = [[], [], []]

    for _ in range(cols):
        column = []
        current_symbol = available_symbols[:]
        for row in range(rows):
            value = r.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)


def mode_select():

    print(" Select the mode you want to play ")
    print("\t\t 1. Any amount ")
    print("\t\t 2. Only 50, 100, 200, 500, 1000 ")

    while True:
        mode = input("Select mode (1 or 2) : ")

        if mode.isdigit():
            mode = int(mode)
            if mode == 1 or mode == 2:
                break
            else:
                print("Mode must be 1 or 2")
        else:
            print("Mode must be a number")

    return mode


def get_deposit_1():
    while True:
        money = input("Enter the amount you want to deposit : ")

        if money.isdigit():
            money = int(money)
            if money > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Amount must be a number")

    return money


def get_deposit_2():
    while True:
        money = input(
            "Enter the amount you want to deposit (50, 100, 200, 500, 1000) only :  ")

        if money.isdigit():
            money = int(money)
            if money == 50 or money == 100 or money == 200 or money == 500 or money == 1000:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Amount must be a number")

    return money


# getting number of lines


def get_lines():
    while True:
        line = input(f'Enter the number of lines to bet (1-{MAX_LINES}): ')

        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                break
            else:
                print("Lines must be greater than 0")
        else:
            print("Lines must be a number")

    return line


def get_bet():

    while True:
        bet_Money = input("Enter the amount you want to bet on each line : ")

        if bet_Money.isdigit():
            bet_Money = int(bet_Money)
            if MIN_BET <= bet_Money <= MAX_BET:
                break
            else:
                print(f'Bet must be between {MIN_BET} and {MAX_BET}')
        else:
            print("Bet amount must be a number")

    return bet_Money


def main():

    mode_choice = mode_select()

    # getting deposit based on mode selected
    account_balance = get_deposit_1 if mode_choice == 1 else get_deposit_2

    lines = get_lines()

    while True:
        bet_amount = get_bet()
        total_bet = bet_amount * lines

        if total_bet >= account_balance:
            print(
                f'You do not have enough money to bet {total_bet}. Your current balance is {account_balance}')
        else:
            break
    print(f'You are betting {bet_amount} on {lines} lines.')
    print(f'Total bet is = {total_bet}')


main()
