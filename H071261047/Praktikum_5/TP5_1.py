def bersihkan_teks(teks):
    hasil = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    for karakter in teks:
        huruf_kecil = karakter.lower()
        if huruf_kecil in alfabet:
             hasil = hasil + huruf_kecil
    return hasil

def cek_palinrome(teks):
    balik = "".join(reversed(teks))
    if teks == balik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != balik[i]:
            return (False, i)
         
def inti_palinrome(teks): 
    terbaik = ""
    indeks_awal = 0

    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            potongan =  teks[i:j]
            cek = cek_palinrome(potongan)
            if cek [0] and len(potongan) > len(terbaik):
                terbaik = potongan
                indeks_awal = i
    return {"teks": terbaik, "panjang": len(terbaik), "indeks_awal": indeks_awal}

teks_asli = input("Masukkan teks prasasti: ")
teks_bersih = bersihkan_teks(teks_asli)
hasil = inti_palinrome(teks_bersih) 

print("\n")
print("teks bersih:", teks_bersih)
print("outpot terharga:", hasil)