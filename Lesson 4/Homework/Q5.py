def sapxep(a):
    b=[]
    while len(a):
        z=a[0]
        for i in a:
            if z>=i:
                z=i
        a.remove(z)
        b.append(z)
    return b

print(sapxep([4,8,1,3,2,9,5,7,6]))
