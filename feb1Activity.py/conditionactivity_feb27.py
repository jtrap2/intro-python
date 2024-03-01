def access_control(user_input):
    correct_passcode = "get_this_money"
    if user_input == correct_passcode:
        print("access granted. welcome!")
    else:
        print("acces denied. Incorrect ")

access_control("get_this_money")