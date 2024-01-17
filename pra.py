#8.1
e2f={'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f)
#8.2
print(e2f['walrus'])
#8.3
f2e={}
for e,f in e2f.items():
    f2e[f]=e
print(f2e)
#8.4
print(f2e['chien'])
#8.5
print(set(e2f.keys()))
#8.6
life={'animal':{'cat':['Henri','Grumpy','Lucy'],'octopi':{},'emus':{}},'plants':{},'other':{}}
#8.7
print(set(life.keys()))
#8.8
print(set(life['animal'].keys()))
#8.9
print(set(life['animal']['cat']))
#8.10
squares={x: x*x for x in range(10)}
print(squares)