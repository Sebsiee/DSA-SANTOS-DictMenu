# Display menu
print("Menu:")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
dict = {}
info = []
# Ask user to select item
# Perform option
# Option 1 Ask personal data
while True:
    user_input = input("What do you want to do? (1-3) ")
    if user_input == "1":
        print("Add your information.")
        name = "Name"
        user_name = dict["Name"] = input("Full Name: ")

        age = "Age"
        user_age = dict["Age"] = input("Age: ")

        address = "Address"
        user_address = dict["Address"] = input("Address: ")
        
        dict = {
            user_name  : 
            {
                age : user_age, address : user_address
            }
        }
        print("Saved!")

        info.append(dict)
        dict = {}
        print(info)

# Option 2 Search
    elif user_input == "2":
        print("Search information.")
        search_user = input ('Full Name: ')
        if search_user == user_name:
            print("Age: ", user_age)
            print("Address: ", user_address)
# Option 3 Ask User
    elif user_input == "3":
        exitOption = print("Exit? ")
        if exitOption == "y":
            break

    else:
        print("Input not recognized.")