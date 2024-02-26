import math

def hitung_luas(jari_jari):
    return math.pi * jari_jari ** 2

def hitung_keliling(jari_jari):
    return 2 * math.pi * jari_jari

jari_jari = float(input("jari-jari: "))

if jari_jari < 0:
    print("jari-jari lingkaran tidak boleh negatif.")
else:
    luas = hitung_luas(jari_jari)
    keliling = hitung_keliling(jari_jari)

    print("Luas:", round(luas, 2))
    print("Keliling:", round(keliling, 2))
