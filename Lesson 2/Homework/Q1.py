for i in range(9):
    if i<6:
        for x in range(i):
            print('*',end= '')
        print(end= '\n')
    else:
        for x in range(10-i):
            print('*',end= '')
        print(end= '\n')