#Başlangıç ve bitiş değeri verilen sayının arasındaki sayıların toplamını bulan program
baslangıc=int(input("başlangıç değerini giriniz "))
bitis=int(input("bitiş değerini giriniz "))
toplam=0
if 0<=baslangıc<=100 and 0<=bitis<=100:
    for i in range(baslangıc,bitis+1):
        toplam+=i
    print(toplam)
        
            