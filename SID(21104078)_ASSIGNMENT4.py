#***************************Solution 1*********************************

# tower of hanoi

count = 0
def towerofhanoi(n, prime_rod, terminal_rod, auxilliary_rod):
    global count
    if n == 0:                                                                                          #Base case
        return
    count += 1
    towerofhanoi(n-1, prime_rod, auxilliary_rod, terminal_rod)                                                #Recursive call
    print("Move disk",n,"from rod",prime_rod,"to rod",terminal_rod)
    towerofhanoi(n-1, auxilliary_rod, terminal_rod, prime_rod)

no_of_discs = int(input("Number of discs: "))
print("\nA is the prime rod\nB is the auxilliary rod\nC is the terminal rod\n\nSteps:")
towerofhanoi(no_of_discs, 'A', 'C', 'B')
print("\nNumber of steps will be: %d" % (count))




print("." * 100)
#***************************Solution 2*********************************

#pascal triangle using recursion
while True:
    num = int(input("Enter the number of rows you want to be printed: "))
    if num>=0:
          break
    else:
       print("INVALID! NUMBER OF ROWS MUST BE POSITIVE")

print("The pascal triangle with recursion is: ")
def pascals_triangle(n):
    if n==0:
        return[[0]]
    elif n==1:
        return[[1]]
    else:
        output=pascals_triangle(n-1)
        existing_row=[1]
        last_row=output[-1]
        for i in range(len(last_row)-1):
            existing_row.append(last_row[i]+ last_row[i+1])
        existing_row +=[1]
        output.append(existing_row)
    return output

for i in pascals_triangle(num):
    print((num-len(i))*" ",end="")
    for j in i:
        if j !=0:
            print(j, end =" ")
    print()    


print('-'*50)

#Pascal triangle using Iteration
while True:
    n_rows = int(input("Enter the number of rows you want to be printed: "))
    if n_rows>=0:
          break
    else:
       print("INVALID! NUMBER OF ROWS MUST BE POSITIVE")


arr = [[1]]

# Using while to append next 'n-1' rows into the array.
while len(arr) < n_rows:

    new_row = [1]
    last_row = arr[-1]

    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])

    new_row += [1]
    arr.append(new_row)

# Printing the array containing the triangle as string.
width = len(str(arr[-1])) - 2
for i in arr:
    stri_ng = ""

    for j in i:
        stri_ng += (f"{j}" + "   ")

    print(stri_ng.center(width * 2, " "))



print("." * 100)
#***************************Solution 3*********************************
num1=int(input("Enter the first Integer: "))
num2=int(input("Enter the second Integer: "))
 
a, b= divmod(num1, num2)
print("Quotient: ", a)
print("Remainder: ", b)
output=[a, b]
  


print('-'*50)
#****************PartA******************
if callable(divmod):
    print("The function is Callable")
else:
    print("The function is not Callable")



print('-'*50)
#****************PartB******************
if 0 in [num1, num2]+list(output):
    print("All the values are not non-zero.")

elif 0 not in [num1, num2]+list(output):
    print("All the values are non-zero.")



print('-'*50)
#****************PartC******************
output.extend([4, 5, 6])
print("After adding 4,5,6 : ", output)
filtered = filter(lambda n: n > 4, output)
print("Values greater than 4 are : ", list(filtered))


print('-'*50)
#****************PartD******************
set_of_output=set(output)
print("Converted set: ",set_of_output)


print('-'*50)
#****************PartE******************
frzn_set=frozenset(set_of_output)
print("IMMUTABLE SET:  ",frzn_set)


print('-'*50)
#****************PartF******************
output=max(frzn_set)
print("Maximum value: ",output)
print("integer hash value of Max value: ",hash(output))


print("." * 100)
#***************************Solution 4*********************************
#Creating a class named Student
class student:
    def __init__(self,_NAME:str,_ROLLNO:int):
        self.name = _NAME
        self.rollno=_ROLLNO
    
    def __del__(self):
        '''Using del function for created points'''
        print("ALL THE OBJECTS ARE DELETED")

#creating a point
Gautam= student("Gautam Singal",21104078)
print(f"NAME ={Gautam.name}\nROLLNO = {Gautam.rollno}")



print("." * 100)
#***************************Solution 5*********************************

def details():
    print("\nDETAILED ACCOUNTS OF EMPLOYEES")
    print("Employee\tName\t\tSalary")
    print('-'*50)
    print(f"{Mehak.Employee_no}\t\t{Mehak.Name}\t\t{Mehak.Salary}")
    print(f"{Ashok.Employee_no}\t\t{Ashok.Name}\t\t{Ashok.Salary}")
    print(f"{Viren.Employee_no}\t\t{Viren.Name}\t\t{Viren.Salary}")

class Employees:

    def __init__(self,_employee: int, _name: str, _salary: int):
        
        self.Employee_no = _employee
        self.Name = _name
        self.Salary = _salary

    def __del__(self):


        pass

#putting employees detail
Mehak = Employees(1,"Mehak", 40000)
Ashok = Employees(2,"Ashok", 50000)
Viren = Employees(3,"Viren", 60000)

details()



print('-'*50)
#****************PartA******************
#update salary
Mehak_Salary=70000
print("\nThe Updated salary of Mehak is, ",Mehak_Salary)



print('-'*50)
#****************PartB******************
#Deleting record of one employee Viren

del Viren

print("\nDETAILED ACCOUNTS OF EMPLOYEES AFTER UPDATION")
print("Employee\tName\t\tSalary")
print('-'*50)
print(f"{Mehak.Employee_no}\t\t{Mehak.Name}\t\t{Mehak.Salary}")
print(f"{Ashok.Employee_no}\t\t{Ashok.Name}\t\t{Ashok.Salary}")



print("." * 100)
#***************************Solution 6*********************************
George_word=(input("Enter the word utter by George: "))
Barbie_word=(input("Enter the word utter by Barbie: "))

#making a list and sorting
George_list=list(George_word)
Barbie_list=list(Barbie_word)
George_list.sort()
Barbie_list.sort()
print()

#conditions
if George_list == Barbie_list:
    print("CONGRATULATIONS! Their Friendship is true.")  

elif len(Barbie_word) == 0:
    print("ALAS! Their Friendship is Fake.")

elif len(George_word) == 0:
    print("Error!: George's word cannot be empty.")

else:
    print("INPUT ERROR! Their Friendship is Fake.")

if len(George_word) != len(Barbie_list):
    print("INVALID! The letters of both words are not exactly same.")
    exit()    



print("." * 100)
