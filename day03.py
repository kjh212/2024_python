# - split
#course = "2024 KEB Bootcamp"
#print(course)
#list_course=course.split()
#print(list_course)
#list_course2=course.split('B')
#print(list_course2)

# - split 활용
#numbers=input("Firstnumber SecondNumber : ").split('b')
#print(int(numbers[0]) + int(numbers[1]))

# -join
subjects=["python","c++","database"]
subjects_string='/'.join(subjects)
print(subjects_string)

# - replace
course = "* KEB 2024 KEB Bootcamp KEB.!#"
print(course.replace("KEB","inha"))
print(course)
course = course.replace("KEB","inha")
print(course)
print(course.replace("2","1",2))

# - strip
print(course.strip())
print(course.strip("!.#*"))

# -find,index
course = "* KEB 2024 KEB Bootcamp KEB.!#"
print(course.find('KEB'))
print(course.rfind('KEB'))
print(course.index("KEB"))

print(course.find('inha')) #-1
print(course.index('inha')) #ValueError