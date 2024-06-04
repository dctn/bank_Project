import json
def data_update_func():

    user_name = input("enter your name: ")
    new_data = {
        user_name: {
            "amount": 0,
            "loan": 0
        }
    }
    with open("date.json",mode="r") as file:
        all_name = json.load(file)
        name_list = []
        for i in all_name:
            name_list.append(i)

    if user_name not in name_list:
        try:
            with open("date.json", mode="r") as file:
                global data
                data = json.load(file)
                data.update(new_data)
        except:
            with open("date.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("date.json", mode="w") as file:
                json.dump(data, file, indent=4)
                print("account is created")
    else:
        print("this is already taken")
        data_update_func()

global not_in
not_in = True
def credit_or_debit(user_input):
    global not_in
    not_in = True
    name = input("enter your account name: ")
    amount = int(input("enter the amount: "))
    with open("date.json", mode="r") as file:
        data = json.load(file)
    for i in data:
        if i == name:
            not_in = False
            if user_input == "credit":
                data[name]["amount"] += amount
                print("your is successfully credited")
            elif user_input == "debit":
                if data[name]["amount"] > amount:
                    data[name]["amount"] -= amount
                    print("your is successfully debited")
                else:
                    print("you Don't have enough amount")
            elif user_input == "loan":
                data[name]["loan"] += amount
                print("your loan amount is credited in your account")

            data.update(data)

            with open("date.json", mode="w") as file:
                json.dump(data, file, indent=4)

    if not_in:
        print("your name is not found")


repeat = True
while repeat:
    user_input = input(f"Type what option you want\n1.create account\n2.credit\n3.debit\n4.loan\n5.account info\n>>> ").lower()

    if user_input == "create account":


        data_update_func()


    elif user_input == "credit" or user_input == "debit" or user_input == "loan":
       credit_or_debit(user_input=user_input)


    elif user_input == "account info":
        name = input("enter your account name: ")
        with open("date.json",mode='r') as file:
            data = json.load(file)
            for i in data:
                if i == name:
                    not_in = False
                    print(f"name: {name}\namount in account: {data[name]["amount"]}\nloan taken: {data[name]["loan"]}")
        if not_in:
             print("your name is not found")




    else:
        print("spelling is incorrect")

    again = input("\nType YES to continue or to exit type NO:  ").lower()
    if again == "no":
        repeat = False
