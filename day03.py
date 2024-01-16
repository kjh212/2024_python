number=int(input("input number : "))
cnt = 0
i=1
while i<=number:
    if number % i == 0:
        cnt = cnt +1
    i+=1
if cnt == 2:
    print(f'{number} is prime number')
else:
    print(f'{number} is not prime')