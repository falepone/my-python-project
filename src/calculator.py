"""
Advanced Calculator Module
Provides comprehensive mathematical operations with error handling
"""

from typing import Union, List
from enum import Enum
import math


class MathOperations(Enum):
    """Available mathematical operations"""
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    POWER = "power"
    SQUARE_ROOT = "sqrt"
    FACTORIAL = "factorial"


class Calculator:
    """
    Advanced Calculator class with multiple operations
    
    Attributes:
        history: List of all performed operations
        precision: Decimal precision for results
    """
    
    def __init__(self, precision: int = 2):
        """
        Initialize Calculator
        
        Args:
            precision: Decimal places for rounding (default: 2)
        """
        self.history: List[str] = []
        self.precision = precision
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Add two numbers
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Sum of a and b
        """
        result = a + b
        self._log_operation(f"add({a}, {b}) = {result}")
        return round(result, self.precision)
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract b from a"""
        result = a - b
        self._log_operation(f"subtract({a}, {b}) = {result}")
        return round(result, self.precision)
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers"""
        result = a * b
        self._log_operation(f"multiply({a}, {b}) = {result}")
        return round(result, self.precision)
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Divide a by b
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        
        result = a / b
        self._log_operation(f"divide({a}, {b}) = {result}")
        return round(result, self.precision)
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Calculate base raised to exponent"""
        result = base ** exponent
        self._log_operation(f"power({base}, {exponent}) = {result}")
        return round(result, self.precision)
    
    def square_root(self, n: Union[int, float]) -> float:
        """
        Calculate square root of n
        
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        
        result = math.sqrt(n)
        self._log_operation(f"sqrt({n}) = {result}")
        return round(result, self.precision)
    
    def factorial(self, n: int) -> int:
        """
        Calculate factorial of n
        
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        
        result = math.factorial(n)
        self._log_operation(f"factorial({n}) = {result}")
        return result
    
    def fibonacci(self, n: int) -> List[int]:
        """
        Generate first n Fibonacci numbers
        
        Args:
            n: Number of Fibonacci numbers to generate
        
        Returns:
            List of Fibonacci numbers
        """
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        
        self._log_operation(f"fibonacci({n}) generated {n} numbers")
        return fib_list
    
    def get_history(self) -> List[str]:
        """Get all operation history"""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear operation history"""
        self.history.clear()
    
    def _log_operation(self, operation: str) -> None:
        """
        Private method to log operations
        
        Args:
            operation: Operation description to log
        """
        self.history.append(operation)
