def calculate():
    operation = input("""
    please type in the operation you would like to compute:
    + for  additin
    - for subtraction
    / for division
    % for modulus
    * for multiplication
    """)
#eval only takes in integers
#prompts the user to enter two numbers
    number1 = eval(input("Enter your fist_number: "))
    number2 = eval(input("Enter your second_number: "))
#dding mathematical operators
#string formatters show the user confirm the mathematical operation
    if operation == "+":
        sum = number1 + number2
        print("{} + {} = ".format(number1,number2),sum)
#subtraction
    elif operation == "-":
        subtraction = number1 - number2
        print("{} - {} = ".format(number1,number2),subtraction)
#multiplication
    elif operation == "*":
        multiplication = number1 * number2
        print("{} * {} = ".format(number1,number2),multiplication)
#division
    elif operation == "/":
        division = number1/number2
        print("{} / {} = ".format(number1,number2),division)
#modulus
    elif operation == "%":
        modulus = number1%number2
        print("{} % {} = ".format(number1,number2),modulus)
    else:
        print("you have entered the wrong operator, run the program again")
    again()
        #again() triggers the again function
def again():
    calculate_again = input("""
    Do you want to perform calculations again?
    please type y for yes and n for no.
    """)
    if calculate_again == "y":
        calculate()
    elif calculate_again  == "n":
        print("bye")
    else:
        again()
        
#call calculate() outside the function
calculate()
