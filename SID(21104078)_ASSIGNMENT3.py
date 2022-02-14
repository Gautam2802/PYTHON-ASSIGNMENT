#***********************Solution 1**********************

# program for Counting the number of occurence of each word/character in single word
real_string = input("Enter the String:")
print()

input_string = real_string.lower()       ;'''real_string to variable'''

# Condition to check if the string entered is single word or sentence.
if " " in input_string:
    input_string = input_string.split()
elif len(input_string) == 0:              '''Checking the empty string.'''
print("Empty String Has been Entered")

'''Count the occurrences with function.'''
output_set = []
for j in input_string:
    count = input_string.count(j)
    output_set.append(f"Occurrences of {j} in \"{real_string}\": {count}\n")

'''Removing  repetitive outputs using a set.'''
output_set = set(output_set)
for k in output_set:
    print(k)

print("." * 100)

#**********************Solution 2***********************

# program for finding Next date from input date

'''Program to check the leap year'''
def Check_leap(y):
    if (y % 4) == 0:
        if (y % 100) == 0:
            if (y % 400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap

'''next date finder'''

DAY=int(input("Enter the Day: "))
MONTH=int(input("Enter the Month: "))
YEAR=int(input("Enter the Year: "))

if MONTH< 1 or MONTH > 12:
    print("\nError!: Date entered is out of range.")
    exit()

elif DAY < 1 or DAY > 31:
    print("\nError!: Date entered is out of range.")
    exit()

elif YEAR < 1800 or YEAR > 2025:
    print("\nError!: Date entered is out of range.")
    exit()

output_day = DAY
output_month = MONTH
output_year = YEAR

if MONTH in [1, 3, 5, 7, 8, 10]:
    if DAY == 31:
        output_day = 1
        output_month += 1
    else:
        output_day += 1

elif MONTH in [4, 6, 9, 11]:
    if DAY == 30:
        output_day = 1
        output_month += 1
    else:
        output_day += 1

elif MONTH == 12:
    if DAY == 31:
        output_day = 1
        output_month = 1
        output_year += 1

elif MONTH == 2:
    if Check_leap(YEAR):
        if DAY > 29:
            print("\nError!: Date entered is out of range.")

        elif DAY == 29:
            output_day = 1
            output_month += 1
        else:
            output_day += 1
    else:
        if DAY > 28:
            print("\nError!: Date entered is out of range.")

        elif DAY == 28:
            output_day = 1
            output_month += 1
        else:
            output_day += 1

output_date = f"{output_day}/{output_month}/{output_year}"
print("\nThe next Date is :", output_date)

print("." * 100)

# **********************Solution 3***********************

#program for List of tupples with first element(number) and second element(square of numbers)

Numbers = input("Enter the list of numbers(Enter the numbers separated by space):")

# Converting the input entered by the user into a list of containing integer datatypes using map function.
chr_lst = list(map(int, Numbers.split()))

final_list = []
for j in chr_lst:
    final_list.append((j, j ** 2))

print()
print(final_list)

print("." * 100)

#**********************Solution 4***********************5

#program for finding grade and performance 
Grade_Points = int(input("Enter the Grade Point: "))

if Grade_Points >10 or Grade_Points < 4:
    print("Incorrect! Grade Point is out of range")
    exit()

else:
    student_grades_dictionary={10: ['A+', 'Outstanding'], 9: ['A', 'Excellent'], 8: ['B+', 'Very Good'], 7: ['B', 'Good']
                            , 6: ['C+', 'Average'], 5: ['C', 'Below Average'],4: ['D', 'Poor']}
print(f"\tYour letter Grade is: {student_grades_dictionary[Grade_Points][0]}")
print(f"\tYour performance is: {student_grades_dictionary[Grade_Points][1]}")
 
print("." * 100)

# #**********************Solution 5***********************

# program for reverse pyramid pattern

n = 6

for j in range(n):
    
    for k in range(j):
        print(' ', end='')
    
    for k in range(2*(n-j)-1):
        print(chr(65 + k), end='')
    print()

print("." * 100)

# #**********************Solution 6***********************

#program to add student detail repeatedly

dictionary1={}
while True:
    NAME=input("Enter the name of the student: ")
    SID=int(input("Enter the SID the student: "))
    dictionary1[SID]=NAME
    while True:
        More_details=input(" Do you want to enter more details press y/n: ")
        if More_details==("y"):
            More_details=1
            break
        elif More_details==("n"):
            More_details=0
            break
        else:
            print("Enter only y/n")
            continue
    if More_details==0:
        break
    
print("\t The Students Details Are:- ")
for x in dictionary1:
    print(f"\t The SID of %s is %d:"%(dictionary1[x],x))

print("-" * 50)

print("(b): Sorting  Details Using Student Names")
dictionary2={}
for sorted_value in sorted(dictionary1.values()):
    for key,value in dictionary1.items():
        if value==sorted_value:
            dictionary2[key]=value
for x in dictionary2:
    print(" The SID of %s is %d :" %(dictionary2[x],x))

print("-" * 50)

print("(c): Sorting Details Using SID: ")    
dictionary3={}
for sorted_key in sorted(dictionary1.keys()):
    for key,value in dictionary1.items():
        if key==sorted_key:
            dictionary3[key]=value
for x in dictionary3:
    print(" The SID of %s is %d :" %(dictionary3[x],x))

print("-" * 50)

print("(d): Search a student details with SID and print name: ")
while True:
    search_sid=int(input(" Enter the SID of student whose details you want to search: "))
    if search_sid in dictionary1:
        print(" The name of the student whose SID is %d is %s" %(search_sid,dictionary1[search_sid]))
        break
    else:
        print("The SID you entered is invalid:")
        continue

print("." * 100)

#**********************Solution 7***********************

# program to print fibonacci series as the input gather
nterms = int(input("Number of fibonacci terms to be printed: "))

'''first two terms'''
n1, n2 = 0, 1
count = 0

'''checking if the number of terms is valid for fibonacci'''
if nterms <= 0:
   print("Incorrect,Please enter a positive integer")
# if there is only one term, return n166
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
#generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

print("." * 100)

#**********************Solution 8 **********************

# program for following set questions

set1 ={1,2,3,4,5}
set2 ={2,4,6,8}
set3 ={1,5,9,13,17}

#*******Part a**********
A=(set1 | set2)-(set1 & set2)   ; '''A=Set'''
print ("A = ",A)

#*******Part b**********
B=(set1|set2|set3)-(set1&set2)-(set2&set3)-(set3&set1)    ; '''B=Set'''
print ("B = ",B)

#*******Part c**********
C=(set1 & set2) | (set1 & set3)    ; '''C=Set'''
print ("C = ",C)

#*******Part d**********
D={1,2,3,4,5,6,7,8,9,10}       ; '''D=Set'''
print("D = ",D-set1)

#*******Part e**********
E={1,2,3,4,5,6,7,8,9,10}      ; '''E=Set'''
print("E = ",E-(set1|set2|set3)) 

print("." * 100)