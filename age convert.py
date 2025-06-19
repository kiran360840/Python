from datetime import date

today = date.today()

print("Enter correct choice.\n  English.\n  Nepali.")

choice = input("Enter your choice: ")

if choice == "English" or choice == "english":
     year = today.year
     month = today.month
     day = today.day
     birth_year = int(input("Enter your DOB Year (yyyy): "))
     birth_month = int(input("Enter your DOB Month (mm): "))
     birth_day = int(input("Enter your DOB Day (dd): "))
     cal_year = year - birth_year
     cal_month = month - birth_month
     cal_day = day - birth_day
     print(f"{cal_year}Year   {cal_month}Month   {cal_day}Day")

elif choice == "Nepali" or choice == "nepali":
     birth_year = int(input("Enter your DOB Year (yyyy): "))
     birth_month = int(input("Enter your DOB Month (mm): "))
     birth_day = int(input("Enter your DOB Day (dd): "))
     today_year = int(input("Enter current year (yyyy): "))
     today_month = int(input("Enter current month (mm): "))
     today_day = int(input("Enter current day (dd): "))
     cal_year = today_year - birth_year
     cal_month = today_month - birth_month
     cal_day = today_day - birth_day
     print(f"{cal_year}Year   {cal_month}Month   {cal_day}Day") 

else: 
     print("Enter correct choice.")
