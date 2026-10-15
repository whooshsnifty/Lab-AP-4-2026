def perbaiki_pesan(pesan):
    if "dtg" in pesan:
        return pesan.replace("dtg", "datang")
    elif "gk" in pesan:
        return pesan.replace("gk", "tidak")
    elif "tugas" in pesan:
        return pesan.replace("tugas", "pekerjaan")
    else:
        return pesan
daftar_pesan = ["yg penting dtg tepat waktu", "gk ada yg dtg hari ini", "tugas sudah dikumpul"]
daftar_pesan_perbaikan = [perbaiki_pesan(pesan) for pesan in daftar_pesan]

print(f"Pesan asli: {daftar_pesan}")
print(f"Pesan perbaikan: {daftar_pesan_perbaikan}")
