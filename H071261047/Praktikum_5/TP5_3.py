ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    posisi = ALFABET.find(ch.lower())
    if posisi == -1:
        return ch
    baru = ALFABET[(posisi + k) % 26]
    if ch == ch.upper():
        return baru.upper()
    return baru

def mesin_enkripsi(teks, k):
    hasil = ""
    for karakter in teks:
        hasil = hasil + cek_sandi(karakter, k)
    return hasil 

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil

sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")

print()
print("Output Deskripsi:", retas_sandi(sandi, kata_kunci))