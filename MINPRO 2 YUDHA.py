# ===========================================
# Nama   : Muhammad Aqia Yudha Yulian Putra
# NIM    : 2509116105
# Kelas  : C 2025
# Tugas  : Mini Project 2 
# ===========================================

# Data user login
users = {
    "manager": {"password": "tenggarong123", "role": "Manager"},
    "yudha": {"password": "tenggarongabc", "role": "penghuni"}
}

# Data kos
penghuni = {}
kamar = {}

# CRUD Penghuni
def tambah_penghuni():
    nama = input("Nama penghuni: ")
    if nama in penghuni:
        print("Nama sudah ada bos.")
        return
    kontak = input("Nomor HP: ")
    kamar_no = input("Nomor kamar: ")
    penghuni[nama] = {"kontak": kontak, "kamar": kamar_no}
    print("Penghuni berhasil ditambahkan.")

def lihat_penghuni():
    if not penghuni:
        print("Belum ada data penghuni.")
    else:
        print("\n--- Data Penghuni ---")
        for n, d in penghuni.items():
            print(f"Nama: {n}, Kontak: {d['kontak']}, Kamar: {d['kamar']}")

def ubah_penghuni():
    lihat_penghuni()
    nama = input("Nama penghuni yg mau diubah: ")
    if nama not in penghuni:
        print("Tidak ada.")
        return
    kontak = input(f"Kontak baru ({penghuni[nama]['kontak']}): ") or penghuni[nama]['kontak']
    kamar_no = input(f"Kamar baru ({penghuni[nama]['kamar']}): ") or penghuni[nama]['kamar']
    penghuni[nama] = {"kontak": kontak, "kamar": kamar_no}
    print("Data berhasil diubah.")

def hapus_penghuni():
    lihat_penghuni()
    nama = input("Nama penghuni yg mau dihapus: ")
    if nama not in penghuni:
        print("Tidak ada.")
        return
    del penghuni[nama]
    print("Data berhasil dihapus.")

# CRUD Kamar
def tambah_kamar():
    nomor = input("Nomor kamar: ")
    if nomor in kamar:
        print("Sudah ada.")
        return
    status = input("Status (kosong/terisi): ")
    kamar[nomor] = {"status": status}
    print("Kamar berhasil ditambahkan.")

def lihat_kamar():
    if not kamar:
        print("Belum ada data kamar.")
    else:
        print("\n--- Data Kamar ---")
        for n, d in kamar.items():
            print(f"Kamar {n}, Status: {d['status']}")

def ubah_kamar():
    lihat_kamar()
    nomor = input("Nomor kamar yg mau awk ubah: ")
    if nomor not in kamar:
        print("Tidak ada.")
        return
    status = input(f"Status baru ({kamar[nomor]['status']}): ") or kamar[nomor]['status']
    kamar[nomor]["status"] = status
    print("Data berhasil diupdate.")

def hapus_kamar():
    lihat_kamar()
    nomor = input("Nomor kamar yg mau awk hapus: ")
    if nomor not in kamar:
        print("Tidak ada.")
        return
    del kamar[nomor]
    print("Data berhasil dihapus.")

# Menu Manager
def menu_manager():
    while True:
        print("\n=== MENU MANAGER ===")
        print("1. Tambah Penghuni")
        print("2. Lihat Penghuni")
        print("3. Ubah Penghuni")
        print("4. Hapus Penghuni")
        print("5. Tambah Kamar")
        print("6. Lihat Kamar")
        print("7. Ubah Kamar")
        print("8. Hapus Kamar")
        print("9. Keluar")
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka.")
            continue

        if pilih == 1: tambah_penghuni()
        elif pilih == 2: lihat_penghuni()
        elif pilih == 3: ubah_penghuni()
        elif pilih == 4: hapus_penghuni()
        elif pilih == 5: tambah_kamar()
        elif pilih == 6: lihat_kamar()
        elif pilih == 7: ubah_kamar()
        elif pilih == 8: hapus_kamar()
        elif pilih == 9: break
        else: print("Pilihan tidak ada.")

# Menu Penghuni
def menu_penghuni():
    while True:
        print("\n=== MENU PENGHUNI ===")
        print("1. Lihat Data Penghuni")
        print("2. Lihat Data Kamar")
        print("3. Logout")
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka.")
            continue

        if pilih == 1: lihat_penghuni()
        elif pilih == 2: lihat_kamar()
        elif pilih == 3: break
        else: print("Pilihan tidak ada.")

# Login
def login():
    print("="*35)
    print("   SISTEM MANAJEMEN KOS")
    print("="*35)
    while True:
        try:
            username = input("Username: ")
            password = input("Password: ")
        except Exception as e:
            print("Error:", e)
            continue

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login berhasil sebagai {role}")
            if role == "Manager":
                menu_manager()
            else:
                menu_penghuni()
            break
        else:
            print("Username / Password awk salah.")

# Main
if __name__ == "__main__":
    login()
