tujuan = input("Masukkan tujuan (Pantai/pegunungan/Kota): ")
waktu = input("Masukkan waktu (Pagi/Malam): ")
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ")

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print("Paket Rekomendasi: Paket A")
        elif waktu == "Malam" and tipe == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi" and tipe == "Dewasa":
            print("Paket Rekomendasi: Paket B")
        elif waktu == "Malam" and tipe == "Dewasa":
            print("Paket Rekomendasi: paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam":
            print("Paket Rekomendasi: Paket C")
        elif waktu == "Malam" or tipe == "Dewasa":
            print("Paket Rekomendasi: Paket C SMA")
        else:
            print("Tidak ada paket yang cocok")