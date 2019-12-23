from view.input_nilai import *
data = {}

def tambah_data():
    global data
    nama = input_nama()
    NIM = input_NIM()
    tugas = input_tugas()
    uts = input_uts()
    uas = input_uas()
    akhir = input_akhir()
    data[nama] = [nama, NIM, tugas, uts, uas, akhir]
    return data


def ubah_data():
    nama = input("Nama : ")
    if nama in data.keys():
        NIM = input("NIM : ")
        tugas = int(input("Nilai Tugas : "))
        uts = int(input("Nilai UTS : "))
        uas = int(input("Nilai UAS : "))
        data[nama][1] = NIM
        data[nama][2] = tugas
        data[nama][3] = uts
        data[nama][4] = uas
    else:
        print("Daftar nilai untuk anak yang bernama {0} tidak ada". format(nama))


def hapus_data():
    nama = input("Nama : ")
    if nama in data.keys():
        del data[nama]
    else:
        print("Daftar nilai untuk anak yang bernama {0} tidak ada".format(nama))




