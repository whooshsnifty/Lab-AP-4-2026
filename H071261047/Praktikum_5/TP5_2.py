def cek_kata(teks, kata):
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    hasil = []
    start = 0 

    while True:
        i = teks_kecil.find(kata_kecil, start)
        if i == -1:
            break
        hasil.append(i)
        start = i + 1 
    return hasil

def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    if i > 0:
        sebelum = teks[i - 1].lower()
        if sebelum in alfabet:
            return False
    akhir = i + panjang 
    if akhir < len(teks):
        sesudah = teks[akhir].lower()
        if sesudah in alfabet:
            return False    
    return True

def sensor_kata(teks, kata, simbol):
    semua = cek_kata(teks, kata)
    panjang = len(kata)
    indeks_sensor = []
    hasil = ""
    posisi = 0

    for i in semua:
        if cek_batas_kata(teks, i, panjang):
            hasil = hasil + teks[posisi:i] + simbol * panjang 
            posisi = i + panjang 
            indeks_sensor.append(i)

    hasil = hasil + teks[posisi:]
    return (hasil, len(indeks_sensor), indeks_sensor)

teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil_teks, jumlah, indeks = sensor_kata(teks, kata, simbol)

print("Hasil Teks:", hasil_teks)
print("jumlah:", jumlah, "| indeks:", indeks)