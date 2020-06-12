def welcome():
    print("welcome.")
def calculate():
    num1 = eval(input("Enter your first_number: "))
    num2 = eval(input("Enter your second_number:"))
    operation = input("""
        type in the operator to use:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        ** for exponention
        // for floor division
        % for modulus
         """)
    if operation == "+":
        sum = num1 + num2
        print("{} + {} = ".format(num1,num2),sum)
    elif operation == "-":
        subtraction = num1 - num2
        print("{} - {} = ".format(num1,num2),subtraction)
    elif operation == "*":
        multiplication = num1 * num2
        print("{} * {} = ".format(num1,num2),multiplication)
    elif operation == "/":
        division = num1 / num2
        print("{} / {} = ".format(num1,num2),division)
    elif operation == "**":
        num3 = eval(input("Enter the power = "))
        exponent = num1 **num3
        print("{} ** {} = ".format(num1,num3),exponent)
    elif operation == "%":
        modulus = num1/num2
        print("{} % {} = ".format(num1,num2),modulus)
    else:
        print("check your operator.")
    repeat()
def repeat():
    response = input("""
    Do you want to continue?
    press y for yes and n for no.
    """)
    if response == "y":
        calculate()
    elif response == "n":
        welcome()
    else:
        repeat()
welcome()
calculate()