def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division and handle division by zero
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Can not divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    except Exception as e:
        return f"An unexpected error occurred: {e}"