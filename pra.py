a=int(input("Input the first number :"))
b=int(input("Input the second number :"))
number=int(3)
for number in range (a,b):
    natural = int(2)
    while natural <= (number-1):
        if number % natural == 0:
            break
        natural+=1
    else:
        print(f'{number} is prime')
    number+=1
