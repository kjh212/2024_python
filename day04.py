t1=(5) #','가없어서 튜플 x
t2=5,
t3=(5,)
t4=(5,7)
t5=5,7 #굳이 소괄호 안쳐도 튜플
print(type(t1),type(t2),type(t3),type(t4),type(t5))
t6= "python","kim" #packing
print(type(t6),t6[1])
subject, prof = t6
print(prof) # kim 이 나옴, subject 는 python
#a,b,c = t6 #error (2개면 2개로 받아야됨, 2개인데 3개로 받으면 에러)
t7 = () # 비어있으면 콤마 없어도 튜플
t8 = tuple() # 튜플로 변환

type('asdf',) #string
type(('asdf',)) #tuple
print(type(prof)) #unpacking 하면 str

# tuple 연상
print(('ta',)+('ka',)) # ('ta','ka')
print(('ta',)*3) # ('ta','ta','ta')

#a=(7,2), b=(7,2,9), a<=b

t11= 4.43,
t12= 3.97, 4.1, 3.27
print(id(t11))
t11+=t12
print(id(t11))