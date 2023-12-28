"""
Author: [Alexa]
Assignment / Part: HW1 - Q5
Due Date: 30 Dec 2023, 8:00 am
I pledge that I have completed this assignment without collaborating with anyone else,
in conformance with the Bornforthis 1v1 School of Computer Science and Procedures on Academic Misconduct.
"""
Semi_days = int(input("Please enter the number of days Semi worked: "))
Semi_hours = int(input("Please enter the number of hours Semi worked: "))
Semi_minutes = int(input("Please enter the number of minutes Semi worked: "))
Semi_total = Semi_days * 24 * 60 + Semi_hours * 60 + Semi_minutes
Ollie_days = int(input("Please enter the number of days Ollie worked: "))
Ollie_hours = int(input("Please enter the number of hours Ollie worked: "))
Ollie_minutes = int(input("Please enter the number of minutes Ollie worked: "))
Ollie_total = Ollie_days * 24 * 60 + Ollie_hours * 60 + Ollie_minutes
Total = Semi_total + Ollie_total
days = int(Total // (24 * 60))
hours = int((Total - days * 24 * 60) // 60)
minutes = int(Total - days * 24 * 60 - hours * 60)
print(f"The total time both of them worked together is: {days} day(s), {hours} hour(s), amd {minutes} minute(s).")