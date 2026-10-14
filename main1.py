from peserta import Peserta

jumlah = int(input("Jumlah Peserta : "))

daftar_peserta = []

for i in range(jumlah):
    print(f"\nPeserta ke-{i + 1}")

    nama = input("Nama Peserta  : ")
    nilai_tugas = float(input("Nilai Tugas   : "))
    nilai_uts = float(input("Nilai UTS     : "))
    nilai_uas = float(input("Nilai UAS     : "))

    peserta = Peserta(nama, nilai_tugas, nilai_uts, nilai_uas)
    daftar_peserta.append(peserta)

for peserta in daftar_peserta:
    print("\n=== HASIL PENILAIAN ===")
    print("Nama Peserta :", peserta.nama)
    print("Nilai Akhir  :", round(peserta.hitung_nilai_akhir(), 2))
    print("Grade        :", peserta.hitung_grade())
    print("Status       :", peserta.cek_kelulusan())