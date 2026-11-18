# PROGRAM KASIR KANTIN KAMPUS

jumlah_transaksi = int(input("Masukkan jumlah transaksi: "))

total_belanja = 0

for i in range(jumlah_transaksi):

    print("===== Transaksi ke-", i + 1,"=====")

    nama_makanan = input("Masukkan nama makanan: ")
    harga = int(input("Masukkan harga makanan: "))
    jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))

    total_harga = harga * jumlah_pembelian

    print("Nama makanan:", nama_makanan)
    print("Total harga:", total_harga)

    total_belanja = total_belanja + total_harga

if total_belanja > 100000:
    diskon = int(10 / 100 * total_belanja)
    total_pembayaran = int(total_belanja - diskon)

else:
    diskon = 0
    total_pembayaran = total_belanja

print("======= HASIL PEMBAYARAN =======")
print("Total belanja:", total_belanja)
print("Diskon:", diskon)
print("Total pembayaran:", total_pembayaran)