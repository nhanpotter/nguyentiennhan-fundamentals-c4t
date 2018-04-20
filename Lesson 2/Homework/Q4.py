import random
while True:
    print("Welcome!")
    a= random.randint(1,9)
    c= int(input("Ban doan so nao? "))
    while c!=a:
        print("Do qua. NOT SO NICE")
        c= int(input("Again? "))
    print("Well guessed!")
    response= input("Play again? (yes or no)")
    if response != "yes":
        break
print("Bye <3")