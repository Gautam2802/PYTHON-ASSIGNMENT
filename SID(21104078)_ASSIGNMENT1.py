#***************Solution 1****************
x=int(input('ENTER NUMBER 1:  '))
y=int(input('ENTER NUMBER 2:  '))
z=int(input('ENTER NUMBER 3:  '))
RESULT=(x+y+z)/3
print('the average of numbers is: ', RESULT)

print()
print()

#***************Solution 2****************
income=int(input('Enter your gross income:  '))
dep=int(input('Enter number of dependents:  '))
t= income-10000-(dep*3000)
print('your annual tax is:  ', t*0.2)

print()
print()

#***************Solution 3****************
Name=str(input('Enter your name:  '))
SID=int(input('Enter your sid:  '))
print('Type M for male,F for female U for unknown')
Gender=str(input('Enter your gender:  '))
Course=(input('Enter your course name:  '))
CGPA=int(input('Enter your Cgpa:  '))
Student=[Name,SID,Gender,Course,CGPA]
print(Student)

print()
print()

#***************Solution 4****************
Marks1=int(input('Enter marks of 1st student: '))
Marks2=int(input('Enter marks of 2nd student: '))
Marks3=int(input('Enter marks of 3rd student: '))
Marks4=int(input('Enter marks of 4th student: '))
Marks5=int(input('Enter marks of 5th student: '))
Marks=[Marks1,Marks2,Marks3,Marks4,Marks5]
Marks.sort()
print(Marks)

print()
print()

#***************Solution 5****************
color=['Red','Green','White','Black','Pink','Yellow']
print(color)
#***********Part A*************
del color[3]
print('New list is:', color)
#***********Part B*************
color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=['purple']
print('Answer for part B: ', color)

