attempts= 0
while True:
    response= input("Do you want to quit?(y/n):")
    if response=="y":
        attempts+=1
    else:
        break
print("Exiting after",attempts,"attempts")