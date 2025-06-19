import random
import time
import os
def loading():
    x = 1
    while x <= 3: 
        os.system("cls")
        print("rolling.")
        time.sleep(1)
        os.system("cls")
        print("rolling..")
        time.sleep(1)
        os.system("cls")
        print("rolling...")
        time.sleep(1)
        os.system("cls")
        x += 1

loading()

print(f"Congrulation you got: {random.randint(1, 6)}")
