def konversi_suhu(suhu, asal, tujuan):
    asal = asal.upper()
    tujuan =  tujuan.upper()

    if asal not in ("C", "F", "K") or tujuan not in ("C", "F", "K"):
        raise ValueError("skala suhu tidak dikenali")

    if asal == "C":
        celcius = suhu
    elif asal == "F":
        celcius = (suhu - 32) * 5  / 9
    else:
        celcius = suhu - 273.15

    if tujuan == "C":
        return celcius
    elif tujuan  ==  "F":
        return celcius * 9 / 5 + 32
    else:
        return celcius +  273.15
    
print("=== konversi suhu ===")
while True:
    teks = input("masukkan suhu(atau 'selesai' untuk keluar): ")
    if teks.lower() == "selesai":
        break
    asal  = input("skala asal (C/F/K): ")
    tujuan = input("skala tujuan (C//F/K): ")

    try:
        suhu = float(teks)
        hasil = konversi_suhu(suhu, asal, tujuan)
        print(f"hasil: {suhu} {asal.upper()} = {hasil} {tujuan.upper()}")
    except ValueError:
        print("error: skala suhu tidak dikenali")