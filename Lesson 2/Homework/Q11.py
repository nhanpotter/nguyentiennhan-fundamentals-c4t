a = input("Input string: ")
l =0
d =0
for i in a:
    if i.isdigit():
        d = d+1
    elif i.isalpha():
        l = l+1
print ("letters: ",l,"\ndigits: ",d)