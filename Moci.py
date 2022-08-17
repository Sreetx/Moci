import os, sys, requests, webbrowser, time

"""Software yang kami buat bersifat OPEN SOURCE"""

os.system(' ')

print('\n [</>] Memulai program....\n')
time.sleep(3)
print (" [..............................] 0%")
time.sleep(2)
print (" [>>>>>>>>>>>>>>>>>>............] 60%")
time.sleep(2)
print (" [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>] 100%\n")
time.sleep (3)
print (" [</>] Membuka Program....\n")
time.sleep(3)

banner ="""
  
<=|=>-----------------------------| Moci |-------------------------------<=|=>
  |                       ________________________                         |
  |                      |All In One This Software|                        |
  |                       ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                         |
 <|------------------------------------------------------------------------|>
  | Author:                    RX77E, Security Syber Team Indonesian       |
  | Spesial Thank's:           RX77E                                       |
  | Github:                    https://github.com/Sreetx                   |
  | Instagram:                 https://www.instagram.com/memelucubikin     |
 <|------------------------------------------------------------------------|>
  |       Kami tidak bertanggung jawab atas apapun yang kalian lakukan     |
<=|=>--------------------------------------------------------------------<=|=>
  """
print(banner)
enter = input("\n [*] Tekan enter untuk melanjutkan....\n")
while True:
    try:
    
        print("\n [#] Pilih opsi")
        print("  {1} Alone                            [#] Konten Kami")
        print("  {2} DDOS Attack                       {Y} YouTube")
        print("  {3} DDOS Attack Lite                  {I} Instagram")
        print("  {4} Defacer                           {G} Github")
        print("  {5} Funnycat                          {W} Website")
        print("  {6} Israel SQL Injection Dork")
        print("  {7} Server Info                       [#] Konten luar")
        print("  {8} Readme/Tentang                     {S} Sqlmap")
        print('  {9} Keluar                             {M} Metasploit(Khusus Linux)')
        pilih = input("\n   [?] Pilih opsi: ")

    # Tool's kami
        if pilih.strip() == '1':
            print("\n [*] Deskripsi:")
            print("  Alone adalah sebuah script pembuat script deface web. kalian bisa dengan mudah membuat script deface tanpa harus coding.")
            tanya = input("\n [?] Pasang script? [Y/n]: ")
            if tanya.lower() == 'y':
                print ("\n[*] Mengunduh script....")
                r = requests.get('https://github.com/Sreetx/alone/archive/refs/heads/main.zip')
                nf = r.split('/')[-1]
                with open(nf, 'wb') as code:
                  code.write(r.content)
                print(' [*] Selesai')
                print(" [*] File disimpan dengan nama '"+nf+"'\n")
        elif pilih.strip() == '2':
            print('\n [*] Deskripsi:')
            print('  DDOS Attack adalah script yang dapat melakukan serangan ddos dengan mengirimkan lonjakan internet dengan sangat besar ditambah dengan booster')
            tanya6 = input('\n [?] Pasang script? [Y/n]: ')
            if tanya6.lower() == 'y':
                print('\n [*] Mengunduh script....')
                da = requests.get('https://github.com/Sreetx/DDOS-Attack/archive/refs/heads/main.zip')
                nf2 = da.split('/')[-1]
                with open(nf2, 'wb') as code2:
                  code2.write(da.content)
                print(' [*] Selesai')
                print(" [*] File disimpan dengan nama '"+nf2+"'\n")
        elif pilih.strip() == '3':
            print('\n [*] Deskripsi:')
            print('  DDOS Attack Lite adalah script yang sama seperti script biasanya, yaitu DDOS Attack. Hanya saja DDOS Attack Lite tidak memiliki booster untuk penyerangan.')
            tanya7 = input('\n [?] Pasang script? [Y/n]: ')
            if tanya7.lower() == 'y':
                print('\n Mengunduh script....')
                dal = requests.get('https://github.com/Sreetx/dalite/archive/refs/heads/main.zip')
                nf3 = dal.split('/')[-1]
                with open(nf3, 'wb') as code3:
                  code3.write(dal.content)
                print(' [*] Selesai')
                print(" [*] File disimpan dengan nama '"+nf3+"'\n")
        elif pilih.strip() == '4':
            print('\n [*] Deskripsi:')
            print("  Defacer adalah sebuah tool's yang digunakan untuk mendeface sebuah website, cara kerjanyapun cukup mudah. Tapi kami tidak bertangung jawab atas apa yang kalian lakukan pada web orang lain")
            tanya13 = input('\n [?] Pasang script? [Y/n]: ')
            if tanya13.lower() == 'y':
                print('\n [*] Mengunduh script....')
                df = requests.get('https://github.com/Sreetx/deweb/archive/reft/heads/main.zip')
                nf4 = df.split('/')[-1]
                with open(nf4, 'wb') as code9:
                  code9.write(df.content)
                print(' [*] Selesai')
                print(" [*] File disimpan dengan nama '"+nf4+"'\n")
        elif pilih.strip() == '5':
            print('\n [*] Deskripsi')
            print('  Funnycat adalah script pengunduh video dari situs Facebook dan Instagram saja.')
            tanya8 = input('\n [?] Pasang script? [Y/n] : ')
            if tanya8.lower() == 'y':
                print('\n [*] Mengunduh script....')
                fun = requests.get('https://github.com/Sreetx/funnycat/archive/refs/heads/main.zip')
                nf5 = fun.split('/')[-1]
                with open(nf5, 'wb') as code4:
                  code4.write(fun.content)
                print(' [*] Selesai')
                print(" [*] File disimpan dengan nama '"+nf5+"'\n")
        elif pilih.strip() == '6':
            print('\n [*] Deskripsi:')
            print('  Israel SQL Injection Dork adalah daftar dork yang sengaja kami buat untuk menyerang website Israel menggunakan SQLmap. Jadi ayo kita sama sama menyerang website Israel. Dengan menyerang lewat virtual, kita juga sudah ikut berperang bersama negara lain yang membela Palestina.')
            tanya10 = input('\n [*] Unduh Dork? [Y/n]: ')
            if tanya10.lower() == 'y':
                print('\n [*] Mengunduh dork....')
                drk = requests.get('https://github.com/Sreetx/Israel_SQL_Injection_Dork/archive/refs/heads/main.zip')
                nf7 = drk.split('/')[-1]
                with open(nf7, 'wb') as code6:
                  code6.write(drk.content)
                print(' [*] Selesai')
                print(" [*] File disimpan dengan nama '"+nf7+"'\n")
        elif pilih.strip() == '7':
            print('\n [*] Deskripsi:')
            print("  Server Info adalah sebuah tool's yang dapat menampilkan info sebuah web dengan detail, mulai dari alamat IP, port, layanan penghosting, protokol, dan lain sebagainya.")
            tanya14 = input('\n [?] Unduh script? [Y/n]: ')
            if tanya14.lower() == 'y':
                print('\n [*] Mengunduh script....')
                svi = requests.get('https://github.com/Sreetx/server-info/archive/refs/heads/main.zip', verify = False)
                nf8 = svi.split('/')[-1]
                with open(nf8, 'rb') as code10:
                  code10.write(svi.content)
                print(' [*] Selesai')
                print(" [*] File disimpan dengan nama '"+nf8+"'\n")
        elif pilih.strip() == '8':
            webbrowser.open('https://github.com/Sreetx/Moci')

    # Konten kami
        elif pilih.strip() == 'y':
            tanya2 = input(' [?] Apakah anda ingin membantu motenisasi kami di YouTube? [Y/n]: ')
            if tanya2.lower() == 'y':
                print('\n [*] Membuka browser....')
                webbrowser.open('https://youtube.com/channel/UCscuxW-ZUViftGyJ9Z1cPbw/')
                print(' [*] Terima kasih telah membantu motenisasi kami\n')
        elif pilih.strip() == 'i':
            tanya3 = input(' [?] Apakah anda ingin membantu motenisasi kami di Instagram? [Y/n]: ')
            if tanya3.lower() == 'y':
                print('\n [*] Membuka browser....')
                webbrowser.open('https://www.instagram.com/memelucubikin/')
                print(' [*] Terima kasih telah membantu motenisasi kami\n')
        elif pilih.strip() == 'g':
            tanya4 = input(' [?] Ingin melihat repostori kami di Github? [Y/n]: ')
            if tanya4.lower() == 'y':
                print('\n [*] Membuka browser....')
                webbrowser.open('https://github.com/Sreetx/')
                print(' [*] Terima kasih telah melihat berbagai repostori kami di Github\n')
        elif pilih.strip() == 'w':
            tanya5 = input('\n [?] Ingin melihat website kami? [Y/n]: ')
            if tanya5.lower() == 'y':
                print(' [*] Membuka browser....')
                webbrowser.open('https://progpem.blogspot.com/2022/04/hom.html/')
                print(' [*] Terima kasih telah me-review website kami')
                
    # Konten luar
        elif pilih.strip() == 's':
            print('\n [*] Deskripsi')
            print("  SQLmap adalah sebuah Tool's yang dapat melakukan injeksi pada suatu bug pada website. Untuk info lebih lanjut silakan masuk ke situs ini 'https://github.com/sqlmapproject/sqlmap'")
            tanya11 = input('\n [*] Pasang script? [Y/n]: ')
            if tanya11.lower() == 'y':
                print("\n [*] Mengunduh Tool's....")
                sql = requests.get('https://github.com/sqlmapproject/sqlmap/archive/refs/heads/master.zip')
                nf9 = sql.split('/')[-1]
                with open(nf9, 'wb') as code7:
                   code7.write(sql.content)
                print(' [*] Selesai')
                print(" [*] File disimpan dengan nama '"+nf9+"'\n")
        elif pilih.strip() == 'm':
            print(" [*] Deskripsi")
            print('   silakan baca deskripsinya di https://github.com/rapid7/metasploit-framework. Untuk mengunduh metasploit harap diperhatikan, metasploit memiliki ukuran 500MB+ dan kalian harus memiliki bahasa program Ruby, C++/Clang dan lainnya.')
            tanya12 = input('\n [*] Pasang Script? [Y/n]: ')
            if tanya12.lower() == 'y':
                print("\n [*] Mengunduh Tool's....")
                print(' [INFO] Karena proses mengunduh lama, sebaiknya anda tinggalkan komputer anda selama proses pengunduhan')
                os.system('apt-get install metasploit')
                print(' [*] Selesai')

    # Menu Keluar
        elif pilih.strip() == '9':
            print('\n [*] Mematikan program....\n')
            print(' [*] Terima kasih karena telah mengunakan script kami\n');sys.exit()
        else:
            print(' [!] Ops, Pilihan yang anda masukan salah')
    except Exception as e: print (" [!] Anda tidak terhubung ke internet")
    except EOFError: print('\n [*] CTRL+C Terdeteksi, keluar dari program');sys.exit()
    except KeyboardInterrupt: print('\n [*] CTRL+C Terdeteksi, keluar dari program');sys.exit()