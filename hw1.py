menu = int(input("1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit\n3) find prime            4) find prime in range\n : "))

if menu == 1:
    fahrenheit = float(input('Input 1 Fahrenheit : '))
    print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')

elif menu == 2:
    celsius = float(input('Input Celcius : '))
    print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
elif menu ==3:
    number = int(input("input number : "))
        if isprime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is not prime')
elif menu ==4:
    numbers = input("input first second number : ").split()
    n1 = int(numbers[0]) #간소화
    n2 = int(numbers[1]) #
    if n1 > n2:          #
        n1, n2 = n2, n1  #
    for number in range(n1, n2 + 1):
        is_prime = True

        if number < 2:
            pass
        else:
            for i in range(2, number): #중복코드
                if number % i == 0:    #
                    is_prime = False   #
                    break              #
            if is_prime:
                print(number, end=' ')
else:
    print("quit program")