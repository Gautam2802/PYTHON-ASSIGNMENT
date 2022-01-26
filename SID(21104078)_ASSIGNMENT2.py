#*******************Solution1***********************
 
# Heading
print("\nString Operations\n")
 
# ORIGINAL STRING
string = ("Python is a case sensitive language")
print("The original String is: \"{}\"".format(string))
 
# *********Part A************
  # Finding the length of the given string using length function
length = len(string)
print("\tlength of the given string: ", length)
 
# *********Part B*************
 # Printing out the sting in reverse order using slicing.
print("\tThe reverse order of string is: \"{0}\"".format(string[::-1]))
 
# *********Part C*************
 # Slicing the string and storing the value in a new variable named new_string.
new_string = string[10:26]
print("\tNew String: \"{0}\"".format(new_string))
 
# *********Part D*************
 # Replacing words in string using replace command and printing out the changed string.
print("\tString after the changes: \"{0}\"".format(string.replace("a case sensitive", "object oriented")))
 
# *********Part E*************
 # Finding the index of 'a' and printing it out.
print("\tIndex of \"a\" in the given string:",string.find("a"))
 
# *********Part F*************
 # Removing the white spaces from the string and printing it out.
print("\tString after removing the white spaces: \"{0}\"".format(string.replace(" ", "")))
 
print("." * 120)
 
 
#********************Solution 2**********************
 
# Heading
print("\nString Formatting\n")
 
# Taking inputs from user.
NAME = input("Enter your Name: ")
SID = int(input("Enter your SID: ")) 
DEPARTMENT_NAME = (input("Enter the name of your department: ")) 
CGPA = float(input("Enter your CGPA: "))  
print()
# Printing out the strings after doing string formatting using .format() command.
print("Hey {0} Here!\nMy SID is {1}\nI am from {2} department and my CGPA is {3}.".format(NAME,SID,DEPARTMENT_NAME,CGPA))
 
print("." * 120)
 
 
#*********************Solution 3*********************
 
# Heading
print("\nBitwise Operators\n")
 
# Assigning given values to variables a and b.
a = 56
b = 10
# printing out the variables.
print("a:", a)
print("b:", b)
print()
 
# *********Part A*************
 # AND operator.
print("a & b: ", a & b)
 
# *********Part B*************
 # OR operator.
print("a | b: ", a | b)
 
# *********Part C*************
 # XOR operator.
print("a ^ b: ", a ^ b)
 
# **********Part D************
 # left bit shifting.
print("Left shifting both a and b with 2 bits: a={0},b={1}".format(a << 2, b << 2))
 
# **********Part E************
 # right bit shifting.
print("Right shifting a with 2 and b with 4 bits: a={0},b={1}".format(a >> 2, b >> 4))
 
print("." * 120)
 
 
#******************Solution 4*********************
 
# Heading.
print("\nGreatest Number Calculator\n")
 
# Taking inputs of num=numbers from users.
Number1 = float(input("Enter your first number: "))
Number2 = float(input("Enter your second number: "))
Number3 = float(input("Enter your third number: "))
# Using conditional statements to compare the numbers entered by the user.
# condition to check if Number1 is greatest.
if (Number1 >= Number2) and (Number1 >= Number3):
    greatest = Number1                              ;'''greatest is a variable used to store the greatest number'''
# condition to check if Number2 is greatest.
elif (Number2 >= Number3) and (Number2 >= Number1):
    greatest = Number2
# remaining condition: Number3 is greatest.
else:
    greatest = Number3
# printing out the greatest of the three numbers.
print("Greatest of the three numbers entered:",greatest)
 
print("." * 120)
 
#******************Solution 5**********************
 
# Heading
print("\nString Comparison\n")
 
# Taking input from the user and storing it in a variable named user_input.
user_detail = (input("Enter the string: "))
# condition to check if "name" present in user_detail.
if "name" in user_detail:
    print("Yes")
else:
    print("No") 
 
print("." * 120)
 
#******************Solution 6*********************
 
# Heading
print("\nTriangle Validity Checker\n")
 
# Taking input of triangle side:- a,b and c from the user.
a = int(input("Enter the Length of first side: "))
b = int(input("Enter the Length of second side: "))
c = int(input("Enter the Length of third side: "))
# condition to check if any of the three lengths is greater than the sum of other two.
if (c >= a+b) or (b >= a+c) or (a >= b+c):
    print("No, Triangle Cannot be formed.")
else:
    print("Yes, Triangle Can Be formed.")
