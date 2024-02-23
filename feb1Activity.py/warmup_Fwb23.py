# the two parts needed for a pthyon code is  a function name  and it basically allows the computer to know itss doing a specefic task. then we go the code in the function wich basic is what the computer follows when useing the function name
#a fuction parameter is a variable listed in the function while a function argument is the actual value or variable passed to the function when it is called

def username_andage(username, userage):
    username= userage +10
    username = input('username')
    print(f'goodmorning{username} you will be {userage} in 10 years')
    
username_andage('jaden',17)



def passwordcheck(userpassword):
    password = '123'
    if userpassword == password:
        print("password correct. Welcome to the site")
    else:
        print('password is incorrect. please try again')

passwordcheck('123')
