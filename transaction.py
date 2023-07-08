# Pembuatan class dengan nama transaksi yang akan menyimpan item yang dibeli dalam sebuah list kosong
class Transaction:
    """
    Methods
    
    add_item : menambahkan item pada list belanja
            
    update_item_name : mengganti nama item pada list belanja
            
    update_item_quantity : mengganti jumlah item pada list belanja
            
    update_item_price : mengganti harga item pada list belanja
            
    delete_item : menghapus item pada list belanja
            
    reset_item : menghapus semua item pada list belanja
    
    check_order : mengecek kebenaran input data list belanja
    
    show_item : menampilkan nama item, jumlah item, harga satuan dan total harga
            
    total_price : menampilkan total harga dan diskon yang diberikan
    """
    def __init__(self):
        self.items = []

    # Menambahkan method yang berfungsi menambahkan item ke dalam list belanja
    def add_item(self, item):
        """
        Fungsi : Menambahkan item pada list item belanja.

        Parameter:
        item : Berupa list yang berisi nama, jumlah, dan harga item.

        Output:
        Pesan yang memberitahu bahwa item sudah berhasil ditambahkan ke dalam list belanja.
        """
        self.items.append(item)
        print("-" * 60)
        print(f"{item} telah berhasil ditambahkan ke keranjang")
        self.show_item()

    # Menambahkan method yang berfungsi mengganti nama item ke dalam list belanja
    def update_item_name(self, old_name, new_name):
        """
        Fungsi : Mengganti nama item pada list belanja.

        Parameter:
        old_name (string): Nama item yang akan diganti.
        new_name (string): Nama baru untuk item yang akan diganti.

        Output:
        Pesan yang memberitahu bahwa nama item sudah berhasil diubah.
        """
        for item in self.items:
            if item[0] == old_name:
                item[0] = new_name

        print(f"Item {old_name} telah berhasil diubah menjadi {new_name}")
        self.show_item()

    # Menambahkan method yang berfungsi mengganti jumlah item ke dalam list belanja
    def update_item_quantity(self, name, quantity):
        """
        Fungsi : Mengganti jumlah item pada list belanja.

        Parameter:
        name (string): Nama item yang ingin diubah jumlahnya.
        new_quantity (int): Jumlah baru dari item yang ingin diubah.

        Output:
        Pesan yang memberitahu bahwa jumlah item sudah berhasil diubah.
        """
        for item in self.items:
            if item[0] == name:
                item[1] = quantity

        print(f"Jumlah {name} telah diubah menjadi {quantity}")
        self.show_item()

    # Menambahkan method yang berfungsi mengganti harga item ke dalam list belanja
    def update_item_price(self, name, price):
        """
        Fungsi : Mengganti harga item pada list belanja.

        Parameter:
        name (string): Nama item yang ingin diubah harganya.
        new_price (int): Harga item baru dari item yang ingin diubah.

        Output:
        Pesan yang memberitahu bahwa harga per item sudah berhasil diubah.
        """
        for item in self.items:
            if item[0] == name:
                item[2] = price

        print(f"Harga {name} telah diubah menjadi {price}")
        self.show_item()

    # Menambahkan method yang berfungsi menghapus item ke dalam list belanja
    def delete_item(self, name):
        """
        Fungsi : Menghapus item di dalam list belanja.

        Parameter:
        name (string): Nama item yang ingin dihapus dari list items.

        Output:
        Pesan yang memberitahu bahwa item sudah berhasil dihapus dari list items.
        """
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)

        print(f"Anda telah menghapus : {name} ")
        self.show_item()

    # Menambahkan method yang berfungsi menghapus semua item dalam list belanja
    def reset_item(self):
        """
        Fungsi : Menghapus semua item di dalam list belanja.

        Output:
        Pesan yang memberitahu bahwa semua item sudah berhasil dihapus dari list items.
        """
        self.items = []

        print(f"Anda telah mereset transaksi ini. Semua item telah dihapus.")

    # Menambahkan method yang berfungsi mengecek kebenaran data list belanja
    def check_order(self):
        """
        Fungsi : Mengecek kebenaran input data dalam list belanja.

        Output:
        Jika semua input data sudah benar, fungsi akan mengeluarkan pesan "Pemesanan sudah sesuai".
        Jika terdapat kesalahan pada input data, fungsi akan mengeluarkan pesan "Terdapat kesalahan input data".
        Jika input data sudah benar, fungsi akan mengeluarkan output berupa tabel berisi item, jumlah item,
        harga satuan, dan total harga.
        """
        error = False
        for item in self.items:
            if (None, "", 0) in item or not all(item):
                error = True
        if error:
            print("Terdapat kesalahan input data")
        else:
            print("Pesanan sudah sesuai")
            self.show_item()

    # Menambahkan method yang menampilkan daftar belanja dan total harga
    def show_item(self):
        """
        Fungsi : Menampilkan nama item, jumlah item, harga satuan dan total harga

        Output:
        Tabel nama item, jumlah item, harga satuan dan total harga
        """
        print("=" * 60)
        print("Item\t\tJumlah\tHarga Satuan\tTotal Harga")
        print("-" * 60)
        for item in self.items:
            total_price = item[1] * item[2]
            print("{}\t\t{}\t\t{}\t\t\t{}".format(item[0], item[1], item[2], total_price))
        print("-" * 60)

    # Menambahkan method yang menampilkan total harga dan diskon yang diberikan
    def total_price(self):
        """
        Fungsi untuk menghitung total harga dari seluruh item pada list items.
        Menghitung diskon dengan ketentuan yang telah ditetapkan sebelumnya.

        Output:
        Total harga dari seluruh item pada list items.
        """
        total = 0
        for item in self.items:
            total += item[1] * item[2]
        if total > 500000:
            discount = total * 0.1
        elif total > 300000:
            discount = total * 0.08
        elif total > 200000:
            discount = total * 0.05
        else:
            discount = 0
        total -= discount
        print("Total Harga: {}\nDiskon: {}\nTotal yang harus dibayar: {}".format(total + discount, discount, total))
