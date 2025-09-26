def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "you can't divide by zero"
    else:
        return "Enter the correct operation"
    
