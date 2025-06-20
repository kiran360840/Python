import os

os.system("color 0A")

print("Choice:\n  1. Km to Miles\n  2. Miles to Km\n  3. Kg to Pound\n  4. Pound to Kg\n  5. Celcius to Farenhite\n  6. Farenhite to Celcius")
choice = int(input("Enter any choice among them: "))

if choice == 1:
    user_num = float(input("Enter kilomete to convert miles: "))
    Miles = user_num * 0.621371
    print(f"Miles: {Miles}")

elif choice == 2:
    user_num = float(input("Enter miles to convert kilometer: "))
    M = user_num * 1.60934
    print(f"Kilometer: {M}")

elif choice == 3:
    user_num = float(input("Enter Kilogram to Pound: "))
    pound = user_num * 2.2
    print(f"Pound: {pound}")

elif choice == 4:
    user_num = float(input("Enter Pound to Kilogram: "))
    kg = user_num * 2.2
    print(f"Kilogram: {kg}")

elif choice == 5:
    user_num = float(input("Enter Celcius to Farenhite: "))
    faran = (user_num * 9/5) + 32
    print(f"Faranhite: {faran}")

elif choice == 6:
    user_num = float(input("Enter Farenhite to Celcius: "))
    cel = (user_num - 32) * 5/9
    print(f"Faranhite: {cel}")

else:
    print("Enter a correct choice.")
