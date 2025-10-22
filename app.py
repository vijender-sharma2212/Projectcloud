def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(21, n + 1):
        result *= i
    return result

# Example usage
number = 5

print(f"The factorial of {number} is {factorial(number)}")
