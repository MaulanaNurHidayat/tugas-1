# 1.Buat program yang terus meminta pengguna memasukkan angka dan menghitung berapa jumlah angka genap yang telah dimasukkan.
# 2.Buat program yang meminta pengguna memasukkan kata atau kalimat, dan menampilkan jumlah karakter yang dimasukkan. Program akan terus berjalan sampai pengguna mengetik "keluar".
# 3.Buatlah fungsi prima(n) yang mengecek apakah sebuah bilangan n adalah bilangan prima (bilangan yang hanya memiliki dua faktor: 1 dan dirinya sendiri). Fungsi harus mengembalikan True jika n adalah bilangan prima, dan False jika tidak.

while True :
    print ("""
---> SELAMAT DATANG DI PROGRAM UNIVERSAL <---
\n PROGRAM YANG INGIN DI JALANKAN :
   A. Menghitung Jumlah Angka Genap         
   B. Menghitung Jumlah Karakter Huruf
   C. Mengecek Bilangan Prima""")
    list_program = input ("Pilih Program (pilih huruf A-C): ")
    if list_program == 'A':
        jumlah_genap = 0
        while True :
            try:
                angka = int (input("\nMasukkan angka / ketik 'exit' untuk keluar program : "))
                if angka % 2 == 0:
                    jumlah_genap += 1
            except ValueError:
                print(f"jumlah angka genap yg dimasukkan adalah : {jumlah_genap}")
                print("Program Berhenti.")
                break
        
    elif list_program == 'B':
        while True:
            kata=input ("\nMasukkan kata atau kalimat (ketik 'exit' untuk keluar) : ")
            if kata.lower() == "exit":
                print("Program berhenti.")
                break
            else:
                print(f"Jumlah karakter yang dimasukkan adalah : {len(kata)}")
            
    elif list_program == 'C':
        n = int(input("\nMasukkan bilangan yang akan di cek : "))
        prima = True
        if n <=1:
            prima = False
        else:
            for i in range(2, int(n**0.5) + 1) :
                if n % i == 0:
                    prima = False
                    break
        if prima:
            print(f"{n} aladah bilanagan prima.")
        else:
            print(f"{n} bukan bilangan prima.")
        
    else :
        print("Data tidak valid")
            
    list_program = input("pilih program kembali (y/n) : ")
    if list_program.lower()=='n':
        print ("Program berhenti.")
        break