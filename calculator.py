def calculator():
    first_num = input("Enter the first number: ")
    operator = raw_input("Enter the operator ('+' add, '-' subtract, '*' multiple, '/' divide): ")
    second_num = input("Enter the second number: ")
    if operator == '+':
        return first_num + second_num
    elif operator == '-':
        return first_num - second_num
    elif operator == '*':
        return first_num * second_num
    elif operator == '/':
        return first_num / second_num
    else:
        return "Error! Try again."

print(calculator())




