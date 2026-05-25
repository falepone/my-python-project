"""
Test file untuk semi-automatic workflow
"""

def fibonacci(n: int) -> list:
    """
    Fibonacci serisini üret
    
    Args:
        n: Kaç tane fibonacci sayısı istiyorsun
    
    Returns:
        Fibonacci sayıları listesi
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    
    return fib_list


if __name__ == "__main__":
    result = fibonacci(10)
    print(f"İlk 10 Fibonacci sayısı: {result}")
