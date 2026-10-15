daftar_file = ["main.py", "laporan.pdf", "foto.png", "test_string.py"]

for file in daftar_file:
    if file.endswith(".py"):
        print(f"{file} adalah kode Python.")
    elif file.endswith(".pdf"):
        print(f"{file} adalah dokumen PDF.")
    elif file.endswith(".png"):
        print(f"{file} adalah file gambar PNG.")
    else:
        print(f"{file} adalah jenis file lain.")