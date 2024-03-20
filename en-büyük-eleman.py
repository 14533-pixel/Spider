#Dizideki en büyük sayıyı bulan program
liste=[12,14,5,67,34,23]
enb=liste[0]
for i in liste:
    if i>enb:
        enb=i
print(enb)
            