info_holder= {}

size = int(input("Enter the size of dictnoary: "))

for x in range(size):

    key = input("Enter key for dictonary: ")
    value = input("Enter value for Dictnoary: ")
    
    info_holder[key] = value

    print("\nInfo is stored.")

    for key, value in info_holder.items():
        print(f"{key}: {value}")
        print("\n")

print(info_holder)
