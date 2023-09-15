
The program simulates a gambling machine with 3x3 grid of symbols. The user can bet on one or more lines. The winnings are calculated based on the number of winning lines and the amount of bet per line.

The program first prompts the user to enter the amount of money they want to deposit. It then enters a loop where it prompts the user to play or quit. If the user chooses to play, it prompts the user to enter the number of lines they want to bet on and the amount they want to bet per line. It then checks if the total bet is greater than the user's balance. If it is, it prints a message and returns. Otherwise, it calculates the total bet, spins the gambling machine, and prints the results.

The program uses the following functions:

find_winnings(): This function finds the winning lines and the amount of winnings for a given grid of symbols.
get_gambling_spin(): This function generates a random 3x3 grid of symbols.
Insert_money(): This function prompts the user to enter the amount of money they want to deposit.
number_of_lines(): This function prompts the user to enter the number of lines they want to bet on.
amount_of_bet(): This function prompts the user to enter the amount they want to bet per line.
spin(): This function is the main function of the program. It spins the gambling machine and prints the results.
main(): This function is the entry point of the program. It prompts the user to enter the amount of money they want to deposit and then enters a loop where it prompts the user to play or quit.
