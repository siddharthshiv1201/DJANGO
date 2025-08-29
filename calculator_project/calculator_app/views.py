# calculator_app/views.py

from django.http import HttpResponse
import math

def calculate_home(request):
    """
    Provides a welcome message and instructions for using the calculator.
    """
    return HttpResponse(
        "<h1>Welcome to the Scientific Calculator!</h1>"
        "<p>Use the following URL formats:</p>"
        "<ul>"
        "<li><b>Two values:</b> /calculate/&lt;operation&gt;/&lt;value1&gt;/&lt;value2&gt;/</li>"
        "   <ul>"
        "   <li>Operations: add, subtract, multiply, divide, power, log, percentage, root</li>"
        "   <li>Example: /calculate/add/10/5/</li>"
        "   <li>Example: /calculate/power/2/3/</li>"
        "   <li>Example: /calculate/log/100/10/</li>"
        "   </ul>"
        "<li><b>One value:</b> /calculate/&lt;operation&gt;/&lt;value1&gt;/</li>"
        "   <ul>"
        "   <li>Operations: sqrt, sin, cos, tan, abs, factorial</li>"
        "   <li>Example: /calculate/sqrt/16/</li>"
        "   <li>Example: /calculate/sin/90/</li>"
        "   </ul>"
        "</ul>"
    )

def calculate(request, operation, value1, value2=None):
    """
    Performs various mathematical operations based on URL parameters.
    """
    try:
        num1 = float(value1)
        # num2 is optional, so we only try to convert if it's provided
        num2 = float(value2) if value2 is not None else None
    except ValueError:
        return HttpResponse("Error: Please provide valid numeric values for operations.", status=400)

    result = None
    error_message = None

    if operation == 'add':
        if num2 is not None:
            result = num1 + num2
        else:
            error_message = "Error: 'add' operation requires two values."
    elif operation == 'subtract':
        if num2 is not None:
            result = num1 - num2
        else:
            error_message = "Error: 'subtract' operation requires two values."
    elif operation == 'multiply':
        if num2 is not None:
            result = num1 * num2
        else:
            error_message = "Error: 'multiply' operation requires two values."
    elif operation == 'divide':
        if num2 is not None:
            if num2 == 0:
                error_message = "Error: Cannot divide by zero."
            else:
                result = num1 / num2
        else:
            error_message = "Error: 'divide' operation requires two values."
    elif operation == 'percentage':
        if num2 is not None:
            result = (num1 / 100) * num2
        else:
            error_message = "Error: 'percentage' operation requires two values."
    elif operation == 'power':
        if num2 is not None:
            result = num1 ** num2
        else:
            error_message = "Error: 'power' operation requires two values."
    elif operation == 'root':
        if num2 is not None:
            if num1 < 0 and num2 % 2 == 0:
                error_message = "Error: Cannot take an even root of a negative number."
            elif num2 == 0:
                error_message = "Error: Root degree cannot be zero."
            else:
                result = num1 ** (1 / num2)
        else:
            error_message = "Error: 'root' operation requires two values."
    elif operation == 'log':
        if num2 is not None:
            if num1 <= 0 or num2 <= 0 or num2 == 1:
                error_message = "Error: Invalid input for logarithm."
            else:
                result = math.log(num1, num2)
        else:
            error_message = "Error: 'log' operation requires two values."
    elif operation == 'sqrt':
        if num1 < 0:
            error_message = "Error: Cannot calculate square root of a negative number."
        else:
            result = math.sqrt(num1)
    elif operation == 'sin':
        result = math.sin(math.radians(num1))
    elif operation == 'cos':
        result = math.cos(math.radians(num1))
    elif operation == 'tan':
        angle_in_radians = math.radians(num1)
        if math.isclose(math.cos(angle_in_radians), 0, abs_tol=1e-9):
            error_message = f"Error: tan({num1} degrees) is undefined."
        else:
            result = math.tan(angle_in_radians)
    elif operation == 'abs':
        result = abs(num1)
    elif operation == 'factorial':
        if num1 < 0 or num1 != int(num1):
            error_message = "Error: Factorial is defined for non-negative integers only."
        else:
            result = math.factorial(int(num1))
    else:
        error_message = f"Error: Invalid operation '{operation}'."

    if error_message:
        return HttpResponse(f"Operation failed: {error_message}", status=400)
    elif result is not None:
        return HttpResponse(f"Result of {operation}({value1}{', ' + value2 if value2 is not None else ''}): {result}")
    else:
        return HttpResponse(f"An unexpected error occurred for operation '{operation}'.", status=500)