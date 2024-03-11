# to convert a string data type into an integer data type in python you can use the int()function
numcol = ["red", "yellow", "green"]

def check_scholarship_eligibility():
    has_taken_loan = input("Have you ever taken a loan before? (yes/no): ").lower() == 'no'
    has_attended_college = input("Have you ever been to college before? (yes/no): ").lower() == 'no'

    if not (has_taken_loan and has_attended_college):
        print("Congrats! You've gotten the scholarship.")
    else:
        print("Sorry, you do not meet the scholarship criteria.")

    check_scholarship_eligibility()

# the lower method  ruturns a string  where all letters are lowercase.