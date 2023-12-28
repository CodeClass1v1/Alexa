"""
Author: [Alexa]
Assignment / Part: HW1 - Q5
Due Date: 30 Dec 2023, 8:00 am
I pledge that I have completed this assignment without collaborating with anyone else,
in conformance with the Bornforthis 1v1 School of Computer Science and Procedures on Academic Misconduct.
"""
# part b
weight = int(input("Please enter weight in pounds: "))
height = float(input("Please enter height in inches: "))
BMI = (weight * 0.453592) / ((height * 0.0254) ** 2)
print(f"BMI is: {BMI}")