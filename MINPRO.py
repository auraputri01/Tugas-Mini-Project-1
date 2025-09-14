# Nama : Aura Putri Anandita Syarif
# NIM : 2509116094
# Praktikum MINI PROJECT 1 (Data Produk Online Shop)

data_produk = []

print("Hai! Ini Adalah Program Produk Online Shop Kami")
kategori = input("Masukkan kategori produk (fashion/kecantikan/peralatan: ")

if kategori == "1" :
    jenis = input("Produk fashion untuk pria atau wanita? (pria/wanita): ")
    if jenis == "pria":
        print("/n produk: fashion pria")
        print("produk tersedia: Jaket Pria, Kaos Polos, Kemeja")
        print("harga mulai dari: Rp80.000")
    elif jenis == "wanita":
        print("\n jenis: Fashion Wanita")
        print("produk tersedia: Dress, Hijab, Blouse, Rok")
        print("harga mulai dari: 60.000")
    else:
        print("Input tidak sesuai")

elif kategori == "2":
    fungsi = input("Produk untuk wajah atau tubuh? (wajah/tubuh): ")
    if fungsi == "wajah":
        print("\n produk tersedia: Serum, Toner, moisturizer")
        print("harga mulai dari: Rp50.000")
    elif fungsi == "tubuh":
        print("\n produk tersedia: Body lotion, Scrub, Sabun herbal")
        print("harga mulai dari: Rp30.000")
    else:
        print("Input tidak sesuai")

elif kategori == "3":
    jenis = input("Peralatan dapur atau kantor? (dapur/kantor): ")
    if jenis == "dapur" :
        print("\n produk tersedia: Pisau, Wajan, Blender")
        print("harga mulai dari: Rp25.000")
    elif jenis == "kantor" :
        print("\n produk tersedia: Pulpen, Notebook, Printer")
        print("harga mulai dari: Rp10.000")
    else:
        print("Input tidak sesuai")

else:
    print("Kategori tidak terdaftar")