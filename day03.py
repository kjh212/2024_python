subjects={'python' : 'kim', 'c++':'sung', 'database':'kang','data structure':'kim'}
print("{0[c++]} {0[data structure]}".format(subjects))

thing='wraith'
place='window'
print(('the {} is at the {}').format(thing,place))
    #the wraith is at the window
print(('the {:10s} is at the {:10s}').format(thing,place))
    #the wraith     is at the window
print(('the {:<10s} is at the {:<10s}').format(thing,place))
    #the wraith     is at the window
print(('the {:^10s} is at the {:^10s}').format(thing,place))
    #the   wraith   is at the   window
print(('the {:!^10s} is at the {:#^10s}').format(thing,place))
    #the !!wraith!! is at the ##window##