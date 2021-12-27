print("*" * 10, "Calculator", "*" * 10)
print("To exit from program type q")

while True:
    arithmetic_operators = input("Choose arithmetic operation (+ - * /):\n")
    if arithmetic_operators == "q":
        break
    if arithmetic_operators in ("+", "-", "*", "/"):
        first_number = float(input("First number is:\n"))
        second_number = float(input("Second number is:\n"))
        print("The result is:")
        if arithmetic_operators == "+":
            print("%.2f" % (first_number + second_number))
        elif arithmetic_operators == "-":
            print("%.2f" % (first_number - second_number))
        elif arithmetic_operators == "*":
            print("%.2f" % (first_number * second_number))
        elif arithmetic_operators == "/":
            if second_number != 0:
                print("%.2f" % (first_number / second_number))
            else:
                print("You can't divide by zero!")      
    else:
        print("Invalid symbol!")
        
