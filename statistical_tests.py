"""
İstatistiksel Rastgelelik Testleri

Bu modül, rastgele sayı üreteçlerinin kalitesini test etmek için
çeşitli istatistiksel testler içerir.
"""

import math
from typing import List


def ki_kare_testi(bit_dizisi: List[int]) -> bool:
    """
    Ki-Kare (Chi-Square) Testi
    
    Kriter 1: 0 ve 1'lerin eşit dağılımını kontrol eder.
    Amaç: 0 ve 1 sayıları birbirine yakın olmalı.
    
    Args:
        bit_dizisi: Test edilecek bit dizisi (0 ve 1'lerden oluşmalı)
    
    Returns:
        True eğer test başarılı ise (rastgele dağılım), False aksi halde
    
    Note:
        1 serbestlik derecesi ve %5 anlamlılık düzeyi için
        kritik değer 3.841'dir.
    """
    n = len(bit_dizisi)
    beklenen = n / 2
    sayac_1 = sum(bit_dizisi)
    sayac_0 = n - sayac_1
    
    chi_square = ((sayac_0 - beklenen)**2 / beklenen) + ((sayac_1 - beklenen)**2 / beklenen)
    
    print(f"\n--- Ki-Kare (Chi-Square) Testi ---")
    print(f"Toplam Bit: {n}")
    print(f"0 Sayısı: {sayac_0}, 1 Sayısı: {sayac_1}")
    print(f"Hesaplanan Chi-Square Değeri: {chi_square:.4f}")
    
    # 1 serbestlik derecesi ve %5 anlamlılık düzeyi için kritik değer 3.841'dir.
    if chi_square < 3.841:
        print("SONUÇ: BAŞARILI (Dağılım Rastgele)")
        return True
    else:
        print("SONUÇ: BAŞARISIZ (Dağılım Eşit Değil)")
        return False


def mislin_testi(bit_dizisi: List[int]) -> bool:
    """
    Mislin (Runs) Testi
    
    Kriter 2: Ardışık 0'lar ve 1'lerin diziliminin (serilerin)
    rastgeleliğini ölçer.
    
    Örnek: 00001111 dengelidir ama rastgele değildir.
           01010101 de öyle.
    
    Args:
        bit_dizisi: Test edilecek bit dizisi (0 ve 1'lerden oluşmalı)
    
    Returns:
        True eğer test başarılı ise (bağımsız ve rastgele dizilim),
        False aksi halde
    
    Note:
        %95 güven aralığı için Z-skoru -1.96 ile +1.96 arasında olmalı.
        Wald-Wolfowitz formülleri kullanılır.
    """
    n = len(bit_dizisi)
    n1 = sum(bit_dizisi)  # 1'lerin sayısı
    n0 = n - n1           # 0'ların sayısı
    
    # Seri (Run) sayısını bulma
    runs = 1
    for i in range(len(bit_dizisi) - 1):
        if bit_dizisi[i] != bit_dizisi[i + 1]:
            runs += 1
    
    # Beklenen seri sayısı ve varyans hesaplama (Wald-Wolfowitz Formülleri)
    beklenen_runs = ((2 * n0 * n1) / n) + 1
    varyans = ((2 * n0 * n1) * (2 * n0 * n1 - n)) / ((n**2) * (n - 1))
    
    # Z-Skoru hesaplama
    if varyans > 0:
        z_skoru = (runs - beklenen_runs) / math.sqrt(varyans)
    else:
        # Varyans sıfırsa (tüm bitler aynı), test başarısız
        z_skoru = float('inf')
    
    print(f"\n--- Mislin (Runs) Testi ---")
    print(f"Toplam Seri (Runs) Sayısı: {runs}")
    print(f"Beklenen Seri Sayısı: {beklenen_runs:.2f}")
    print(f"Z-Skoru: {z_skoru:.4f}")
    
    # %95 güven aralığı için Z -1.96 ile +1.96 arasında olmalı
    if -1.96 < z_skoru < 1.96:
        print("SONUÇ: BAŞARILI (Dizilim Bağımsız ve Rastgele)")
        return True
    else:
        print("SONUÇ: BAŞARISIZ (Bağımlılık veya Desen Tespit Edildi)")
        return False

