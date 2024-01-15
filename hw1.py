menu = int(input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : "))

while menu <= 3:
    if menu == 1:
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
        menu+=1
    elif menu == 2:
        celsius = float(input('Input Celcius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
        menu +=1
    else:
        print("terminate program")
        menu+=1