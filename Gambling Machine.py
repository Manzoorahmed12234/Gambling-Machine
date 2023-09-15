#special thanks to tech with tim

import random
Max_lines = 3
Max_bet = 1000
Min_bet = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
    }

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
    }

def find_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_gambling_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_gambling_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



def Insert_money():
    while True:
        deposit = input("Please enter the amount you would like to deposit? $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("Invalid choice: Amount should be greater than 0.")
        else:
            print("Please enter a number.")
    return deposit

def number_of_lines():
    while True:
        lines = input("Please enter the number of lines to bet on? 1 -" + str(Max_lines) + ")? $")
        if lines.isdigit():
            lines = int(lines)
            if 0 <= lines <= Max_lines:
                break
            else:
                print("Invalid choice: Enter a valid number.")
        else:
            print("Please enter a number.")
    return lines

def amount_of_bet():
    while True:
        bet = input("Please enter your bet per line $")
        if bet.isdigit():
            bet = int(bet)
            if Min_bet <= bet <= Max_bet:
                break
            else:
                print(f"Bet must be between ${Min_bet} - ${Max_bet} .")
        else:
            print("Please enter a number.")
    return bet

def spin(balance):
    lines = number_of_lines()
    while True:
        bet = amount_of_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough balance. your total amount is ${balance}")
        else:
            break


    print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet}")
    print(balance,lines)

    slots = get_gambling_spin(ROWS, COLS, symbols_count )
    print_gambling_machine(slots)
    winnings, winning_lines = find_winnings(slots, lines, bet, symbols_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet



def main():

    balance = Insert_money()

    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
main()




