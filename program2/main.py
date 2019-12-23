from model.daftar_nilai import *
from view.view_nilai import *
print("Program Input Nilai")
print("===================")
while True:
    d = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if d.lower() == 't':
        tambah_data()
    elif d.lower() == 'l':
        lihat_data()
    elif d.lower() == 'k':
        break
    elif d.lower() == 'h':
        hapus_data()
    elif d.lower() == 'u':
        ubah_data()
    elif d.lower() == 'c':
        cari_data()
    else:
        print("Pilih menu yang tersedia")

