birth_year = int(input("Enter your DOB year (yyyy): "))
birth_month = int(input("Enter your DOB month (mm): "))
birth_day = int(input("Enter your DOB day (dd): "))

tdy_year = int(input("Enter current year: "))
tdy_month = int(input("Enter current month: "))
tdy_day = int(input("Enter current day: "))

cal_year = tdy_year - birth_year
cal_month = tdy_month - birth_month
cal_day = tdy_day - birth_day

print(f"{cal_year}Year   {cal_month}Month   {cal_day}Day")
