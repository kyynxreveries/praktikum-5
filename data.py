data_nilai = []

def lihat_data():
    if len(data_nilai) == 0:
        print("Tidak Ada Data")
    else:
        print("Daftar Nilai")
        print("=" * 60)
        print("| NO |   NIM   |   NAMA   | TUGAS | UTS | UAS | AKHIR |")
        print("=" * 60)
        for i, data in enumerate(data_nilai, start=1):
            print(f"| {i:2} | {data['NIM']:7} | {data['Nama']:8} | {data['Tugas']:5} | "
                  f"{data['UTS']:3} | {data['UAS']:3} | {data['Akhir']:5.2f} |")
        print("=" * 60)

def tambah_data():
    NIM = input("NIM: ")
    Nama = input("Nama: ")
    Tugas = int(input("Nilai Tugas: "))
    UTS = int(input("Nilai UTS: "))
    UAS = int(input("Nilai UAS: "))
    Akhir = (Tugas * 0.3) + (UTS * 0.35) + (UAS * 0.35)
    data_nilai.append({"NIM": NIM, "Nama": Nama, "Tugas": Tugas, "UTS": UTS, "UAS": UAS, "Akhir": Akhir})
    print("Data berhasil ditambahkan!")

def ubah_data():
    lihat_data()
    index = int(input("Masukkan nomor data yang akan diubah: ")) - 1
    if index < 0 or index >= len(data_nilai):
        print("Data tidak ditemukan.")
    else:
        print("Ubah Data")
        data_nilai[index]['NIM'] = input("NIM: ")
        data_nilai[index]['Nama'] = input("Nama: ")
        data_nilai[index]['Tugas'] = int(input("Nilai Tugas: "))
        data_nilai[index]['UTS'] = int(input("Nilai UTS: "))
        data_nilai[index]['UAS'] = int(input("Nilai UAS: "))
        data_nilai[index]['Akhir'] = (data_nilai[index]['Tugas'] * 0.3 +
                                       data_nilai[index]['UTS'] * 0.35 +
                                       data_nilai[index]['UAS'] * 0.35)
        print("Data berhasil diubah!")

def hapus_data():
    lihat_data()
    index = int(input("Masukkan nomor data yang akan dihapus: ")) - 1
    if index < 0 or index >= len(data_nilai):
        print("Data tidak ditemukan.")
    else:
        del data_nilai[index]
        print("Data berhasil dihapus!")

def cari_data():
    keyword = input("Masukkan nama yang dicari: ").lower()
    hasil_cari = [data for data in data_nilai if keyword in data['Nama'].lower()]
    if len(hasil_cari) == 0:
        print("Data tidak ditemukan.")
    else:
        print("Hasil Pencarian")
        print("=" * 60)
        print("| NO |   NIM   |   NAMA   | TUGAS | UTS | UAS | AKHIR |")
        print("=" * 60)
        for i, data in enumerate(hasil_cari, start=1):
            print(f"| {i:2} | {data['NIM']:7} | {data['Nama']:8} | {data['Tugas']:5} | "
                  f"{data['UTS']:3} | {data['UAS']:3} | {data['Akhir']:5.2f} |")
        print("=" * 60)

while True:
    print("\nProgram Input Nilai")
    print("===================")
    print("[L]ihat, [T]ambah, [U]bah, [H]apus, [C]ari, [K]eluar")
    menu = input("Pilih menu: ").lower()

    if menu == 'l':
        lihat_data()
    elif menu == 't':
        tambah_data()
    elif menu == 'u':
        ubah_data()
    elif menu == 'h':
        hapus_data()
    elif menu == 'c':
        cari_data()
    elif menu == 'k':
        print("Keluar dari program.")
        break
    else:
        print("Menu tidak valid.")