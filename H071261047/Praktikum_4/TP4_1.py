def hitung_subtotal(harga, jumlah, adalah_member):
    subtotal = harga * jumlah

    if adalah_member:
        subtotal = subtotal * 0.9
    return int(subtotal)

print("Selamat datang di kasir Minimarket!")

status = input("Apakah Anda member? (y/n): ")
member = status.lower() == "y"
total = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        break

    harga = int(input("Harga Barang: "))
    jumlah = int(input("Jumlah Barang: "))

    subtotal = hitung_subtotal(harga, jumlah, member)
    print(f"subtotal {nama_barang}: Rp{subtotal}")
    total += subtotal

print(f"Total belanja: Rp{total}")