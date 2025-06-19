print("Choice.\n1 = add.\n2 = subctract.\n3 = multiply.\n4 = divide.")
first = int(input("Enter your first number: "))
oprater = int(input("Enter any choice: "))
second = int(input("Enter your second number: "))

match oprater:
    case 1:
        add = first + second
        print(f"{first} + {second} = {add}")
    case 2:
        sub = first - second
        print(f"{first} - {second} = {sub}")
    case 3:
        mult = first * second
        print(f"{first} * {second} = {mult}")
    case 4:
        divide = first / second
        rem = first % second
        print(f"{first} / {second} = {divide}")
        print(f"{first} % {second} = {rem}")
    case _:
        print("Enter correct choice.")
