def input_nama():
    global nama
    nama = input("Nama : ")
    return nama
def input_NIM():
    global NIM
    NIM = input("NIM : ")
    return NIM
def input_tugas():
    global tugas
    tugas = int(input("Nilai Tugas : "))
    return tugas
def input_uts():
    global uts
    uts = int(input("Nilai UTS : "))
    return uts
def input_uas():
    global uas
    uas = int(input("Nilai UAS : "))
    return uas
def input_akhir():
    global akhir
    a = int(tugas * 30 / 100)
    b = int(uts * 35 / 100)
    c = int(uas * 35 / 100)
    akhir = a + b + c
    return akhir