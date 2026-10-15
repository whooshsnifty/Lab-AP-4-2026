def deteksi_anomali_email(email):
    error = []

    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    posisi_at = email.find("@")
    local = email[:posisi_at]
    domain = email[posisi_at + 1:]

    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
    if " " in email:
        error.append("Tidak boleh mengandung spasi.")
    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Bagian local tidak boleh diawali titik, diakhiri titik, atau mengandung titik berurutan.")
    if domain.count(".") == 0:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
    if not (email.endswith(".com") or email.endswith(".id")):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")
    return error

def cetak_daftar(daftar_email_valid, karakter_border): 
    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    garis = "+" + karakter_border * (terpanjang + 2) + "+"
    hasil = garis + "\n"

    for email in daftar_email_valid:
        spasi = " " * (terpanjang - len(email))
        hasil = hasil + "| " + email + spasi + " |\n" 

    hasil = hasil + garis
    return hasil 

print("--- Sistem Pencatatan email valid ---")
karakter_border = input("Masukkan border dengan karakter bebas: ")

print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []

while True:
    email = input("Masukkan email: ")
    if email == "tutup":
        break 

    error = deteksi_anomali_email(email)
    if email in daftar_valid:
        error.append("Email sudah terdaftar (Duplikat).")

    if len(error) == 0:
        print(">> Email VALID!")
        daftar_valid.append(email)
    else:
        print(">> Email DITOLAK karena: ")
        for pesan in error:
            print("   - " + pesan)

print()
print("--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_valid,  karakter_border))