import Buku,sqlite3
class Cerpen(Buku.Buku):
    def __init__(self):
        super().__init__()
        self.namaTable = 'cerpen'
        self.kolom = ['id_cerpen', 'judul_cerpen', 'nama_pengarang', 'harga_buku', 'tebal_buku', 'tahun_terbit']
        self.createTable()
    def createTable(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS cerpen(id_cerpen INTEGER, judul_cerpen, nama_pengarang, harga_buku, tebal_buku, tahun_terbit, id_kategori INTEGER, PRIMARY KEY(id_cerpen))')
        cursor.close()
        con.close()
    def showBuku(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM " + self.namaTable + " INNER JOIN kategori ON kategori.id_kategori = " + self.namaTable + ".id_kategori")
        print("ID || Nama  || Pengarang ||  Harga  ||  Tebal  || Tahun Terbit || Kategori")
        for row in cursor.fetchall():
            print(str(row[0]) + ' ||  ' + row[1] + ' || ' + row[2] + '  ||   ' + row[3] + '  ||  ' + row[4] + ' ||  ' +
                  row[5] + '  ||  ' + row[8])
        cursor.close()
        con.close()