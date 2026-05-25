"""
Unit tests for Calculator module
Comprehensive test coverage for all operations
"""

import pytest
from src.calculator import Calculator, MathOperations


class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add(self, calculator):
        """Test addition operation"""
        assert calculator.add(5, 3) == 8
        assert calculator.add(-5, 3) == -2
        assert calculator.add(0, 0) == 0
    
    def test_subtract(self, calculator):
        """Test subtraction operation"""
        assert calculator.subtract(10, 3) == 7
        assert calculator.subtract(3, 10) == -7
        assert calculator.subtract(5, 5) == 0
    
    def test_multiply(self, calculator):
        """Test multiplication operation"""
        assert calculator.multiply(5, 3) == 15
        assert calculator.multiply(-5, 3) == -15
        assert calculator.multiply(0, 100) == 0
    
    def test_divide(self, calculator):
        """Test division operation"""
        assert calculator.divide(10, 2) == 5.0
        assert calculator.divide(7, 2) == 3.5
        assert calculator.divide(-10, 2) == -5.0
    
    def test_divide_by_zero(self, calculator):
        """Test division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Division by zero"):
            calculator.divide(10, 0)


class TestAdvancedOperations:
    """Test advanced mathematical operations"""
    
    def test_power(self, calculator):
        """Test power operation"""
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 0) == 1
        assert calculator.power(2, -1) == 0.5
    
    def test_square(self, calculator):
        """Test square operation"""
        assert calculator.square(4) == 16
        assert calculator.square(5) == 25
        assert calculator.square(0) == 0
    
    def test_cube(self, calculator):
        """Test cube operation"""
        assert calculator.cube(2) == 8
        assert calculator.cube(3) == 27
        assert calculator.cube(0) == 0
    
    def test_modulo(self, calculator):
        """Test modulo operation"""
        assert calculator.modulo(10, 3) == 1
        assert calculator.modulo(7, 2) == 1
        assert calculator.modulo(20, 5) == 0
    
    def test_modulo_by_zero(self, calculator):
        """Test modulo by zero raises ValueError"""
        with pytest.raises(ValueError, match="zero divisor"):
            calculator.modulo(10, 0)
    
    def test_square_root(self, calculator):
        """Test square root operation"""
        assert calculator.square_root(4) == 2.0
        assert calculator.square_root(9) == 3.0
        assert calculator.square_root(0) == 0.0
    
    def test_square_root_negative(self, calculator):
        """Test square root of negative number raises ValueError"""
        with pytest.raises(ValueError, match="negative"):
            calculator.square_root(-1)
    
    def test_factorial(self, calculator):
        """Test factorial operation"""
        assert calculator.factorial(0) == 1
        assert calculator.factorial(5) == 120
        assert calculator.factorial(1) == 1
    
    def test_factorial_negative(self, calculator):
        """Test factorial of negative number raises ValueError"""
        with pytest.raises(ValueError, match="negative"):
            calculator.factorial(-1)


class TestFibonacci:
    """Test Fibonacci sequence generation"""
    
    def test_fibonacci_basic(self, calculator):
        """Test basic Fibonacci sequence"""
        assert calculator.fibonacci(5) == [0, 1, 1, 2, 3]
        assert calculator.fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
    
    def test_fibonacci_edge_cases(self, calculator):
        """Test Fibonacci edge cases"""
        assert calculator.fibonacci(0) == []
        assert calculator.fibonacci(1) == [0]
        assert calculator.fibonacci(2) == [0, 1]


class TestHistory:
    """Test operation history tracking"""
    
    def test_history_logging(self, calculator):
        """Test that operations are logged to history"""
        calculator.add(5, 3)
        calculator.multiply(2, 4)
        
        history = calculator.get_history()
        assert len(history) == 2
        assert "add(5, 3)" in history[0]
        assert "multiply(2, 4)" in history[1]
    
    def test_clear_history(self, calculator):
        """Test clearing history"""
        calculator.add(5, 3)
        assert len(calculator.get_history()) == 1
        
        calculator.clear_history()
        assert len(calculator.get_history()) == 0


class TestPrecision:
    """Test decimal precision handling"""
    
    def test_default_precision(self, calculator):
        """Test default precision is 2 decimal places"""
        assert calculator.divide(10, 3) == 3.33
    
    def test_custom_precision(self, calculator_with_precision):
        """Test custom precision"""
        assert calculator_with_precision.divide(10, 3) == 3.3333
