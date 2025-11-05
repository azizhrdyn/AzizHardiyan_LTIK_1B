def intro():
    print("=== APLIKASI ADMINISTRASI SEKOLAH ===")
    print("Username: SMAN 1 Karawang")
    print()

def login(pwsistem):
    uinput = 2 

    while uinput >= 0:
        
        if uinput == 2:
            pw = input("Password (3 kali kesempatan): ")
        else:
            pw = input("Password: ")

        if uinput == 0:
            print("Akses ditolak, anda telah gagal mencoba sebanyak 3 kali.")
            return False  
        
        elif pw == pwsistem:
            print("Akses diterima. Selamat datang di aplikasi.")
            return True  
        
        else:
            print(f"Password salah. Sisa kesempatan: {uinput}")
            uinput -= 1

def main():
    pwsistem = "Latihan"
    intro()
    login(pwsistem)

main()