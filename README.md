# Super Cashier Project - Pacmann
#### Python Final Project by Gupita Rahajeng Kusumaningtyas


### Latar Belakang
---------------
Super cashier adalah sebuah sistem kasir self-service yang akan digunakan di salah satu supermarket besar di Indonesia. Super cashier dibuat dengan tujuan untuk meningkatkan efisiensi dan produktivitas dari supermarket itu sendiri. Cara kerja dari sistem super cashier adalah customer bisa memasukkan sendiri item, jumlah item, dan harga item yang dibeli di supermarket, hingga total belanja yang harus dibayarkan. Hal ini diikuti juga dengan fitur-fitur yang dapat mempermudah penggunaan sistem tersebut sehingga mempermudah customer untuk menyelesaikan pembayaran dengan lebih cepat.

### Objektif
---------------
Hal-hal yang dapat dilakukan dengan sistem super cashier:
1.	Membuat ID transaksi customer
2. 	Memasukkan nama, jumlah, dan harga item yang dibeli
3.	Mengubah nama, jumlah, dan harga item yang dibeli
4.	Menghapus salah satu nama item yang dibeli
5.	Menghapus semua transaksi yang telah diinput
6.	Mengecek keseluruhan pesanan sebelum menghitung total belanjaan
7.	Menghitung total belanja, dengan ketentuan diskon sebagai berikut:
    - Jika total belanja diatas 200.000 akan mendapat diskon 5%
    - Jika total belanja diatas 300.000 akan mendapat diskon 8%
    - Jika total belanja diatas 500.000 akan mendapat diskon 10%

### Program Flow Chart
---------------
![flowchart](https://github.com/gupitarahajeng/Pacmann/assets/138182400/2c74a5c1-e9c3-4b6d-954a-ba581e9b77cc)

### Method Flowchart
---------------
#### Add Item
![add item](https://github.com/gupitarahajeng/Pacmann/assets/138182400/99421598-7b59-4c42-921d-354c867831fd)

#### Update Item Name
![update item name](https://github.com/gupitarahajeng/Pacmann/assets/138182400/e51879f6-a717-4861-83c5-f3f0d68f86ae)

#### Update Item Quantity
![update item qty](https://github.com/gupitarahajeng/Pacmann/assets/138182400/b2e764a2-3e90-4b23-a485-c8a90e4318ea)

#### Update Item Price
![update item price](https://github.com/gupitarahajeng/Pacmann/assets/138182400/7d0b6cba-9c83-48b6-8c0c-b99cfa295021)

#### Delete Item
![delete item](https://github.com/gupitarahajeng/Pacmann/assets/138182400/d8d4ca29-3069-43e4-bdd1-5d1b03b41925)

#### Reset Item
![reset item](https://github.com/gupitarahajeng/Pacmann/assets/138182400/711419ec-51a1-42eb-ab69-7a5d895c183b)

#### Check Order
![check order](https://github.com/gupitarahajeng/Pacmann/assets/138182400/dd1da04b-a236-42c2-b2eb-50edb851f2f1)

#### Show Item
![show item](https://github.com/gupitarahajeng/Pacmann/assets/138182400/1f7b4ce1-197b-4960-a285-68f90653d11e)

#### Total Price
![total price](https://github.com/gupitarahajeng/Pacmann/assets/138182400/b23eb0b5-c582-4a60-8010-1238ea5b4b91)

### Deskripsi Program
---------------
Project ini menggunakan dua file, yaitu main.py sebagai file utama yang akan dieksekusi, serta modul transaction.py yang berisi fungsi-fungsi untuk menjalankan program. Berikut fungsi-fungsi yang ada di dalam sistem Super Cashier:
-	add_item : menambahkan item pada list belanja
-	update_item_name : mengganti nama item pada list belanja
-	update_item_quantity : mengganti jumlah item pada list belanja
-	update_item_price : mengganti harga item pada list belanja
-	delete_item : menghapus item pada list belanja
-	reset_item : menghapus semua item pada list belanja
-	check_order : mengecek kebenaran input data list belanja
-	show_item : menampilkan nama item, jumlah item, harga satuan dan total harga
-	total_price : menampilkan total harga dan diskon yang diberikan

### Cara Menggunakan Program & Tes Case
---------------
##### Main Menu
![image](https://github.com/gupitarahajeng/Pacmann/assets/138182400/c28a9eaa-37a0-4cbb-9bf1-32025287b15e)

##### Test Case 1
Menambahkan dua item baru dengan method add_item(). Item yang ditambahkan adalah sebagai berikut:
-	Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
-	Nama Item: Pasta Gigi, Qty: 3, Harga: 15000
  
Output:

![image](https://github.com/gupitarahajeng/Pacmann/assets/138182400/a30bec71-c6af-436f-baa9-56a922b11ac5)

##### Test Case 2
Menghapus item dari list belanja dengan menggunakan method delete_item(). Item yang ingin dihapus adalah item Pasta Gigi.

Output:

![image](https://github.com/gupitarahajeng/Pacmann/assets/138182400/f04b284f-a49c-4121-8382-f5b09808a1d2)

##### Test Case 3
Menghapus seluruh item dari list belanja dengan menggunakan method reset_transaction().

Output:

![image](https://github.com/gupitarahajeng/Pacmann/assets/138182400/681b4a69-6854-4674-9820-6f8094b14957)

##### Test Case 4
Menghitung total belanja yang harus dibayarkan dengan method total_price(). Item yang akan diproses lebih lanjut untuk pembayaran adalah sebagai berikut:
-	Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
-	Nama Item: Pasta Gigi, Qty: 3, Harga: 15000
-	Nama Item: Mainan Mobil, Qty: 1, Harga: 200000
-	Nama Item: Mi Instan, Qty: 5, Harga: 3000
  
Output:

![image](https://github.com/gupitarahajeng/Pacmann/assets/138182400/fcd18edf-635f-4720-aaa4-1a08d2baf076)

### Kesimpulan 
---------------
Program Super Cashier memungkinkan pengguna untuk menambah, mengupdate, menghapus, dan memeriksa item dalam transaksi, dan menghitung total harga belanja dengan diskon secara otomatis.
