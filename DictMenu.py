# Display menu
print("=============MENU=============")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit")
print("==============================")
dict = {}
info = []
# Ask user to select item
# Perform option
# Option 1 Ask personal data
while True:
    user_input = input("Choose your option (1-3) ")
    if user_input == "1":
        print("Add your information.")
        print()
        name = "Name"
        user_name = dict["Name"] = input("Full Name: ")

        gender = "Gender"
        user_gender = dict["Gender"] = input("Gender: ")

        age = "Age"
        user_age = dict["Age"] = input("Age: ")

        address = "Address"
        user_address = dict["Address"] = input("Address: ")

        phone = "Phone Number"
        user_phone = dict["Phone"] = input("Phone: ")
        
        dict = {
            user_name  : 
            {
                gender: user_gender, age : user_age, address : user_address, phone : user_phone
            }
        }
        print("Info Saved.")
        print()

        info.append(dict)
        dict = {}
        print(info)

# Option 2 Search
    elif user_input == "2":
        print("Search information.")
        print()
        search_user = input ('Full Name: ')
        if search_user == user_name:
            print("Gender: ", user_gender)
            print("Age: ", user_age)
            print("Address: ", user_address)
            print("Phone Number: ", user_phone)

# Option 3 Ask User
    elif user_input == "3":
        exitOption = input("Exit? (Y/N): ")
        if exitOption.upper() == "Y":
            break
        elif exitOption.upper() == "N":
            continue
        else:
            print("Input not recognized.")


    else:
        print("Input not recognized.")
        continue