while True:
    try:
        jumlah_kursi = int(input("Masukkan jumlah kursi bus: "))
        break
    except:
        print("Input jumlah kursi harus berupa angka!")

print("--- Sistem Reservasi PO BUS Dimulai ---")

sisa_kursi = jumlah_kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print("Sisa kursi:", sisa_kursi)

    try:
        umur = int(input("Masukkan umur penumpang: "))

        if umur < 0:
            print("Umur tidak valid!")
            continue

        if umur <= 5:
            kategori = "Balita"
            harga = 0
            print(f"Kategori: {kategori} - Tiket gratis (Rp 0)")

        elif umur <= 12:
            kategori = "Anak"
            harga = 50000
            print(f"Kategori: {kategori} - Harga Rp 50.000")

        else:
            kategori = "Dewasa"
            harga = 100000
            print(f"Kategori: {kategori} - Harga Rp 100.000")

        total_pendapatan += harga
        sisa_kursi -= 1

    except:
        print("Input umur harus berupa angka!")

print("--- Semua Kursi Terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini: Rp", total_pendapatan)