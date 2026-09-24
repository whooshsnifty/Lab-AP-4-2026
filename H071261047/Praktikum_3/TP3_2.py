print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))

        if jumlah_baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        
        jumlah_kursi = int(input("Masukkan jumlah kursi perbaris: "))
        break

    except:
        print("Input harus berupa angka!")
        continue


print("--- Daftar kursi tersedia ---")

for baris in range(1, jumlah_baris + 1):
    for kursi in range (1, jumlah_kursi + 1):
        

        if kursi == 13:
            continue

        if baris == 1 and kursi % 2 == 0:
            continue

        print(f"Baris {baris}, Kursi {kursi}")