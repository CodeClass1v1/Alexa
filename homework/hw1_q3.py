"""
Author: [Alexa]
Assignment / Part: HW1 - Q3
Due Date: 30 Dec 2023, 8:00 am
I pledge that I have completed this assignment without collaborating with anyone else,
in conformance with the Bornforthis 1v1 School of Computer Science and Procedures on Academic Misconduct.
"""
quarters = 25 * int(input("Please enter the number of coins: \nNumber of quarters:"))
dimes = 10 * int(input("Number of dimes:"))
nickels = 5 * int(input("Number of nickels:"))
pennies = int(input("Number of pennies:"))
total_in_cents = quarters + dimes + nickels + pennies
dollar = int(total_in_cents // 100)
cents = total_in_cents - dollar * 100
print(f"The total is {dollar} dollar(s) and {cents} cent(s)")