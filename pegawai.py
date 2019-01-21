masa = int(input("Masa Kerja: "))
tunjangan = []

if masa >= 3:
    gaji = 6000000
    tunjangan.append("BPJS")
    tunjangan.append("Keluarga")
    tunjangan.append("Hari raya")
elif masa >= 2:
    gaji = 5500000
    tunjangan.append("BPJS")
    tunjangan.append("Keluarga")
elif masa >= 1:
    gaji = 4000000
    tunjangan = "Tidak ada"
else:
    print("ERROR")

print("----------------------")
print("Masa Kerja:", masa)
print("tunjangan:", tunjangan)