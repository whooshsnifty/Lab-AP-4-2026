from datetime import datetime #u/ ambil tgl & waktu saat ini
import random #u/ menghasilkan angka secara acak
import os #u/ kelola  folder dan lokasi file

folder_saat_ini = os.path.dirname(os.path.abspath(__file__) 
#u/ cari lokasi folder tempat program disimpan
#___file___ u/ tunjukkan file mana yg dijalankan

folder_invoices = os.path.join(folder_saat_ini, "invoices") 
#u/ gabungkan alamat folder dg nama folder lain
#"invoices" nama folder u/ simpan file invoice

file_history = os.path.join(folder_saat_ini, "trx_history.txt")
#u/ gabungkan lokasi folder dgn nama file trx history

os.makedirs(folder_invoices, exist_ok=True)
#u/ buat folder kalau blm ada, True = agar tdk eror kalau folder invoices sdh ada

def membuat_invoices(kasir, data_produk): #fungsi u/ buat invoice sekaligus tambah transaksi ke riwayat
    waktu_sekarang = datetime.now().strftime("%Y%m%d%H%M%S") #u/ ambil tgl, wkt saat ini
    #strftime ubah jadi teks dg format Y,m,d,H,M,S
    id_nama = kasir[:3].upper() #ambil 3 huruf pertama nama kasir, ubah jadi kapital
    id_tahun = waktu_sekarang[2:4] #ambil karakter dr indeks 2 sampai sblm 4
    id_bulan = waktu_sekarang[4:6] #indeks 4-sblm 6 untuk bulan
    id_tanngal = waktu_sekarang[6:8] 
    id_jam_menit = waktu_sekarang[8:12]
    angka_random = random.randint(100, 999) #u/ ambil angka acak termasuk kedua batasnya
    border = "=" * 79 
    border1 = "|" + "Nama".center(38) + "|" + "Harga".center(14) + "|" + "Jumlah".center(8) + "|" + "Total".center(14) + "|"
    total_keseluruhan = 0
    total_item = 0
    nama_file = f"{id_nama}{id_tahun}{id_bulan}{id_tanngal}{id_jam_menit}{angka_random}.txt"
    file_dalam_folder = os.path.join(folder_invoices, nama_file) #u/ gabungkan lokasi folder & nama file
    with open(file_dalam_folder, "w") as o: #u/ membuka file, sesuai lokai file yg ingin dibuka
    #w=u/ menulis isi ke file. nama o sbg variabel u/ akses file tsb
        o.write(f"TOKO {kasir.capitalize()}".center(100)) 
        o.write("\n")
        o.write("=" * 100)
        o.write("\nNama kasir".ljust(20) + f": {kasir}")
        o.write("\nWaktu transaksi".ljust(20) + f": {id_tanngal}/{id_bulan}/{id_tahun} {waktu_sekarang[8:10]}:{waktu_sekarang[10:12]}")
        o.write("\n")
        o.write("=" * 100)
        o.write("\n")
        o.write("\n")
        o.write("Daftar Produk".center(100))
        o.write("\n")
        o.write("\n" + border.center(100))
        o.write("\n" + border1.center(100))
        o.write("\n" + border.center(100))
        for i in data_produk: #perulangan u/ setiap produk yg ada di data_produk
            total_item = i["Harga"] * i["Jumlah"]
            hasil = "| " + f"{i["Nama"]}".ljust(37) + "|" + f"Rp{i["Harga"]}".rjust(13) + " |" + f"{i["Jumlah"]}".center(8) + "|" + f"Rp{total_item}".rjust(13) + " |"
            o.write("\n" + hasil.center(100)) #o.write, menulis teks ke file
            total_keseluruhan += total_item 
        border_total = "|" + "TOTAL".center(38) + "|".rjust(25) + f"Rp{total_keseluruhan}".rjust(13) + " |"
        o.write("\n" + border.center(100))
        o.write("\n" + border_total.center(100))
        o.write("\n" + border.center(100))
        o.write("\n")
        o.write("\n")
        o.write("=" * 100)
        o.write("\n" + "TERIMAKASIH TELAH BELANJA".center(100))
        o.write("\n")
        o.write("=" * 100 + "\n")
    with open(file_history, "a") as isi: #u/ buka file trx supaya bs tambah riwayat trnsaksi tanpa hps data sblmnya
    #with, memastikan file ditutup otomatis setelah digunakan. isi= nm variabel u/ akses file
        isi.write("\n| " + f"{id_tanngal}/{id_bulan}/{id_tahun} {waktu_sekarang[8:10]}:{waktu_sekarang[10:12]}".ljust(28) + "| " + f"{id_nama}{id_tahun}{id_bulan}{id_tanngal}{id_jam_menit}{angka_random}".ljust(29) + "|" + f"Rp{total_keseluruhan}".rjust(26) + " |")
        isi.write("\n" + ("=" * 90))
    print("=" * 54)
    print("TRANSAKSI BERHASIL".center(54))
print("=" * 54)
print("SELAMAT DATANG".center(54))
print("=" * 54)
nama_kasir = input("Masukkan nama kasir".ljust(35) + ": ")
while True: #perulangan smpai program dihentikan dg kondisi tertentu/perintah break
    print("=" * 54)
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. keluar")
    print("=" * 54)
    pilih_opsi = input("Masukkan opsi pilihan".ljust(35) + ": ")
    print("=" * 54)
    if pilih_opsi == "1":
        data_list = [] #u/ simpan data produk yg dimasukkab dlm transaksi
        while True:
            try:
                nama_produk = input("Masukkan nama produk".ljust(35) + ": ")
                harga_produk = int(input("Masukkan harga produk".ljust(35) + ": "))
                jumlah_produk = int(input("Masukkan jumlah produk".ljust(35) + ": "))
                data = { #u/ simpan informasi satu produk dlm bntuk dictionary
                    "Nama": nama_produk,
                    "Harga": harga_produk,
                    "Jumlah": jumlah_produk,
                    }
                data_list.append(data) #tambahkan data produk ke dalam list data_list
                Tambah = True  #true krn blm memilih y/t
                Keluar = True
                while Tambah == True:
                    print("=" * 54)
                    tambah_produk = input("Tambah produk? (y/t)".ljust(35) + ": ")
                    print("=" * 54)
                    if tambah_produk == "y":
                        Tambah = False
                    elif tambah_produk == "t":
                        Keluar = False
                        break
                    else:
                        print("Input yang anda masukkan tidak valid")
                        continue
                if Keluar == False:
                    membuat_invoices(nama_kasir, data_list)
                    break
            except:
                print("Harga yang anda masukkan tidak valid")
                continue
    elif pilih_opsi == "2":
        id_transaksi = input("Masukkan ID transaksi".ljust(35) + ": ")
        lokasi_file_folder = os.path.join(folder_invoices, id_transaksi+".txt")
        if os.path.isfile(lokasi_file_folder):
            with open(lokasi_file_folder, "r") as ada: #buka file invoice yg dicari, lalu baca
                isi = ada.read() #baca seluruh file dan simpan ke variabel isi
                print("=== ISI FILE ===")
                print(isi) #menampilkan isi invoice yg sdh dibaca ke terminal
        else:
            print(f"File '{id_transaksi}' tidak ditemukan.")
    elif pilih_opsi == "3":
        print("Terimas kasih!")
        break
    else:
        print("Opsi yang anda pilih tidak valid!")