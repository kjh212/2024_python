subjects = "python c++ database linux"
subject=input("수강신청과목 입력 : ")
if subjects.find(subject) != -1: #index시 오류
    print(f'해당과목 존재. 위치는 {subjects.find('c++')}번 인덱스')
else:
    print(' 해당과목 존재 x')

subjects = "python c++ database linux"
subject=input("수강신청과목 입력 : ")
try:
    print(f'해당과목존재. 위치는 {subjects.index(subject)}번 인덱스')
except ValueError:
    print('해당과목 존재 x')

