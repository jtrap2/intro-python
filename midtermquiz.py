# 1. In your own words, describe what the difference
# between a function arguement and a function parameter.
# Write your response using complete sentences.

# a paramater is the the variable listed inside the parenthesis in  the function defenetion
# WHile and argument is  the value that is sent  to the function when it is called

# the formating rules of a laguage

# a type errror is whenever and operation is peformed on and incorrectobject type

# an name error is when you try to use a variable that has not beeen defined or assigned a value

#What function would I use if I wanted to convert an integer data type into 
# a string data type?
# you would use the st

#What function would I use if I wanted to change a float data type into a 
# an integer data type?
# you would use the int() function

# 5. Describe three (3) Variable naming rules. Write your response in complete sentences. 
 #A variable name must start with a letter or the undescore character
# a variable can not start with a number
# variable names are case snesetive


#symbols
# = 
# equal
# == 
#it means it's equal
# =!
# it means it's not equal


 #You have been hired as an engineer to develop a car speed detection system.
# the car company would like to create a function where if the user goes over a certain
# speed it will notify them to change gears. The client has provided you with the following
# guidelines on how they would like the gear system to work:
# if the driver is going over 20mph, alert the driver to shift to gear 1
# if the the driver is going over 30mph, alert the driver to shift to gear 2
# if the driver is going over 40mph, alert the driver to shift to gear 3
# if the driver is going over 70mph, alert the driver to shift back to gear 1.
# the client would like you to pass in the speed that the user is going as an argument. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# we have to make a coperison operator so it dosnt go past the speed limit
# THey want us to pass the speed as and argument
# they want us to create a function

def speed_detection(speed):
    if speed > 70:
        print('shift to gear 1')
    elif speed > 40:
        print('shift to gear 3')
    elif speed > 30:
        print('shift to gear 2')
    elif speed > 20:
        print('shit to gear 1')
speed_detection('enter the current speed' )











# 9. You have been hired as an enineer to develop a school to develop an academic honors system.
# the client would like to check if the user has gotten above an 85% overall grade or has
# has accomplished passing the SAT. The client would like you to pass this information in as
# arguements. If either of these situations are true the student has made the academic honors list
# if only passing the SAT is true, congratulate the user but inform them they did not make the list.
# if they only scored above 85%, congratulate the user but inform them they did not make the list.
# if none of the conditions are met, inform them to continue studying and try again next semester. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.
# we have to make a bolean
# whe have to make and argument
#we have to make comparison operator

def check_academic_honors(overall_grade, sat_passed):
    if overall_grade > 85 or sat_passed:
        print('congratulation! you have madethe academic honors list')
    elif sat_passed:
        print('congratulations on passing the sat! however you have not made the academic honers list ')
    elif overall_grade > 85:
        print('conrgatulations on scorring above a 85! however you did not make the academic honors')
    else:
        print('please continue studying and try again  next semester')

check_academic_honors(overall_grade, 87)

 # 10. Create a function that will check the temperature outside. If the user enters
# a number above 60 degrees it is warm outside, if the enter a number above 80 degrees it is hot outside.
# if the user enters a number below 50 degrees it is cold outside. and if the tempeature is above 50 degrees,
# tell the user it's not warm but it's also not too cold. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# we have  to mak a comparison

def check_tempature(tempature):
    if tempature > 80:
        print(' it is hot outside')
    elif > 60:
        print('it is warm outside')
    elif < 50:
        prin("it is cold outside")
    else:
        print('it's not warm but it is also npot to cold')
check_tempature(60)      





 8. You have been hired as an engineer to develop a fitness meal plan program. 
# your function should take in two (2) arguements; the day of the week, and the time of the day.
# depending on the time of the day; either morning or afternoon, the meal plan will change. 
# the client has provided you with the following meal plan information
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

def FitnessmealPlan(DayOfTheWeek, TimeOfTheDay):
    if DayOfTheWeek == 'monday' and TimeOfTheDay == 'morning':
        print('2 eggs and a apple')
    elif DayOfTheWeek == 'monday' and TimeOfTheDay == 'afternoon':
        print('bbg grilled chicken and broccoli')
    elif DayOfTheWeek == 'tuesday' and TimeOfTheDay == 'morning':
        print('oatmeal with strawberries and blueberries')
    elif DayOfTheWeek == 'tuesday' and TimeOfTheDay == 'afternoon':
        print('baked chicken with kale')
    elif DayOfTheWeek == 'wednesday' and TimeOfTheDay == 'morning':
        print('fruit salad')
    elif DayOfTheWeek == 'wednesday' and TimeOfTheDay == 'afternoon':
        print('curry goat with rice and cabbage')
    elif DayOfTheWeek == 'thursday' and TimeOfTheDay == 'morning':
        print('pankcakes and turkey sausage')
    elif DayOfTheWeek == 'thursday' and TimeOfTheDay == 'afternoon':
        print('eggplant pasta')
    elif DayOfTheWeek == 'friday' and TimeOfTheDay == 'morning':
        print('steak and eggs')
    elif DayOfTheWeek == 'friday' and TimeOfTheDay == 'afternoon':
        print('cheeseburger and fries')
    elif DayOfTheWeek == 'saturday' and TimeOfTheDay == 'morning':
        print('oatmeal')
    elif DayOfTheWeek == 'saturday' and TimeOfTheDay == 'afternoon':
        print('baked chicken with string beans')
    elif DayOfTheWeek == 'sunday' and TimeOfTheDay == 'morning':
        print('oatmeal')
    elif DayOfTheWeek == 'sunday' and TimeOfTheDay == 'afternoon':
        print('steak and spinach')
FitnessmealPlan('wednesday', 'afternoon')



#using the + (addition) operator on a string and an integer value will raise a TypeError.