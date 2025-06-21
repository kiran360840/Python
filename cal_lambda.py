first1 = int(input("Enter your first number: "))
oprater = input("choice +, -, *, /: ")
second2 = int(input("Enter your second number: "))
add = lambda a, b: a + b
sub = lambda a, b: a - b
multi = lambda a, b: a * b
div = lambda a, b: a / b
rem = lambda a, b: a % b
if oprater == "+":
    print(f"Addition: {add(first1, second2)}")
elif oprater == "-":
    print(f"Subctraction: {sub(first1, second2)}")
elif oprater == "*":
    print(f"Multiply: {multi(first1, second2)}")
elif oprater == "/":
    print(f"divide: {int(div(first1, second2))}")
    print(f"Reminder: {rem(first1, second2)}")
else:
    print("Wrong choice.")
