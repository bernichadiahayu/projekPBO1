import Novel,Komik,Cerpen,sqlite3,datetime,Majalah
class Transaksi:
    def __init__(self,username):
        self.username = username
        self.novel = {'id_novel': [], 'jumlah': []}
        self.cerpen = {'id_cerpen': [], 'jumlah': []}
        self.komik = {'id_komik': [], 'jumlah': []}
        self.majalah = {'id_majalah': [], 'jumlah': []}
        self.createTable()
    def addCart(self):
        buku = ['Novel', 'Cerpen', 'Komik', 'Majalah']
        for i in range(len(buku)):
            print(str(i + 1) + ". " + buku[i])
        pil = int(input("Masukkan Pilihan: "))
        if pil == 1:
            novel = Novel.Novel()
            novel.showBuku()
            pilihan = int(input("Masukkan Id Buku :"))
            jumlah = int(input("Masukkan Jumlah :"))
            self.novel['id_novel'].append(pilihan)
            self.novel['jumlah'].append(jumlah)
        elif pil == 2:
            cerpen = Cerpen.Cerpen()
            cerpen.showBuku()
            pilihan = int(input("Masukkan Id Buku :"))
            jumlah = int(input("Masukkan Jumlah :"))
            self.cerpen['id_cerpen'].append(pilihan)
            self.cerpen['jumlah'].append(jumlah)
        elif pil == 3:
            komik = Komik.Komik()
            komik.showBuku()
            pilihan = int(input("Masukkan Id Buku :"))
            jumlah = int(input("Masukkan Jumlah :"))
            self.komik['id_komik'].append(pilihan)
            self.komik['jumlah'].append(jumlah)

        elif pil == 4:
            majalah = Majalah.Majalah()
            majalah.showBuku()
            pilihan = int(input("Masukkan Id Buku :"))
            jumlah = int(input("Masukkan Jumlah :"))
            self.majalah['id_majalah'].append(pilihan)
            self.majalah['jumlah'].append(jumlah)
    def beli(self):
        con = sqlite3.connect('data.db')
        fix = {'judul_buku': [], 'harga': [], 'total': 0,'jumlah': []}
        if len(self.novel['id_novel']) > 0:
            cur1 = con.cursor()
            data = {'harga':[]}
            for i in range(len(self.novel['id_novel'])):
                cur1.execute("SELECT * FROM novel WHERE id_novel = " + str(self.novel['id_novel'][i]))
                novel = cur1.fetchone()
                data['harga'].append(novel[3])
                fix['judul_buku'].append(novel[1])
                fix['harga'].append(novel[3])
            harga = 0
            for j in range(len(data['harga'])):
                harga += int(data['harga'][j]) * self.novel['jumlah'][j]
                fix['jumlah'].append(self.novel['jumlah'][j])
            fix['total'] += harga
            cur1.close()
        if len(self.cerpen['id_cerpen']) >0:
            cur2 = con.cursor()
            data = {'harga': []}
            for i in range(len(self.cerpen['id_cerpen'])):
                cur2.execute("SELECT * FROM cerpen WHERE id_cerpen = " + str(self.cerpen['id_cerpen'][i]))
                cerpen = cur2.fetchone()
                data['harga'].append(cerpen[3])
                fix['judul_buku'].append(cerpen[1])
                fix['harga'].append(cerpen[3])
            harga = 0
            for j in range(len(data['harga'])):
                harga += int(data['harga'][j]) * self.cerpen['jumlah'][j]
                fix['jumlah'].append(self.cerpen['jumlah'][j])
            fix['total'] += harga
            cur2.close()
        if len(self.majalah['id_majalah']) >0:
            cur3 = con.cursor()
            data = {'harga': []}
            for i in range(len(self.majalah['id_majalah'])):
                cur3.execute("SELECT * FROM majalah WHERE id_majalah = " + str(self.majalah['id_majalah'][i]))
                majalah = cur3.fetchone()
                data['harga'].append(majalah[3])
                fix['judul_buku'].append(majalah[1])
                fix['harga'].append(majalah[3])
            harga = 0
            for j in range(len(data['harga'])):
                harga += int(data['harga'][j]) * self.majalah['jumlah'][j]
                fix['jumlah'].append(self.majalah['jumlah'][j])
            fix['total'] += harga
            cur3.close()
        self.invoice(fix)
    def invoice(self,data):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        tanggal = datetime.date.today()
        cursor.execute("INSERT INTO transaksi(username,tanggal_pembelian,total) VALUES (?,?,?)",(self.username,tanggal,data['total']))
        con.commit()
        cursor.execute("SELECT id_transaksi FROM transaksi ORDER BY id_transaksi DESC")
        id = cursor.fetchone()
        print("Tanggal: " + str(tanggal))
        print("Kasir: " + self.username)
        print("Judul Buku \t Jumlah Buku \t Harga")
        for i in range(len(data['judul_buku'])):
            print(data['judul_buku'][i] + '\t '+ str(data['jumlah'][i]) + '\t Rp.' + str(data['harga'][i]))
            cursor.execute("INSERT INTO transaksi_detail(id_transaksi,judul_buku,harga,jumlah) VALUES(?,?,?,?)",(id[0],data['judul_buku'][i],data['harga'][i],data['jumlah'][i]))
            con.commit()
        print("Total Harga: Rp." + str(data['total']))
        print("-----------Terima Kasih Sudah Berbelanja----------")
        self.novel = {'id_novel': [], 'jumlah': []}
        self.cerpen = {'id_cerpen': [], 'jumlah': []}
        self.komik = {'id_komik': [], 'jumlah': []}
    def createTable(self):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS transaksi(id_transaksi Integer PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, tanggal_pembelian DATE, total INTEGER)')
        cursor.execute('CREATE TABLE IF NOT EXISTS transaksi_detail(id_detail Integer PRIMARY KEY AUTOINCREMENT NOT NULL,id_transaksi, judul_buku TEXT, harga INTEGER, jumlah INTEGER)')
        cursor.close()
        con.close()
    def showCart(self):
        con = sqlite3.connect('data.db')
        cur2 = con.cursor()
        print("Judul Buku   Harga Buku     Jumlah")
        if len(self.novel['id_novel']) > 0:
            for i in range(len(self.novel['id_novel'])):
                cur2.execute("SELECT judul_novel,harga_buku FROM novel WHERE id_novel = " + str(self.novel['id_novel'][i]))
                data = cur2.fetchone()
                print(str(i + 1) + '. ' + data[0] + "  " + data[1] + "    "+str(self.novel['jumlah'][i]))

        if len(self.cerpen['id_cerpen']) >0:
            for i in range(len(self.cerpen['id_cerpen'])):
                cur2.execute("SELECT judul_cerpen,harga_buku FROM cerpen WHERE id_cerpen = " + str(self.cerpen['id_cerpen'][i]))
                data = cur2.fetchone()
                print(str(i + 1) + '. ' + data[0] + "  " + data[1] + "    "+str(self.cerpen['jumlah'][i]))
        if len(self.komik['id_komik']) >0:
            for i in range(len(self.komik['id_komik'])):
                cur2.execute("SELECT judul_komik,harga_buku FROM komik WHERE id_komik = " + str(self.komik['id_komik'][i]))
                data = cur2.fetchone()
                print(str(i + 1) + '. ' + data[0] + "  " + data[1] + "    "+str(self.komik['jumlah'][i]))
        if len(self.majalah['id_majalah']) >0:
            for i in range(len(self.majalah['id_majalah'])):
                cur2.execute("SELECT judul_majalah,harga_buku FROM majalah WHERE id_majalah = " + str(self.majalah['id_majalah'][i]))
                data = cur2.fetchone()
                print(str(i + 1) + '. ' + data[0] + "  " + data[1] + "    "+str(self.majalah['jumlah'][i]))
        cur2.close()
        con.close()
    def deleteCart(self):
        self.novel = {'id_novel': [], 'jumlah': []}
        self.cerpen = {'id_cerpen': [], 'jumlah': []}
        self.komik = {'id_komik': [], 'jumlah': []}