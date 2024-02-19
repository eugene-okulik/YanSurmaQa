import random

bonus = random.choice([True, False])
salary = int(input("Your salary is: "))
random_bonus = random.randint(1, 10000)

if bonus:
    print(f" {salary}, {bonus}, '${random_bonus}'")
else:
    print("You haven't bonus yet!")
