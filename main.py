#!/usr/bin/env python3
"""
Advanced Calculator - Main Entry Point
Demonstrates calculator functionality with examples
"""

from src.calculator import Calculator, MathOperations


def main():
    """Main function demonstrating calculator usage"""
    
    print("=" * 60)
    print("🧮 Advanced Calculator Demo")
    print("=" * 60)
    
    # Initialize calculator
    calc = Calculator(precision=2)
    
    # Demonstrate basic operations
    print("\n📊 Basic Operations:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 × 7 = {calc.multiply(6, 7)}")
    print(f"20 ÷ 4 = {calc.divide(20, 4)}")
    
    # Demonstrate advanced operations
    print("\n🔬 Advanced Operations:")
    print(f"2^10 = {calc.power(2, 10)}")
    print(f"√144 = {calc.square_root(144)}")
    print(f"5! = {calc.factorial(5)}")
    
    # Demonstrate Fibonacci
    print("\n📈 Fibonacci Sequence (First 10):")
    fib = calc.fibonacci(10)
    print(fib)
    
    # Show history
    print("\n📜 Operation History:")
    history = calc.get_history()
    for i, operation in enumerate(history, 1):
        print(f"  {i}. {operation}")
    
    print("\n" + "=" * 60)
    print("✅ Demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
