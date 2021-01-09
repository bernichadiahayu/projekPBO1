import sqlite3
class Pegawai:
    def __init__(self):
        self.createTable()
    def createTable(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS pegawai(username TEXT, nama_pegawai TEXT, alamat TEXT, no_handphone TEXT, password TEXT, PRIMARY KEY(username))')
        cursor.close()
        con.close()
    def showPegawai(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM pegawai")
        print("Username ||  Nama Pegawai  || Alamat  || no_handpone")
        for row in cursor.fetchall():
            print(str(row[0]) + '     ' + row[1] + '      ' + row[2]  + '      ' + row[3])
        cursor.close()
        con.close()
        menu = ['Tambah Pegawai']
        for i in range(len(menu)):
            print(str(i + 1) + ". " + menu[i])
        pil = int(input("Masukkan Pilihan: "))
        if pil == 1:
            self.tambahPegawai()
    def tambahPegawai(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        data = []
        pegawai = ['username','Nama Pegawai','Alamat','nomor Handphone', 'Password']
        for i in pegawai:
            inp = input("Masukkan " + i + ": ")
            data.append(inp)
        try:
            cursor.execute("INSERT INTO pegawai VALUES(?,?,?,?,?)", (data[0], data[1],data[2],data[3],data[4]))
            con.commit()
            cursor.close()
            con.close()
            self.dataKat = []
            print("Berhasil Menambah Kategori")
        except:
            print("Gagal")