import copy

subjects = ["a",["b","c"],"d"]
a=subjects
b=subjects.copy()
c=list(subjects)
d=subjects[:]
e=copy.deepcopy(a)
print(subjects,a,b,c,d,e)
subjects[0]='x'
subjects[1][1]='y'
print(subjects,a,b,c,d,e)
#subjects=['x', ['b', 'y'], 'd']
#a=['x', ['b', 'y'], 'd']
#b=['a', ['b', 'y'], 'd']
#c=['a', ['b', 'y'], 'd']
#d=['a', ['b', 'y'], 'd']
#e=['a', ['b', 'c'], 'd']