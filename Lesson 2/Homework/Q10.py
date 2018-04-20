a =[x for x in input("Nhap so: ").split(",")]
for i in a:
    b= int(i,2)
    if b%5==0:
        print(i)