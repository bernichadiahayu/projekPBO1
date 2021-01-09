import Novel,Komik,Majalah,Cerpen,sqlite3,Transaksi,Pegawai,Kategori
class Main:
    def __init__(self):
        self.kategori = Kategori.Kategori()
        self.login()
    def menu(self):
        print("Pilihan Menu Pengguna")
        menu = ['Show All Book','Kategori Buku','Add Cart', 'Show Cart','Delete Cart','Buy','Lihat Pegawai','Exit']
        for i in range(len(menu)):
            print(str(i+1) +". " + menu[i])
        pil = int(input("Masukkan Pilihan: "))
        if pil == 1:
            self.show()
        elif pil == 2:
            self.kategori.showKategori()
            self.menu()
        elif pil == 3:
            self.tr.addCart()
            self.menu()
        elif pil == 4:
            self.tr.showCart()
            self.menu()
        elif pil == 5:
            self.tr.deleteCart()
            self.menu()
        elif pil == 6:
            self.tr.beli()
            # self.menu()
        elif pil == 7:
            self.pegawai.showPegawai()
            self.menu()
    def show(self):
        buku = ['Novel','Cerpen','Komik','Majalah']
        for i in range(len(buku)):
            print(str(i + 1) + ". " + buku[i])
        pil = int(input("Masukkan Pilihan: "))
        if pil == 1:
            menu = ['Tambah Buku','Update Buku', 'Hapus Buku','Kembali ke menu']
            novel = Novel.Novel()
            novel.showBuku()
            for i in range(len(menu)):
                print(str(i + 1) + ". " + menu[i])
            men = int(input("Masukkan Pilihan: "))
            if men == 1:
                novel.addBuku()
                novel.showBuku()
                self.menu()
            elif men == 2:
                novel.updateBuku()
                self.menu()
            elif men == 3:
                novel.hapusBuku()
                self.menu()
            elif men==4:
                self.menu()
            else:
                self.menu()
        elif pil == 2:
            menu = ['Tambah Buku', 'Update Buku', 'Hapus Buku','Kembali ke menu']
            cerpen = Cerpen.Cerpen()
            cerpen.showBuku()
            for i in range(len(menu)):
                print(str(i + 1) + ". " + menu[i])
            men = int(input("Masukkan Pilihan: "))
            if men == 1:
                cerpen.addBuku()
                cerpen.showBuku()
                self.menu()
            elif men == 2:
                cerpen.updateBuku()
                self.menu()
            elif men == 3:
                cerpen.hapusBuku()
                self.menu()
            elif men==4:
                self.menu()
            else:
                self.menu()
        elif pil == 3:
            menu = ['Tambah Buku', 'Update Buku', 'Hapus Buku','Kembali ke menu']
            komik = Komik.Komik()
            komik.showBuku()
            for i in range(len(menu)):
                print(str(i + 1) + ". " + menu[i])
            men = int(input("Masukkan Pilihan: "))
            if men == 1:
                komik.addBuku()
                komik.showBuku()
                self.menu()
            elif men == 2:
                komik.updateBuku()
                self.menu()
            elif men == 3:
                komik.hapusBuku()
                self.menu()
            else:
                self.menu()
        elif pil == 4:
            menu = ['Tambah Buku', 'Update Buku', 'Hapus Buku']
            majalah = Majalah.Majalah()
            majalah.showBuku()
            kolom = ['id_majalah', 'judul_majalah', 'penerbit', 'harga_buku']
            for i in range(len(menu)):
                print(str(i + 1) + ". " + menu[i])
            men = int(input("Masukkan Pilihan: "))
            if men == 1:

                majalah.addBuku(kolom)
                majalah.showBuku()
                self.menu()
            elif men == 2:
                majalah.updateBuku(kolom)
                self.menu()
            elif men == 3:
                majalah.hapusBuku(kolom)
                self.menu()
            elif men==4:
                self.menu()
            else:
                self.menu()
    def login(self):
        self.pegawai = Pegawai.Pegawai()
        print("-------------SELAMAT DATANG DI SMARTBOOK------------")
        print("--------------------Login Kasir---------------------")
        username = input("Masukkan Username: ")
        password = input("Masukkan password: ")
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM pegawai")
        for row in cursor.fetchall():
            if username == row[0] and password == row[4]:
                self.username = username
                self.tr = Transaksi.Transaksi(row[1])
                self.menu()
                break
        else:
            print("Akun TIdak Ada")

main = Main()