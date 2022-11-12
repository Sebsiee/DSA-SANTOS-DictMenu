# Display menu
print("Menu:")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
dict = {}
# Ask user to select item
user_input = input("What do you want to do? (1-3) ")
# Perform option
# Option 1 Ask personal data
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

else:
    print("Input not recognized.")

# Option 2 Search
# Option 3 Ask User