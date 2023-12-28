"""
Author: [Alexa]
Assignment / Part: HW1 - Q4
Due Date: 30 Dec 2023, 8:00 am
I pledge that I have completed this assignment without collaborating with anyone else,
in conformance with the Bornforthis 1v1 School of Computer Science and Procedures on Academic Misconduct.
"""
amount = [int(input("Please enter your amount of dollar(s) and cent(s) in two separate lines:\n")), int(input())]
total_in_cents = amount[0] * 100 + amount[1]
n_quarters = int(amount[0] * 100 / 25 + amount[1] // 25)
n_dimes = int((total_in_cents - n_quarters * 25) // 10)
n_nickels = int((total_in_cents - n_quarters * 25 - n_dimes * 10) // 5)
n_pennies = int(total_in_cents - n_quarters * 25 - n_dimes * 10 - n_nickels * 5)
print(f"{amount[0]} dollar(s) and {amount[1]} cent(s) are: \n{n_quarters} quarters, {n_dimes} dimes, {n_nickels} nickels, and {n_pennies} pennies.")
