list_temp=[1,1.3,'8',3,5,7,9,10.5]

summa=0
for el in list_temp:
    # if type(el)==float:
        summa+=float(el)

print(summa / len(list_temp))