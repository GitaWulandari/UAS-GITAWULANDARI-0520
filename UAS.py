import mysql.connector
import os

#koneksi
config = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_akademik_0520"
)

#if config.is_connected():
 #   print("koneksi berhasil")
#cursor = config.cursor()
#sql = "INSERT INTO tbl_students_0520 (ID,NIM,NAMA,JK,JURUSAN,ALAMAT) VALUES (%s, %s, %s, %s, %s, %s)"
#val = ("50","20.90.1288","Intan Mawar Anisa","P","Teknik Komputer","Yogyakarta")
#cursor.execute(sql, val)
#config.commit()
#print("{} data ditambahkan".format(cursor.rowcount))

def select_all_data():
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0520"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("data tidak tersedia")
    else:
        for data in results:
            print(data)


def select_limit_data():
    LIMIT = int(input("Masukkan Limit: "))
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0520 ORDER BY ID LIMIT 5"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount < 0:
        print("data tidak tersedia")
    else:
        for data in results:
            print(data)
            
def select_single_data():
    NIM = input("Masukkan NIM: ")
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0520 WHERE NIM=%s"
    val = (NIM,)
    cursor.execute(sql, val)
    results = cursor.fetchone()
    
    if cursor.rowcount < 0:
        print("data tidak tersedia")
    else:
        print("Data NIM", NIM, "Ditemukan!")
        for data in results:
            print(data)

            


def menu():
    print("\n============================D A T A   M A H A S I S W A============================")
    print("1. Tampilkan semua Data")
    print("2. Tampilkan data berdasarkan Limit")
    print("3. Cari Data berdasarkan NIM")
    print("0. Keluar")
    option = input("Pilih menu> ")

    os.system("clear")

    if option == "1":
        select_all_data()
    elif option == "2":
        select_limit_data()
    elif option == "3":
        select_single_data()
    elif option == "0":
        exit()
    else:
        print("Menu Salah!")


if __name__ == "__main__":
    while(True):
        menu()


