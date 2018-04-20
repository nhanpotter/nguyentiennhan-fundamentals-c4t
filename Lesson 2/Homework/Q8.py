for i in range(1,51):
    if i%15 ==0:
        print("Fizzbuzz")
    elif i%15 !=0 and i%3 ==0:
        print("Fizz")
    elif i%15 !=0 and i%5 ==0:
        print("Buzz")
    else:
        print(i)