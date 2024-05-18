---

# Hamming Kodu Simülatörü

Bu proje, Python ve Tkinter kullanarak bir Hamming Kodu Simülatörü oluşturur. Hamming kodları, verilerdeki hataları tespit etmek ve düzeltmek için kullanılan önemli bir hata düzeltme mekanizmasıdır. Bu simülatör, kullanıcıdan aldığı 4, 8 veya 16 bitlik veriler üzerinde Hamming kodu hesaplar, hataları yapay olarak oluşturur ve düzeltir.

## Özellikler

- **Hamming Kodu Hesaplama:** Kullanıcı tarafından girilen 4, 8 veya 16 bitlik veriler üzerinde Hamming kodunu hesaplar.
- **Hata Oluşturma ve Düzeltme:** Hamming koduna yapay olarak rastgele bir hata ekler ve bu hatayı tespit edip düzeltir.
- **Kullanıcı Dostu Arayüz:** Tkinter kullanarak kolay kullanımlı bir grafiksel kullanıcı arayüzü sağlar.

## Gereksinimler

- Python 3.x
- Tkinter kütüphanesi

## Kurulum

1. Bu projeyi klonlayın:

    ```bash
    git clone https://github.com/siracgezgin/hamming_code.git
    ```

2. Proje dizinine gidin:

    ```bash
    cd hamming_code
    ```

3. Gerekli kütüphaneleri yükleyin (eğer yüklü değilse):

    Tkinter, Python standart kütüphanesiyle birlikte gelir. Ekstra bir yükleme yapmanıza gerek yoktur.

## Kullanım

1. Python scriptini çalıştırın:

    ```bash
    python HammingCodeSimulator.py
    ```

2. Açılan arayüzde 0 ve 1 içeren bir veri girin ve "Hamming Kodunu Hesapla" butonuna tıklayın.
3. Hamming kodu oluşturulduktan sonra "Yapay Hata Oluştur ve Düzelt" butonuna tıklayarak rastgele bir hata oluşturun ve bu hatayı düzeltin.

## Kod Açıklaması

### Hamming Kodu Hesaplama ve Parite Bitleri

```python
def calculate_parity_bits(data, r):
    # Parite bitlerini hesaplar ve veriye ekler
```

### Hamming Kodunu Oluşturma

```python
def hamming_code(data):
    # Kullanıcıdan alınan veri üzerinde Hamming kodunu oluşturur
```

### Kullanıcı Arayüzü Fonksiyonları

```python
def generate_code():
    # Kullanıcıdan alınan veriyi kullanarak Hamming kodunu hesaplar ve ekranda gösterir
```

```python
def introduce_and_fix_error():
    # Rastgele bir hata ekler ve hatayı tespit edip düzeltir
```

### Hata Düzeltme

```python
def fix_error(code):
    # Hatalı bitleri tespit eder ve düzeltir
```

## Katkıda Bulunma

Katkıda bulunmak için lütfen bir pull request gönderin veya bir issue açın.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

---
