num = int(input("Enter your number to check weather it's odd or even: "))
if num < 0:
    print("Negative number")
elif num == 0:
    print("Zero")
elif num % 2 == 0:
    print("Even")
else:
    print("Odd")
