class Peserta:
    def __init__(self, nama, nilai_tugas, nilai_uts, nilai_uas):
        self.nama = nama
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas

    def tampilkan_data(self):
        print("Nama Peserta :", self.nama)
        print("Nilai Tugas  :", self.nilai_tugas)
        print("Nilai UTS    :", self.nilai_uts)
        print("Nilai UAS    :", self.nilai_uas)

    def hitung_nilai_akhir(self):
        return (self.nilai_tugas * 0.30) + \
               (self.nilai_uts * 0.30) + \
               (self.nilai_uas * 0.40)

    def cek_kelulusan(self):
        if self.hitung_nilai_akhir() >= 70:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def hitung_grade(self):
        nilai = self.hitung_nilai_akhir()

        if nilai >= 85:
            return "A"
        elif nilai >= 75:
            return "B"
        elif nilai >= 65:
            return "C"
        elif nilai >= 50:
            return "D"
        else:
            return "E"