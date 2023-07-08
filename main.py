# Import transaction
from transaction import Transaction

# Membuat object transaction
transct_123 = Transaction()

# Menu utama yang akan dijalankan pertama kali
while True:
    print("*" * 60)
    print("Andi Supermarket. \n"
          "Pilih 1 menu:")
    print("1. Tambah item pada list belanja")
    print("2. Ganti nama item pada list belanja")
    print("3. Ganti jumlah item pada list belanja")
    print("4. Ganti harga item pada list belanja")
    print("5. Hapus item pada list belanja")
    print("6. Reset semua transaksi belanja")
    print("7. Cek keseluruhan list belanja")
    print("8. Selesaikan belanja")
    menu_choice = input("Pilih menu: ")

    if menu_choice == '1':
        add = True
        while add:
            try:
                nama_item = input("Masukkan nama item: ")
                jumlah_item = int(input("Masukkan jumlah item: "))
                harga_item = int(input("Masukkan harga per item: "))
            
            except ValueError:
                print("Jumlah item dan harga item harus diisi dengan data integer")
                nama_item = input("Masukkan nama item: ")
                jumlah_item = int(input("Masukkan jumlah item: "))
                harga_item = int(input("Masukkan harga per item: "))

            # Tambahkan item ke transaksi
            transct_123.add_item([nama_item, jumlah_item, harga_item])

            # Tanya user untuk menambahkan item
            add_more = input("Tambah item? (y/n): ")
            if add_more.lower() == 'y':
                pass
            elif add_more.lower() == 'n':
                print("Anda akan kembali ke menu utama")
                break
            else:
                print("Input Anda salah. \nMasukkan nilai 'y' atau 'n'")
                print("Anda akan kembali ke menu utama")
                break

    elif menu_choice == '2':
        nama_item_lama = input("Masukkan nama item yang ingin diganti: ")
        nama_item_baru = input("Masukkan nama item baru: ")
        transct_123.update_item_name(nama_item_lama, nama_item_baru)
    elif menu_choice == '3':
        try:
            nama_item = input("Masukkan nama item: ")
            jumlah_item_baru = int(input("Masukkan jumlah item baru: "))
        except ValueError:
            print("Jumlah item baru harus diisi dengan data integer")
            nama_item = input("Masukkan nama item: ")
            jumlah_item_baru = int(input("Masukkan jumlah item baru: "))

        transct_123.update_item_quantity(nama_item, jumlah_item_baru)
    elif menu_choice == '4':
        try:
            nama_item = input("Masukkan nama item: ")
            harga_item_baru = int(input("Masukkan harga item baru: "))
        except ValueError:
            print("Harga item baru harus diisi dengan data integer")
            nama_item = input("Masukkan nama item: ")
            harga_item_baru = int(input("Masukkan harga item baru: "))

        transct_123.update_item_price(nama_item, harga_item_baru)
    elif menu_choice == '5':
        nama_item = input("Masukkan nama item: ")
        transct_123.delete_item(nama_item)
    elif menu_choice == '6':
        transct_123.reset_item()
    elif menu_choice == '7':
        transct_123.check_order()
    elif menu_choice == '8':
        break

# Cetak order detail
transct_123.check_order()

# Cetak harga total
total = transct_123.total_price()
