class Kariawan:
    def __init__(self, nama, usia, gaji_pokok):
        self.nama = nama
        self.usia = usia
        self.gaji_pokok = gaji_pokok

    def info(self):
        print("Nama:", self.nama, 
              "Usia:", self.usia, 
              "Gaji Pokok:", self.gaji_pokok)


class Manager(Kariawan):
    def __init__(self, nama, usia, gaji_pokok, tunjangan):   
        super().__init__(nama, usia, gaji_pokok)       
        self.tunjangan = tunjangan

    def info(self):
        print("Nama:", self.nama, 
              "Usia:", self.usia, 
              "Gaji Pokok:", self.gaji_pokok, 
              "Tunjangan:", self.tunjangan)


class Staff(Kariawan):
    def __init__(self, nama, usia, gaji_pokok, lembur, uang_lembur):  
        super().__init__(nama, usia, gaji_pokok)
        self.lembur = lembur
        self.uang_lembur = uang_lembur

    def info(self):
        print("Nama:", self.nama,
              "Usia:", self.usia, 
              "Gaji Pokok:", self.gaji_pokok, 
              "Lembur (jam):", self.lembur, 
              "Uang lembur/jam:", self.uang_lembur)


# ==== PROGRAM UTAMA ====
print("=== Input Data Perusahaan BAC ===")
kategori = input("Masukkan jenis karyawan (Manager/Staff): ")

if kategori.lower() == "manager":
    nama = input("Masukkan Nama: ")
    usia = input("Masukkan Usia: ")
    gaji_pokok = input("Masukkan Gaji Pokok: ")
    tunjangan = input("Masukkan Tunjangan: ")
    karyawan = Manager(nama, usia, gaji_pokok, tunjangan)

elif kategori.lower() == "staff":
    nama = input("Masukkan Nama: ")
    usia = input("Masukkan Usia: ")
    gaji_pokok = input("Masukkan Gaji Pokok: ")
    lembur = input("Masukkan jumlah jam lembur: ")
    uang_lembur = input("Masukkan uang lembur per jam: ")
    karyawan = Staff(nama, usia, gaji_pokok, lembur, uang_lembur)

else:
    print("Tidak ada di pilihan")
    karyawan = None

if karyawan:
    print("\n=== Data Kariawan ===") 
    karyawan.info()

