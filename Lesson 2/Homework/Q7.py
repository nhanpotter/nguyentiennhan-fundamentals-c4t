a= [0,1]
for i in range(1000):
    x= a[i]+a[i+1]
    if x <50:
        a.append(x)
    else:
        break
print(a)