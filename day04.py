x='1','2','3'
y='4','5','6'
z=list(zip(x,y))
r=dict(zip(x,y))
print(z,r)
#z=[('1', '4'), ('2', '5'), ('3', '6')]
#r={'1': '4', '2': '5', '3': '6'}

number_list=[x*x for x in range(1,6) if x%2==1]
print(number_list)
