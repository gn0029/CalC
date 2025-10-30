from unittest import result
HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found.")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")

def save_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(f"{equation}: {result}\n")
    # file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter two numbers and an operator (+, -, *, /).")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return
    
    if int(result) == result:
        result = int(result)
        print(f"Result: {result}")
        save_history(user_input, result)

def main():
    while True:
        user_input = input("Enter calculation (or 'exit' to quit, 'history' to show history, 'clear' to clear history): ")
        if user_input.lower() == "exit":
            print("Exiting the calculator. Bye")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)

main()


    # # Perform operations

    # addition = num1 + num2
    # subtraction = num1 - num2
    # multiplication = num1 * num2

    # # Handle division carefully (avoid divide by zero)
    # if num2 != 0:
    #     division = num1 / num2
    # else:
    #     division = "undefined (cannot divide by zero)"

    # # Display results
    # print("\nResults:")
    # print(f"Addition: {addition}")
    # print(f"Subtraction: {subtraction}")
    # print(f"Multiplication: {multiplication}")
    # print(f"Division: {division}")

    # # Save the equation and result to history
    # equation = f"{num1} + {num2} = {addition}"
    # save_history(equation, addition)