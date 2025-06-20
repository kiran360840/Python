import os
import random
os.system("color 0A")
user_num = 1
print("This is random guess game.\n\t Created by'Kiran baskoat'")
attempt = 0
rand = random.randint(1, 100)
while user_num != rand:
    user_num = int(input("Enter a number to guess: "))
    attempt+=1

    if rand > user_num:
        print("Too low!")
    elif rand < user_num:
        print("Too high!!")
    elif attempt == 1:
        print("Hacker🤯.")
        break
    elif attempt > 12:
        print("Too bad but your mind is so goofy.")
    elif attempt <= 12:
        print("Pretty decent mind for folish being like human.")
    else:
        print(f"Conguralution you guessed is correct.\nyour guess in {attempt}attempt.")

os.system("pause")
