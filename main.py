"""
Turkuaz-RSÜ (Rastgele Sayı Üreteci) - Ana Program

Bu program, TurkuazRNG sınıfını kullanarak rastgele bitler üretir
ve istatistiksel testlerle kalitesini değerlendirir.
"""

from turkuaz_rng import TurkuazRNG
from statistical_tests import ki_kare_testi, mislin_testi


def main():
    """Ana program fonksiyonu."""
    print("Turkuaz-RSÜ (Rastgele Sayı Üreteci) Başlatılıyor...\n")
    
    # 1. Nesneyi oluştur
    rng = TurkuazRNG()  # Seed otomatik (zaman bazlı)
    
    # 2. Veri Üret (İstatistiksel doğruluk için 10.000 bit üretelim)
    veri_seti = []
    print("Veri üretiliyor (İlk 20 bit): ", end="")
    
    for i in range(10000):
        bit = rng.next_bit()
        veri_seti.append(bit)
        if i < 20:  # Sadece ilk 20 tanesini ekrana yaz
            print(bit, end="")
    print("...")
    
    # 3. Testleri Uygula
    sonuc1 = ki_kare_testi(veri_seti)
    sonuc2 = mislin_testi(veri_seti)
    
    # 4. Genel Sonuç
    print("\n" + "="*50)
    if sonuc1 and sonuc2:
        print(">>> GENEL SONUÇ: ALGORİTMA MÜKEMMEL ÇALIŞIYOR <<<")
    else:
        print(">>> GENEL SONUÇ: ALGORİTMA İYİLEŞTİRİLMELİ <<<")
    print("="*50)


if __name__ == "__main__":
    main()

