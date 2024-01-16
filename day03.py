number=int(input("input number : "))
is_prime = True #int->book
if number <2:
    print(f'{number} is not prime')
else:
    i=2
    while i<number:
        if number % i == 0:
            is_prime = False
            break
        i+=1
    if is_prime :
        print(f'{number} is prime number')
    else:
        print(f'{number} is not prime')