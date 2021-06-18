print("Welcome to the loan decider! Enter the next four questions on a 1-10 scale to receive a consultation.\n")

loan = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

if loan >= 5:
    if credit_history >= 7 and income >= 7:
        approval = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            approval = True
        else:
            approval = False
    else:
        approval = False
else:
    if credit_history < 4:
        approval = False 
    else:
        if income >= 7 or down_payment >= 7:
            approval = True
        elif income >= 4 and down_payment >= 4:
            approval = True
        else:
            approval = False

if approval:
    print("\nYour loan has been approved.")
if not approval:
    print("\nYour loan has been denied.")