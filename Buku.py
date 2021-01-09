import sqlite3
import Kategori
class Buku(Kategori.Kategori):
    def __init__(self):
        super().__init__()
        self.namaTable = 'buku'
        self.kolom = ['id_buku', 'judul_buku', 'nama_pengarang', 'harga_buku', 'tebal_buku', 'tahun_terbit']
        self.buku = []
    def addBuku(self):
        for i in self.kolom:
            data = input("Masukkan " + i + ": ")
            self.buku.append(data)
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM kategori")
        print('ID Jenis_kategori')
        for row in cursor.fetchall():
            print(str(row[0]) + '     ' + row[1])
        cursor.close()
        con.close()
        kat = input("Masukkan Nomor Kategori: ")
        self.buku.append(kat)
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO "+ self.namaTable +" VALUES(?,?,?,?,?,?,?)",(self.buku[0],self.buku[1],self.buku[2],self.buku[3],self.buku[4],self.buku[5],self.buku[6]))
            con.commit()
            self.buku = []
            cursor.close()
            con.close()
        except:
            con.rollback()
            print("gagal")
    def showBuku(self):
        pass
    def updateBuku(self):
        self.showBuku()
        id = int(input("Masukkan Id Yang Akan Diupdate: "))
        kolom = int(input("Masukkan Kolom Yang Akan Diupdate: "))
        if kolom == 5:
            con = sqlite3.connect('data.db')
            cursor = con.cursor()
            cursor.execute("SELECT * FROM kategori")
            print('ID Jenis_kategori')
            for row in cursor.fetchall():
                print(str(row[0]) + '     ' + row[1])
            cursor.close()
            con.close()
        data = input("Masukkan Data Baru: ")
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        try:
            kolom = self.kolom[kolom-1]
            cursor.execute("UPDATE " + self.namaTable + " SET "+ kolom + " = ? WHERE " + self.kolom[0] + "= ?", (data,id))
            con.commit()
            cursor.close()
            con.close()
            print("berhasil")
        except:
            con.rollback()
            print("gagal")
    def hapusBuku(self):
        self.showBuku()
        id = input("Masukkan Id Yang Akan Dihapus: ")
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM " + self.namaTable + " WHERE " + self.kolom[0] + " = ?",(id))
            con.commit()
            cursor.close()
            con.close()
        except:
            con.rollback()
            print("Gagal")
    def createTable(self):
        pass
buku = Buku()