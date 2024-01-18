def menu(wine,entree,dessert):
    return{'wine':wine,"entree":entree,"dessert":dessert}

print(menu('ww',',dd',"wwd"))

def menu1(wine,entree,dessert='cake'): #기본값 정하기
    return{'wine':wine,"entree":entree,"dessert":dessert}

print(menu1("11",'22')) #{'wine': '11', 'entree': '22', 'dessert': 'cake'}

def buggy(arg,result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b') #['a', 'b'] 위에 a를 넣었기에 같이 나옴

def buggy1(arg):
    result=[]
    result.append(arg)
    return print(result)
buggy1('a')
buggy1('b')

def nonbuggy(arg,result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

def print_arg(*args): #*args 여기서 *은 튜플로 출력
    print('position:',args)

print_arg() # position:()
print_arg(33,4,'343') #(33,4,'343')

def print_more(re,*args):
    print('ss:',re)
    print('dd:',args)
print_more(3,3) #ss: 3, dd: (3,)

args=(2,5,7,'x')
print_arg(2,5,7,'x')
print_arg(args)
print_arg(*args)

def print_kwargs(**kwargs): # ** 딕셔너리 매개변수
    print('keyword argument: ', kwargs)

print_kwargs()
print_kwargs(wine='merlot',entree='button')
