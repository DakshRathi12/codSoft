def calculator():
    print("==== Python Calculator ====")
    
    # Taking inputs from the user
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operation (+, -, *, /, %, //, **): ")
    num2 = float(input("Enter the second number: "))

    # Performing calculation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Cannot divide by zero!"
    elif operator == '%':
        result = num1 % num2
    elif operator == '//':
        if num2 != 0:
            result = num1 // num2
        else:
            return "Error: Cannot perform floor division by zero!"
    elif operator == '**':
        result = num1 ** num2
    else:
        return "Invalid operator!"
    
    return f"Result: {result}"

# Run the calculator
print(calculator())

