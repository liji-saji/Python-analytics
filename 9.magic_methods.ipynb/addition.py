def calculator():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Get the user's choice
    choice = input("Enter the number of the operation (1/2/3/4): ")
    
    # Ensure the input is valid
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice, please select a valid operation.")
        return
    
    # Get the numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input, please enter numeric values.")
        return

    # Perform the operation
    if choice == '1':
        print(f"The result is: {num1 + num2}")
    elif choice == '2':
        print(f"The result is: {num1 - num2}")
    elif choice == '3':
        print(f"The result is: {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
            
# Run the calculator
calculator()
