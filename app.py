from db_config import Customer

while True:
    str = input("Your command >")
    if str == "Q":
        print("Bye!")
        break
    elif str == "A":
        input_name = input("New user name >")
        input_age = int(input("New user age >"))
        Customer.create(name=input_name, age=input_age)
        print(f"Add new user{input_name}")
        # print("Add new user"+input_name)
    elif str == "S":
        for customer in Customer.select():
            print(f"Name: {customer.name} Age: {customer.age}")
            




            
