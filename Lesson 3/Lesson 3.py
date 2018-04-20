#Question1
# for i in range(2000,3201):
#     if i%7==0 and i%35!=0:
#         print(i,end= ',')

#Question2
# a=1
# b= int(input('Tinh giai thua! ' ))
# for i in range(1,b+1):
#     a=a*i
# print(a)

#QuestionFunny
# for i in range(35):
#         if 2*i+4*(35-i)==94:
#             print("Chickens: ",i,"Rabbits: ",35-i)

#Question3
# d=dict()
# a= int(input("So can nhap? "))
# for i in range(1,a+1):
#     d[i]=i*i
# print(d)

#Question?
# a=1
# b= int(input('Nhap n?'))
# for i in range(b):
#     a= a+100
# print(a)

# def tinhtong(n):
#     if n==0:
#         return 1
#     else:
#         return tinhtong(n-1)+100
#
# print(tinhtong(3))

#Lesson
# x=10
# while x!=5:
#     x -=1
#     if x%2 !=0: continue
#     print(x)

# lop_C4T ={"Tenlop": "c4t","Siso":(15,29,"lol")}
# print(lop_C4T)
# print(lop_C4T.keys())
# print(lop_C4T.values())
#
# lop_C4T["Tenlop"]= "Ngon day"
# print(lop_C4T["Siso"])

#Question4
# a={}
# a["name"]= "bien"
# print(a)
# a["name"]= "hello"
# print(a)

# a= [x for x in (input("Day? ")).split(",")]
# print(a)
# print(tuple(a))

# a=(1,2,3)
# b=(1,2)
# print(hex(id(a)))
# a=a+b
# print(a)
# print(hex(id(a)))
#
# print("array")
# c=[1,2,3]
# print(hex(id(c)))
# c.append([1,2])
# print(c)
# print(hex(id(c)))



