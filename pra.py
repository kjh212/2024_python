#6.1
y=[x for x in range (3,-1,-1)]
print(y)

#6.2
guess_me=7
number=1
while number<=guess_me+1:
    if number<guess_me:
        print(f'{number} too low')
    elif number==guess_me:
        print('found it!')
    elif number>guess_me:
        print('oops')
        break
    number+=1

#6.3
guess_me=5
for number in range (10):
    if number<guess_me:
        print(f'{number} too low')
    elif number==guess_me:
        print('found it!')
    elif number>guess_me:
        print('oops')


