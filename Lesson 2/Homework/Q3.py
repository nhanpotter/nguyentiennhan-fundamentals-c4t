a=[];b=[]
for i in range(1500,2701):
    if (i%5)==0:
        a.append(i)
    if (i%7)==0:
        b.append(i)
print("Divisible by 5: ",a)
print("Divisible by 7: ",b)