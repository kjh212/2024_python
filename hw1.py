menu = int(input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : "))


if menu == 1:
    fahrenheit = float(input('Input 1 Fahrenheit : '))
    print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')

elif menu == 2:
    celsius = float(input('Input Celcius : '))
    print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
elif menu ==3:
