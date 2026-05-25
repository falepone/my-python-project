"""
Ana Python dosyası - Agent tarafından yardım alarak yazılmıştır
"""

def hello_world():
    """Hoşgeldiniz fonksiyonu"""
    print("Merhaba, GitHub otomasyonu ile yapılan ilk dosya!")
    return "Success"

def add_numbers(a: int, b: int) -> int:
    """
    İki sayıyı topla
    
    Args:
        a: Birinci sayı
        b: İkinci sayı
    
    Returns:
        İki sayının toplamı
    """
    return a + b

if __name__ == "__main__":
    result = hello_world()
    sum_result = add_numbers(5, 3)
    print(f"Toplam: {sum_result}")
