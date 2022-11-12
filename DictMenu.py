# Display menu
print("Menu:")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
dict = {}
# Ask user to select item
# Perform option
# Option 1 Ask personal data
while True:
    user_input = input("What do you want to do? (1-3) ")
    if user_input == "1":
        print("Add your information.")
        name = "Name"
        user_name = input("Full Name: ")
        dict[name] = user_name

        age = "Age"
        user_age = input("Age: ")
        dict[age] = user_age

        address = "Address"
        user_address = input("Address: ")
        dict[address] = user_address
        
        dict = {user_name  : {age : user_age, address : user_address}}
        print("Saved!")

        print(dict)

    elif user_input == "2":
        print("Search information.")
        user_name = input("Full Name: ")
        print("Age: ", user_age)
        print("Address: ", user_address)

    elif user_input == "3":
        exitOption = print("Exit? ")
        if exitOption == "y":
            break
        
    else:
        print("Input not recognized.")

# Option 2 Search
# Option 3 Ask User