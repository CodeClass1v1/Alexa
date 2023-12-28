import random
"""
Author: [Alexa]
Assignment / Part: HW1 - Q5
Due Date: 30 Dec 2023, 8:00 am
I pledge that I have completed this assignment without collaborating with anyone else,
in conformance with the Bornforthis 1v1 School of Computer Science and Procedures on Academic Misconduct.
"""
level = int(input("What is your current level? >>> "))
# 1 - 100% (5/5), 2 - 80% (4/5), 3 - 60% (3/5), 4 - 40% (2/5), 5 -20% (1/5)
target = random.randint(1, 6)
result = target % 5 > (level - 1)
print(f"Your hoot box contains a rare item: {result}")

