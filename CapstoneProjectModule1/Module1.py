import os

DATABASE_KARYAWAN = [
    {
        'employee_id': 1001,
        'nama_karyawan': 'Rofi Afiandi',
        'tahun_masuk': 2018,
        'jabatan': 'Team Leader',
        'divisi': 'Quality Control',
        'asal_kota': 'Bogor'
    },
    {   'employee_id': 1002,
        'nama_karyawan': 'Annisa Febrianty',
        'tahun_masuk': 2019,
        'jabatan': 'Team Leader',
        'divisi': 'Customer Support',
        'asal_kota': 'Sukabumi'
    },
    {
        'employee_id': 1003,
        'nama_karyawan': 'Elizabeth Hestia',
        'tahun_masuk': 2016,
        'jabatan': 'Manager',
        'divisi': 'Operational Services',
        'asal_kota': 'Jakarta'  
    },
    {
        'employee_id': 1004,
        'nama_karyawan': 'Mutia Rahmawati',
        'tahun_masuk': 2018,
        'jabatan': 'Team Leader',
        'divisi': 'Business Development',
        'asal_kota': 'Solo'
    },
    {
        'employee_id': 1005,
        'nama_karyawan': 'Felix Nugroho',
        'tahun_masuk': 2017,
        'jabatan': 'Manager',
        'divisi': 'Sales and Marketing',
        'asal_kota': 'Jakarta'
    }
]

# untuk menampilkan sebagian karyawan
def read_half_karyawan(emp_id:int):
    for karyawan in DATABASE_KARYAWAN:
        if karyawan ['employee_id'] == emp_id:
            return karyawan
          
    return None

def edit_karyawan(
    update_employee_id: int,
    new_nama_karyawan:str,
    new_tahun_masuk: int,
    new_jabatan: str,
    new_divisi: str,
    new_asal_kota:str
):
      # update karyawan
    index = -1
    main_index=0
    for karyawan in DATABASE_KARYAWAN: 
        if karyawan['employee_id'] == update_employee_id:
            index = main_index
            break

        main_index += 1
    
    # update karyawan, dgn cek parameter
    default_nama_karyawan = DATABASE_KARYAWAN[index]['nama_karyawan']
    default_tahun_masuk = DATABASE_KARYAWAN[index]['tahun_masuk']
    default_jabatan = DATABASE_KARYAWAN[index]['jabatan']
    default_divisi = DATABASE_KARYAWAN[index]['divisi']
    default_asal_kota = DATABASE_KARYAWAN[index]['asal_kota']

    if new_nama_karyawan != ['nama_karyawan']:
        default_nama_karyawan = new_nama_karyawan
    if new_tahun_masuk != ['tahun_masuk']:
        default_tahun_masuk = new_tahun_masuk
    if new_jabatan != ['jabatan']:
        default_jabatan = new_jabatan
    if new_divisi != ['divisi']:
        default_divisi = new_divisi
    if new_asal_kota != ['asal_kota']:
        default_asal_kota = new_asal_kota

    # new values
    DATABASE_KARYAWAN[index]['nama_karyawan'] = default_nama_karyawan 
    DATABASE_KARYAWAN[index]['tahun_masuk'] = default_tahun_masuk
    DATABASE_KARYAWAN[index]['jabatan'] = default_jabatan
    DATABASE_KARYAWAN[index]['divisi'] = default_divisi
    DATABASE_KARYAWAN[index]['asal_kota'] = default_asal_kota
    
def read_all_karyawan ():
    print('|=|=|=|=|= List Karyawan |=|=|=|=|=')
    for karyawan in DATABASE_KARYAWAN:
        print("|=| Employee ID            :", karyawan['employee_id'])
        print("|=| Nama Karyawan          :", karyawan['nama_karyawan'])
        print("|=| Tahun Masuk            :", karyawan['tahun_masuk'])
        print("|=| Jabatan                :", karyawan['jabatan'])
        print("|=| Divisi                 :", karyawan['divisi'])
        print("|=| Asal Kota              :", karyawan['asal_kota'])        
        print("|=|=|")
        continue
    
    print("--Semua data sudah ditampilkan")
    input('Tekan enter untuk melanjutkan')

