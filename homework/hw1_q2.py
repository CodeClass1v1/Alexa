"""
Author: [Alexa]
Assignment / Part: HW1 - Q2
Due Date: 30 Dec 2023, 8:00 am
I pledge that I have completed this assignment without collaborating with anyone else,
in conformance with the Bornforthis 1v1 School of Computer Science and Procedures on Academic Misconduct.
"""
birth_per_year = int(365 * 24 * 60 * 60 // 7)
death_per_year = int(365 * 24 * 60 * 60 // 15)
immigrant_per_year = int(365 * 24 * 60 * 60 // 42)
emigrant_per_year = int(365 * 24 * 60 // 1.25)
net_change_per_year = birth_per_year - death_per_year + immigrant_per_year - emigrant_per_year
year_in_question = int(input("Please enter a year greater than 2023:>>>"))
n = year_in_question - 2023
estimated_population = 330109174 + n * net_change_per_year
print(f"The population in year {year_in_question} will be {estimated_population}.")
