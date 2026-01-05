# Turkuaz-RSÜ (Rastgele Sayı Üreteci)

XorShift algoritması kullanarak yüksek kaliteli pseudo-rastgele sayılar üreten Python kütüphanesi.

## Özellikler

- **XorShift Algoritması**: Hızlı ve güvenilir pseudo-rastgele sayı üretimi
- **İstatistiksel Testler**: Ki-Kare ve Mislin (Runs) testleri ile rastgelelik doğrulaması
- **Kolay Kullanım**: Basit ve anlaşılır API
- **Türkçe Dokümantasyon**: Tüm açıklamalar Türkçe

## Kurulum

Bu proje sadece Python standart kütüphanelerini kullanır, ek kurulum gerekmez.

**Gereksinimler:**
- Python 3.6 veya üzeri

## Kullanım

### Temel Kullanım

```python
from turkuaz_rng import TurkuazRNG

# RNG nesnesi oluştur (otomatik seed)
rng = TurkuazRNG()

# Rastgele tam sayı üret
random_int = rng.next_int()

# Rastgele bit üret (0 veya 1)
random_bit = rng.next_bit()
```

### Özel Seed ile Kullanım

```python
# Belirli bir seed ile başlat
rng = TurkuazRNG(seed=12345)

# Aynı seed ile aynı diziyi üretir
random_number = rng.next_int()
```

### İstatistiksel Testler

```python
from turkuaz_rng import TurkuazRNG
from statistical_tests import ki_kare_testi, mislin_testi

# Rastgele bitler üret
rng = TurkuazRNG()
bit_dizisi = [rng.next_bit() for _ in range(10000)]

# Testleri uygula
sonuc1 = ki_kare_testi(bit_dizisi)
sonuc2 = mislin_testi(bit_dizisi)
```

### Ana Programı Çalıştırma

```bash
python main.py
```

## Algoritma

### XorShift

XorShift, bit kaydırma (shift) ve XOR işlemleri kullanarak kaotik ve tahmin edilemez sayılar üretir. Bu projede 32-bit XorShift algoritması kullanılmaktadır.

**Algoritma Adımları:**
1. Mevcut durumu 13 bit sola kaydır ve XOR işlemi yap
2. Sonucu 17 bit sağa kaydır ve XOR işlemi yap
3. Sonucu 5 bit sola kaydır ve XOR işlemi yap
4. 32-bit sınırında tut

## İstatistiksel Testler

### Ki-Kare Testi

0 ve 1'lerin eşit dağılımını kontrol eder. Rastgele bir dizide 0 ve 1 sayıları birbirine yakın olmalıdır.

### Mislin (Runs) Testi

Ardışık 0'lar ve 1'lerin diziliminin (serilerin) rastgeleliğini ölçer. Rastgele bir dizide seriler dengeli bir şekilde dağılmalıdır.

## Proje Yapısı

```
MyAlgorithm/
├── turkuaz_rng.py          # RNG sınıfı
├── statistical_tests.py     # İstatistiksel testler
├── main.py                # Ana program
└── README.md               # Bu dosya
```

## Lisans

Bu proje eğitim amaçlıdır ve özgürce kullanılabilir.

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen pull request göndermeden önce kodunuzu test edin.

## Yazar

Turkuaz-RSÜ Projesi

