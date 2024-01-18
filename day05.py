def squares(n):
    return n*n

even_numbers=[i for i in range(101) if i % 2==0]
print(even_numbers)
print(tuple(map(lambda x:x**2, even_numbers)))# = print(tuple(map(squares, even_numbers)))
z=lambda x:pow(x,2)
print(tuple(map(z, even_numbers))) #맵 뒤에 함수가 아닌 저런 대체함수도 가능
print(type(z)) # funtion