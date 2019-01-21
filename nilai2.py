n = int(input("Masukan Nilai Anda: "))

if n >= 100:
    print("nilai salah")
    exit()
elif n >= 86:
    predikat = "A"
elif n >= 81:
    predikat = "A-"
elif n >= 76:
    predikat = "B+"
elif n >= 71:
    predikat = "B"
elif n >= 66: 
    predikat = "B-"
elif n >= 61:
    predikat = "C+"
elif n >= 56:
    predikat = "C"
elif n >= 51:
    predikat = "C-"
elif n >= 46:
    predikat = "D+"
elif n >= 0:
    predikat = "D"
else:
    predikat = "tidak ada"
    
print ("predikat: ", predikat)