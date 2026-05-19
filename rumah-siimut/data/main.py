from aktivitas import Kebersihan

nama = input("Masukkan nama rumah : ")
kebersihan = int(input("Masukkan kebersihan awal : "))
password = input("Masukkan password : ")

rumah = Kebersihan(nama, kebersihan, password)

while True:

    rumah.status()

    print("\nMENU")
    print("1. Menyapu")
    print("2. Mengepel")
    print("3. Merapikan")
    print("4. Lihat Password")
    print("5. Keluar")

    pilih = input("Pilih menu : ")

    if pilih == "1":
        rumah.sapu()

    elif pilih == "2":
        rumah.pel()

    elif pilih == "3":
        rumah.rapikan()

    elif pilih == "4":
        rumah.tampil_password()

    elif pilih == "5":
        print("Program selesai")
        break

    else:
        print("Menu tidak tersedia")