#Enter year of birth
# yob= int(input('Nam sinh?'))
# age= 2018-yob
# print('age= ',age)
# if age<14:
#     print('Baby!')
# if 14<=age<18:
#     print('Teenager')
# else:
#     print('Adult')

#Giai pt bac 2 ax^2+bx+c=0
# import math
# a= float(input('Nhap a:'))
# b= float(input('Nhap b:'))
# c= float(input('Nhap c:'))
# delta= b**2-4*a*c
# if a==0:
#     print('Khong phai phuong trinh bac 2')
# elif delta<0:
#     print('PT vo nghiem')
# elif delta==0:
#     print('PT co nghiem kep= ',-b/(2*a))
# else:
#     x1= (-b+math.sqrt(delta))/(2*a)
#     x2= (-b-math.sqrt(delta))/(2*a)
#     print("PT co 2 nghiem phan biet=",x1,' va ',x2)

#Khai bao array

# a = [5,2,3,4]
# print(len(a))
# sum = 0
# for i in range(len(a)): #range tinh tu 0
#     sum = sum+a[i]
# print('sum of a: ',sum)

import random
a = []
for i in range(100):
    a.append(random.randint(1,20))
for i in range(100):
    print(a[i],end= " ")

# b=[]
# for i in range(20):
#     b.append(random.randint(0,1000))
# for i in range(20):
#     print(b[i],end= ' ')
# x = b[0]
# for i in range(20):
#     if b[i]>=x:
#         x = b[i]
# print(end= '\n')
# print(x)

# a = [1,"xinchao",{2,3}]
# b = [[1,4],[2,3,4],1]
# c = [{1,2,3,4},{8,7,9,19}]
# for x,y,z,p in c:
#     print(x,y,z,p)

# a = [4,6,8,9]
# print(a[2:4])

# a = ["sad","happy"]
# n = '''░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░
# ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░
# ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░
# ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░
# ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░
# ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░
# ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░
# █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█
# █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█
# █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█
# █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█
# ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░
# ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░
# ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░
# ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░
# ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░'''
# print(n)

#khai bao ham con
#from sub_function import*
import sub_function as sf

b = [2,5,7]
sum = sf.tinh_tong_mang(b)
print(sum)


