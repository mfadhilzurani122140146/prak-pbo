def hitung_bilangan_ganjil(batas_bawah, batas_atas):
    if batas_bawah < 0 or batas_atas < 0:
        print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
        return

    jumlah_ganjil = 0
    for i in range(batas_bawah, batas_atas + 1):
        if i % 2 != 0:
            print(i)
            jumlah_ganjil += i

    print("Total:", jumlah_ganjil)

batas_bawah = int(input("batas bawah: "))
batas_atas = int(input("batas atas: "))

hitung_bilangan_ganjil(batas_bawah, batas_atas)
