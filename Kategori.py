import sqlite3
class Kategori:
    def __init__(self):
        self.dataKat = []
        self.kategori = ['id_kategori','jenis_kategori']
        self.createTable()
    def addKategori(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        for i in self.kategori:
            data = input("Masukkan " + i + ": ")
            self.dataKat.append(data)
        try:
            cursor.execute("INSERT INTO kategori VALUES(?,?)",(self.dataKat[0],self.dataKat[1]))
            con.commit()
            cursor.close()
            con.close()
            self.dataKat = []
            print("Berhasil Menambah Kategori")
        except:
            print("Gagal")
    def showKategori(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM kategori")
        print('ID Jenis_kategori')
        for row in cursor.fetchall():
            print(str(row[0]) + '     ' + row[1])
        cursor.close()
        con.close()
        menu = ['Tambah Kategori', 'Update Kategori', 'Hapus Kategori']
        for i in range(len(menu)):
            print(str(i + 1) + ". " + menu[i])
        pil = int(input("Masukkan Pilihan: "))
        if pil == 1:
            self.addKategori()
        elif pil == 2:
            self.updateKategori()
        elif pil == 3:
            self.hapusKategori()
    def updateKategori(self):
        id = int(input("Masukkan Id Yang Akan Diupdate: "))
        data = input("Masukkan Nama Kategori Baru: ")
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        try:
            cursor.execute("UPDATE kategori SET  jenis_kategori = ? WHERE id_kategori = ?", (data, id))
            con.commit()
            cursor.close()
            con.close()
            print("berhasil")
        except:
            con.rollback()
            print("gagal")

    def hapusKategori(self):
        id = input("Masukkan Id Yang Akan Dihapus: ")
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM kategori WHERE id_kategori = ?", (id))
            con.commit()
            cursor.close()
            con.close()
        except:
            con.rollback()
            print("Gagal")

    def createTable(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS kategori(id_kategori Integer, jenis_kategori TEXT, PRIMARY KEY(id_kategori))')
        cursor.close()
        con.close()