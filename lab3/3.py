n = int(input("введите натуральное число: "))


for i in range(1,n+1):
    for x in range(1,i+1):
        print(x,end='')
    print()