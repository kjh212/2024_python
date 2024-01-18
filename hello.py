def print_data(data,*,start=0,end=100): # *이있으면 기본값으로 사용하기 싫으면 따로 설정(기본값으로 쓰란얘기)
    for value in (data[start:end]):
        print(value)
data=['a','b','c','d','e']
print_data(data)