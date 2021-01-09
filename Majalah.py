import Buku,sqlite3
class Majalah(Buku.Buku):
    def __init__(self):
        super().__init__()
        self.createTable()
    def createTable(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS majalah(id_majalah INTEGER, judul_majalah, penerbit, harga_buku, PRIMARY KEY(id_majalah))')
        cursor.close()
        con.close()

    def addBuku(self,kolom):
        for i in kolom:
            data = input("Masukkan " + i + ": ")
            self.buku.append(data)
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO majalah VALUES(?,?,?,?)",(self.buku[0],self.buku[1],self.buku[2],self.buku[3]))
            con.commit()
            self.buku = []
            cursor.close()
            con.close()
        except:
            con.rollback()
            print("gagal")
    def showBuku(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM majalah")
        print("ID || Nama ||  Penerbit  || Harga Buku")
        for row in cursor.fetchall():
            print(str(row[0]) + ' ||  ' + row[1] + ' || ' + row[2] + '  ||   ' + row[3])
        cursor.close()
        con.close()
    def updateBuku(self,kolom):
        self.showBuku()
        id = int(input("Masukkan Id Yang Akan Diupdate: "))
        colum = int(input("Masukkan Kolom Yang Akan Diupdate: "))
        data = input("Masukkan Data Baru: ")
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        try:
            colum = kolom[colum-1]
            cursor.execute("UPDATE majalah SET "+ colum + " = ? WHERE id_majalah = ?", (data,id))
            con.commit()
            cursor.close()
            con.close()
            print("berhasil")
        except sqlite3.Error as er:
            con.rollback()
            print(er.args)
            print("gagal")
    def hapusBuku(self,kolom):
        self.showBuku()
        id = input("Masukkan Id Yang Akan Dihapus: ")
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM majalah WHERE " + kolom[0] + " = ?",(id))
            con.commit()
            cursor.close()
            con.close()
        except:
            con.rollback()
            print("Gagal")