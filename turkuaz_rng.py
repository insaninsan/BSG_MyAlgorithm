"""
Turkuaz RNG - XorShift tabanlı rastgele sayı üreteci.

Bu modül, XorShift algoritması kullanarak yüksek kaliteli
pseudo-rastgele sayılar üretir.
"""

import time
from typing import Optional


class TurkuazRNG:
    """
    XorShift algoritması kullanarak rastgele sayı üreten sınıf.
    
    XorShift, bit kaydırma (shift) ve XOR işlemleri kullanarak
    kaotik ve tahmin edilemez sayılar üretir.
    
    Attributes:
        state (int): RNG'nin mevcut durumu (32-bit)
    
    Example:
        >>> rng = TurkuazRNG(seed=12345)
        >>> random_number = rng.next_int()
        >>> random_bit = rng.next_bit()
    """
    
    def __init__(self, seed: Optional[int] = None) -> None:
        """
        RNG'yi başlatır.
        
        Args:
            seed: Başlangıç tohumu. Eğer None ise, o anki zamanı kullanır.
        
        Note:
            Sıfır durumu algoritmayı bozar, bu yüzden otomatik olarak
            123456789 değerine ayarlanır.
        """
        if seed is None:
            self.state = int(time.time() * 1000)
        else:
            self.state = seed
        
        # Sıfır durumu algoritmayı bozar, bu yüzden kontrol edelim
        if self.state == 0:
            self.state = 123456789
        
        # 32-bit sınırında tut
        self.state = self.state & 0xFFFFFFFF

    def next_int(self) -> int:
        """
        Bir sonraki 32-bit rastgele tam sayıyı üretir.
        
        XorShift Algoritması Mantığı:
        Bitleri kaydırıp (shift) kendisiyle XOR'layarak
        kaotik ve tahmin edilemez sayılar üretir.
        
        Returns:
            32-bit rastgele tam sayı (0 ile 2^32-1 arası)
        """
        x = self.state
        
        # 32-bit Xorshift parametreleri
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17)
        x ^= (x << 5) & 0xFFFFFFFF
        
        self.state = x & 0xFFFFFFFF  # 32 bit sınırında tut
        return self.state

    def next_bit(self) -> int:
        """
        Bir sonraki rastgele bit'i üretir (0 veya 1).
        
        Returns:
            0 veya 1 değerinde rastgele bit
        """
        return self.next_int() % 2