def menu_read_karyawan(): 
    while True:
        print('|=|=|=|=|= Menu Read Data Karyawan Perusahaan |=|=|=|=|=')
        print('1. List Seluruh Karyawan')
        print('2. List Sebagian Karyawan')
        print('3. Kembali ke Menu Utama')
        pilihan1 = input('Silahkan pilih menu 1-3: ')
        if pilihan1 == '1':
            read_all_karyawan()
        elif pilihan1 == '2':
            emp_id = int(input('Masukkan Employee ID yang ingin ditampilkan: '))
            bacakaryawan = read_half_karyawan(emp_id)

            if bacakaryawan == None:
                print ('Data Tidak Ada.')

            else:
                print("|=| Employee ID            :", bacakaryawan['employee_id'])
                print("|=| Nama Karyawan          :", bacakaryawan['nama_karyawan'])
                print("|=| Tahun Masuk            :", bacakaryawan['tahun_masuk'])
                print("|=| Jabatan                :", bacakaryawan['jabatan'])
                print("|=| Divisi                 :", bacakaryawan['divisi'])
                print("|=| Asal Kota              :", bacakaryawan['asal_kota'])        
                print("|=|=|")
                print('Data berhasil ditampilkan, silahkan melanjutkan pilihan menu')
                print()

        elif pilihan1 == '3':
            return main_menu()

def create_new_data_karyawan():
    while True:
 
        karyawanbaru = int(input('Masukkan Employee ID baru untuk pengecekkan data: '))

        if karyawanbaru in [data['employee_id'] for data in DATABASE_KARYAWAN]:
            print('Data sudah ada, masukkan kembali Employee ID yang berbeda.')

            # emp_exist = True

        elif karyawanbaru != ['employee_id']:
            nama_karyawan = (input("Masukkan Nama Karyawan: ")).title()  
            tahun_masuk = int(input('Masukkan Tahun Masuk Karyawan:'))
            jabatan = (input('Masukkan Jabatan Karyawan: ')).title()
            divisi = (input('Masukkan Divisi Karyawan: ')).title()       
            asal_kota = (input('Masukkan Asal Kota Karyawan: ')).title()
            DATABASE_KARYAWAN.append({
                'employee_id' : karyawanbaru,
                'nama_karyawan' : nama_karyawan,
                'tahun_masuk' : tahun_masuk,
                'jabatan' : jabatan,
                'divisi' : divisi,
                'asal_kota' : asal_kota
            })
            print('Data berhasil tersimpan!')
            read_all_karyawan()
            break

def update_karyawan():
    #codingan belum pasti
    print('|=|=|=|=|= Menu Data Karyawan |=|=|=|=|=')
    print('1. Melanjutkan update karyawan')
    print('2. Kembali ke Main menu')
    pilihanuser = int(input('Silahkan pilih menu 1-2: '))
    if pilihanuser == 1:
        updates_karyawan()
    else:
        main_menu()

def updates_karyawan():
    while True:
        print('|=|=|=|=|= Menu Update Data Karyawan |=|=|=|=|=')
        print()
        
        emp_exists = False
        while not emp_exists:
            empy_id = int(input("Masukkan ID Karyawan yang ingin diupdate: "))
            tambahkaryawan = read_half_karyawan(empy_id)
            if tambahkaryawan is None:
                print('Data salah. Masukkan ID Karyawan yang benar.')
            else:
                emp_exists = True
       
        print("|=| Employee ID            :", tambahkaryawan['employee_id'])
        print("|=| Nama Karyawan          :", tambahkaryawan['nama_karyawan'])
        print("|=| Tahun Masuk            :", tambahkaryawan['tahun_masuk'])
        print("|=| Jabatan                :", tambahkaryawan['jabatan'])
        print("|=| Divisi                 :", tambahkaryawan['divisi'])
        print("|=| Asal Kota              :", tambahkaryawan['asal_kota'])        
        print("|=|=|")
