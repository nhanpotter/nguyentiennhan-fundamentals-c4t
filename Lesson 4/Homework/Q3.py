a= input("String: ")
c=[]
k= int(input("So k: "))
for i in range(len(a)-k+1):
    # b="" ##C1
    # for j in range(k):
    #     b+=a[i+j]

    b = a[i:i+k] #C2

    c.append(b)
print(c)
