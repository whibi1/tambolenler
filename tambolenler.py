def tambol(sayi):
    tam_bolenler=[]
    for i in range (2,sayi):
        if (sayi % i ==0):
            tam_bolenler.append(i)
    return tam_bolenler
        
while True:
    sayi=int(input("lütfen sayıyı girin\n"))
        print("tambolenler",tambol(sayi))
