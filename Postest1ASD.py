#Nurul Asmita(2309116073)
#Program Pendataan Toko Olahraga

import os
os. system

class TokoOlahraga:
    def __init__(self, kode_barang, nama_barang, harga_barang, stok_barang,kategori):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.harga_barang = harga_barang
        self.stok_barang = stok_barang
        self.kategori = kategori

class PendataanTokoOlahraga:
    def __init__(self):
        self.data_barang = []
        
#Fungsi menambahkan data barang
    def tambah_barang(self,toko_olahraga):
        self.data_barang.append(toko_olahraga)
        print("*****Barang berhasil ditambahkan*****\n")
        
#Fungsi Menampilkan data barang
    def lihat_barang(self):
        if self.data_barang:
            for toko_olahraga in self.data_barang:
                print(f"Kode Barang: {toko_olahraga.kode_barang}")
                print(f"Nama Barang: {toko_olahraga.nama_barang}")
                print(f"Harga Barang: {toko_olahraga.harga_barang}")
                print(f"Stok Barang: {toko_olahraga.stok_barang}")
                print(f"Kategori: {toko_olahraga.kategori}")
                print()
        else:
            print("*****Barang yang anda masukkan tidak terdaftar*****\n")
            
#Fungsi mengupdate data barang
    def update_barang(self, kode_barang, nama_barang, harga_barang, stok_barang, kategori):
        for toko_olahraga in self.data_barang:
            if toko_olahraga.kode_barang == kode_barang:
                toko_olahraga.nama_barang = nama_barang
                toko_olahraga.harga_barang = harga_barang
                toko_olahraga.stok_barang = stok_barang
                toko_olahraga.kategori = kategori
                print("*****Barang berhasil di update*****\n")
                return
            print("*****Barang dengan kode", kode_barang, "tidak ditemukan*****")

#Fungsi menghapus data barang
    def hapus_barang(self, kode_barang):
        barang_dihapus = False
        for toko_olahraga in self.data_barang:
            if toko_olahraga.kode_barang == kode_barang:
                self.data_barang.remove(toko_olahraga)
                barang_dihapus = True
                break
        if barang_dihapus:
                print("*****Barang berhasil di hapus*****\n")
        else:
            print("*****Barang dengan kode", kode_barang, "tidak ditemukan*****")
            

#Fungsi Main program pendataan Toko Olahraga
def main():
    Toko_Olahraga = PendataanTokoOlahraga()
    
    while True:
        print("="*5,"Menu Toko Olahraga","="*5)
        print("="*30,"\n")
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Keluar")
        
        pilihan = input("Pilih menu Yang diinginkan:")
        
        if pilihan == '1':
            kode_barang = input("Masukkan kode barang: ")
            nama_barang = input("Masukkan nama barang: ")
            harga_barang = float(input("Masukkan harga barang: "))
            stok_barang = int(input("Masukkan stok barang: "))
            kategori = input("Masukkan kategori barang: ")
            barang_baru = TokoOlahraga(kode_barang, nama_barang, harga_barang, stok_barang, kategori)
            Toko_Olahraga.tambah_barang(barang_baru)
        elif pilihan == '2':
            Toko_Olahraga.lihat_barang()
        elif pilihan == '3':
            kode_barang = input("Masukkan kode barang: ")
            nama_barang = input("Masukkan nama barang: ")
            harga_barang = float(input("Masukkan harga barang: "))
            stok_barang = int(input("Masukkan stok barang: "))
            kategori = input("Masukkan kategori barang: ")
            Toko_Olahraga.update_barang(kode_barang, nama_barang, harga_barang, stok_barang, kategori)
        elif pilihan == '4':
            kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
            Toko_Olahraga.hapus_barang(kode_barang)
        elif pilihan == '5':
            print("*****Pendataan di Toko Olahraga telah selesai*****")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia2")
            
if __name__ == "__main__":
    main()