from model.daftar_nilai import data


def cari_data():
    nama = input("Nama : ")
    if nama in data.keys():
        print("=============================================================================")
        print("|     Nama     |      NIM     |   Tugas   |   UTS   |   UAS   |    Akhir    |")
        print("=============================================================================")
        print("|  {nama:10}  |  {NIM:10}  |   {tugas:5}   |   {uts:3}   |   {uas:3}   |    {akhir:3.2f}    |".format(
            nama=data[nama][0], NIM=data[nama][1], tugas=data[nama][2], uts=data[nama][3], uas=data[nama][4],
            akhir=data[nama][5]))
        print("=============================================================================")
    else:
        print("Daftar nilai untuk anak yang bernama {0} tidak ada".format(nama))


def lihat_data():
    print("Lihat nilai")
    print("===================================================================================")
    print("| No. |     Nama     |      NIM     |   Tugas   |   UTS   |   UAS   |    Akhir    |")
    print("===================================================================================")
    no = 1
    if data.keys():
        for x in data.values():
            print(
                "|  {:2} |  {nama:10}  |  {NIM:10}  |   {tugas:5}   |   {uts:3}   |   {uas:3}   |    {akhir:3.2f}    |".format(
                    no, nama=x[0], NIM=x[1], tugas=x[2], uts=x[3], uas=x[4], akhir=x[5]))
            no += 1
    else:
        print("|                                  TIDAK ADA DATA                                 |")
    print("===================================================================================")