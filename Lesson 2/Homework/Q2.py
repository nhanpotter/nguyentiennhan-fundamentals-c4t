import random
b=[]
for i in range(10):
    b.append(random.randint(0,1000))
print(b)
x=0;y=0
for i in b:
    if (i%2)==0:
        x=x+1
    else:
        y=y+1
print('Number of even numbers: ',x)
print('Number of odd numbers: ',y)