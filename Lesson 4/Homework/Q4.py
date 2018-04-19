a= [(1,2,40),(0,15,60),(10,80,0)]
b= []
for i in a:
    c=[j for j in i]
    c[2]=100
    b.append(tuple(c))
print(b)