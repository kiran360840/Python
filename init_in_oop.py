class second:
    def __init__(info, fname, lname, age, addresh):
        info.fname = fname
        info.lname = lname
        info.age = age
        info.addresh = addresh

first_ = input("Enter your first name: ")
last_ = input("Enter Your last name: ")
age1 = int(input("Enter your age: "))
address = input("Enter your addresh: ") 


Sec_class1 = second(first_, last_, age1, address)

print(f"Your full name: {Sec_class1.fname} {Sec_class1.lname}.")
print(f"Your age is: {Sec_class1.age}.")
print(f"Your Addresh is: {Sec_class1.addresh}.")