#                                 
        update_more = input('Apakah benar ini data yang akan anda update? (Y/T): ').capitalize()
        if update_more == 'Y':
            while True:
                updatean = input('Silahkan update data yang ingin diubah (Nama/Tahun/Jabatan/Divisi/Asal): ').title()
                if updatean in ['Nama', 'Tahun', 'Jabatan', 'Divisi', 'Asal']:
                    new_value = input(f'Masukkan {updatean} yang baru: ').title()
                    if updatean == 'Nama':
                        new_nama_karyawan = new_value
                        new_tahun_masuk = ['tahun_masuk']
                        new_jabatan = ['jabatan']
                        new_divisi = ['divisi']
                        new_asal_kota = ['asal_kota']
                    elif updatean == 'Tahun':
                        new_nama_karyawan = ['nama_karyawan']
                        new_tahun_masuk = new_value
                        new_jabatan = ['jabatan']
                        new_divisi = ['divisi']
                        new_asal_kota = ['asal_kota']
                    elif updatean == 'Jabatan':
                        new_nama_karyawan = ['nama_karyawan']
                        new_tahun_masuk = ['tahun_masuk']
                        new_jabatan = new_value
                        new_divisi = ['divisi']
                        new_asal_kota = ['asal_kota'] 
                    elif updatean == 'Divisi':
                        new_nama_karyawan = ['nama_karyawan']
                        new_tahun_masuk = ['tahun_masuk']
                        new_jabatan = ['jabatan']
                        new_divisi = new_value
                        new_asal_kota = ['asal_kota'] 
                    elif updatean == 'Asal':
                        new_nama_karyawan = ['nama_karyawan']
                        new_tahun_masuk = ['tahun_masuk']
                        new_jabatan = ['jabatan']
                        new_divisi = ['divisi']
                        new_asal_kota = new_value 
                    edit_karyawan(empy_id, new_nama_karyawan, new_tahun_masuk, new_jabatan, new_divisi, new_asal_kota )
                    datakaryawanbaru = read_half_karyawan(empy_id)
                    print('Data karyawan telah berhasi diperbaharui!')
                    print("|=| Employee ID            :", datakaryawanbaru['employee_id'])
                    print("|=| Nama Karyawan          :", datakaryawanbaru['nama_karyawan'])
                    print("|=| Tahun Masuk            :", datakaryawanbaru['tahun_masuk'])
                    print("|=| Jabatan                :", datakaryawanbaru['jabatan'])
                    print("|=| Divisi                 :", datakaryawanbaru['divisi'])
                    print("|=| Asal Kota              :", datakaryawanbaru['asal_kota'])        
                    print("|=|=|")
                    if datakaryawanbaru != None:
                        read_all_karyawan()
                        main_menu() 

def delete_data_karyawan ():
    # os.system('cls')
    while True:
        print('|=|=|=|=|= Menu Menghapus Data Karyawan |=|=|=|=|=')
        read_all_karyawan()
        emp_id = int(input('Masukkan data karyawan yang ingin dihapus sesuai EmployeeID: '))
        if emp_id in [data['employee_id'] for data in DATABASE_KARYAWAN]:
            print('Lanjutkan menghapus data')
            
        else:
            print('Data tidak ditemukan!')
            continue
                       
        checker = input('Yakin ingin menghapus data? (Y/T): ').capitalize()
        print()
        if checker == 'T':
            main_menu()
        for karyawan in range(len(DATABASE_KARYAWAN)):
            if DATABASE_KARYAWAN[karyawan]['employee_id'] == emp_id:
                del DATABASE_KARYAWAN[karyawan]
                print(f'Karyawan dengan Employee ID {emp_id} telah berhasil di delete')
                return read_all_karyawan()
        print(f'Karyawan dengan Employee ID {emp_id} tidak ditemukan!')
            
            
        return None

def main_menu():
    os.system('cls')
    print('|=|=|=|=|= Main Menu |=|=|=|=|=')
    print('''
        1. List Karyawan
        2. Menambahkan Data Karyawan Baru
        3. Mengupdate Data Karyawan
        4. Menghapus Data Karyawan
        0. Exit Menu
        ''')
    menu = int(input("Masukkan menu yang ingin dijalankan: "))
    
    if menu == 1:
        menu_read_karyawan()   
    elif menu == 2:
        create_new_data_karyawan()
    elif menu == 3:
        update_karyawan()
    elif menu == 4:
        delete_data_karyawan()
        main_menu()
    elif menu == 0:
        exit()
while True:
    main_menu()