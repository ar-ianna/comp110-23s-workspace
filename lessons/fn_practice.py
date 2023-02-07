"""Example functions to learn definition & calling syntax"""

def my_max(num1: int, num2: int) -> int:
    """Returns the maximum value out of two numbers"""
    if num1>= num2:
        return num1 + 0
    else: #number1 < number2
        return num2

max_number: int = my_max(1,10)
other_max: int = my_max(11,3)
print(other_max)