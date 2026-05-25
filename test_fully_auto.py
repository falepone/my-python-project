"""
Fully Automatic Test - Bu dosya hook test etmek için oluşturuldu
"""

def calculate_sum(numbers: list) -> int:
    """
    Sayı listesinin toplamını hesapla
    
    Args:
        numbers: Sayı listesi
    
    Returns:
        Toplam değeri
    """
    return sum(numbers)


def calculate_average(numbers: list) -> float:
    """
    Sayı listesinin ortalamasını hesapla
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    test_list = [10, 20, 30, 40, 50]
    print(f"Lista: {test_list}")
    print(f"Toplam: {calculate_sum(test_list)}")
    print(f"Ortalama: {calculate_average(test_list)}")
