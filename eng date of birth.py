from datetime import date

today = date.today()

print("This date of birth conveter is work in english calender only.")

birth_year = int(input("Enter your date of birth year (yyyy): "))
birth_mont = int(input("Enter your date of birth month (mm): "))
birth_day = int(input("Enter your date of birth date (dd): "))

year = today.year
month = today.month
day = today.day

cal_year = year - birth_year
cal_mont = month - birth_mont
cal_day = day - birth_day

print(f"{cal_year}Year   {cal_mont}Month   {cal_day}Day")
