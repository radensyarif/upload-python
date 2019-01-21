print ("-----pengitung nilai----")
nilai = int(input("Masukan nilai anda: "))

if nilai <= 65 and nilai >=0:
    print ("nilai anda: ",nilai, " \nMutu nilai : D")
elif nilai > 70 and nilai <=75:
    print ("nilai anda: ",nilai, " \nMutu nilai : C")
elif nilai > 75 and nilai <=80:
    print ("nilai anda: ",nilai, " \nMutu nilai : B")
elif nilai > 80 and nilai <=100:
    print ("nilai anda: ",nilai, " \nMutu nilai : A")
else:
    print ("Nilai yang anda masukan salah!!!")