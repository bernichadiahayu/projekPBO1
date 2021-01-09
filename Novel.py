import Buku,sqlite3
class Novel(Buku.Buku):
    def __init__(self):
        super().__init__()
        self.namaTable = 'novel'
        self.kolom = ['id_novel', 'judul_novel', 'nama_pengarang', 'harga_buku', 'tebal_buku', 'tahun_terbit']
        self.createTable()
    def createTable(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS novel(id_novel INTEGER, judul_novel, nama_pengarang, harga_buku, tebal_buku, tahun_terbit, id_kategori INTEGER, PRIMARY KEY(id_novel))')
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