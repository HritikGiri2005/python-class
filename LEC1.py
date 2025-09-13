# print('''Hello world''')

# #int
# a=10
# print(a)
# print(type(a))

# #float
# b=10.1
# print(a)
# print(type(b))

# #string
# c='Hritik'
# print(c)
# print(type(c))

# #boolean
# d=True
# print(d)
# print(type(d))

# #complex
# e=3+6j
# print(e)
# print(type(e))

# #decimal
# f=0b10
# print(f) 

# #octal
# l=0o12
# print(l)


# #hexadecimal 
# g=0x213
# print(g)


#CONVERSIONS

# print(bin(12))
# print(bin(0o3434))
# print(bin(0xface))

# print(oct(12))
# print(oct(0b1010))
# print(oct(0x1010))

# print(hex(12))
# print(hex(0b1000))
# print(hex(0o1000))

#------------COMPLEX--------------------------

# h= 2+3j
# y= 4+7j
# print(h)

#--------------------------arithmetic operations-----------

# print(h+y)
# print(h-y)
# print(h/y)
# print(h*y)
# print(h**y)
# print(h%y)  #ERROR

#-------------------------REAL AND IMAGINARY PART-----------------------

# a=10+20j

# print(a.real)
# print(a.imag)

#------------------------

# a=0b10+20j  #applicable
# print(a)

# b=10+0b1010j  invalid syntax
# print(b)


#-----------------------------------BOOL DATATYPE-------------------------------


# a= True
# print(a)
# print(type(a))


#-----------------------------------STRING DATATYPE-------------------------------------

# S = '''python
#     is
#     easy to learn'''

# print(S)


#---------------------------------------TYPE CASTING-------------------------------------------

#---------------------------------------INT------------------------------------
# print(int(10.5))
# print(int('10'))
# print(int('Ten'))  #ValueError: invalid literal for int() with base 10: 'Ten'
# print(int(True))
# print(int(False))

# print(int(10+20j)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'


#-----------------------------------------------------FLOAT----------------------------------------


# print(float(10))
# print(float('10'))
# print(float('Ten'))  #ValueError: invalid literal for float() could not convert string to float
# print(float(True))
# print(float(False))
# print(float(10+20j))  #TypeError: float() argument must be a string, a bytes-like object or a real number, not 'complex'


#-----------------------------------------------------COMPLEX----------------------------------


#FORM 1
#complex(x): x is a real part

# print(complex(10))
# print(complex(10.3))
# print(complex(True))
# print(complex("10"))

# #FORM 2
# #complex(x,y): x is a real part and y is an imaginary part

# print(complex(10,20))
# print(complex(10.3,20))
# print(complex(True,20))
# print(complex("10",20))  #TypeError: complex() can't take second arg if first is a 



# #---------------------------------------------BOOL-----------------------------

# print(bool(10))  #true
# print(bool(10.0))  #true
# print(bool(0.1))  #true
# print(bool(0.0))  #fasle
# print(bool(0))  #false

# print(bool(1+2j))  #true
# print(bool(1+20j))  #true
# print(bool(0+2j))  #true
# print(bool(1+0j))  #true
# print(bool(0+0j))  #false

# print(bool('')) #false
# print(bool(' ')) #true
# print(bool('true')) #true

# #----------------------------------STRING-------------------------------

# print(str(10))
# print(str(True))
# print(str(10+20j))
# print(str(10.5))


#--------------------------------------OPERATORS---------------------------------

#------------------------ARITHMETIC OPERATORS-------------------

# a=10
# b=2

# print("a+b = ", a+b)
# print("a-b = ", a-b)
# print("a/b = ", a/b) #always return result in float type
# print("a*b = ", a*b)
# print("a//b = ", a//b) #result change according to both the operands

#for string type if we use + operator then both args must be str type only
# print('java' + 'python')
# print("Java" + 10) #TypeError: can only concatenate str (not "int") to str

#for string type if we use * operator then both args must be int type only
# print('java'*3)
# print((3*2) * 'python')
# print('java'*'python')  #TypeError: can't multiply sequence by non-int of type 'str'


# print(10/0) #ZeroDivisionError: division by zero


#---------------------------------RELATIONAL OPERATOR---------------------------
#>,<,<=,>=
# print(100>500)
# print(100<200)
# print(100>=100)
# print('java'>'python')
# print(ord('j'))
# print(ord('p'))
# print('java'>200) #TypeError: '>' not supported between instances of 'str' and 'int'
# print(True<200)
#nesting of relational operators : if all are True then only result is True otherwise False
# print(10>5>3>6)
# print(10>5>3<6)


#--------------------------------LOGICAL OPERATORS---------------------

#and
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# #or
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# #not
# print(not True)
# print(not False)


#----------------------------NON BOOLEAN TYPE-------------------------

# X AND Y : RETURN X IF X IS FALSE OTHERWISE RETURN Y
# print(100 and 200)
# print(0 and 10)
# print('java' and 'python')
# print('' and ' ')

# # X OR Y : RETURN X IF X IS TRUE OTHERWISE RETURN Y
# print(100 or 200)
# print(0 or 10)
# print('java' or 'python')
# print('' or ' ')


# #EQUALITY OPERATOR(==,!=) APPLICATBLE FOR SAME TYPE AS WELL AS DIFFERENT TYPE

# print(100==200)
# print(100!=200)
# print('java' == 'java')
# print('java' == 'python')
# print('java' != 200)

# #MEMBERSHIP OPERATOR : in , not in
# s= 'python is simple'
# print('python' in s)
# print('python' not in s)

# # #IDENTITY OP : is , is not
# a=10
# b=20
# c=10

# print(a is b)
# print(a is c)
# print(a is not b)

# -------------------------------------2nd saturday-------------------------------
# INPUT OUTPUT STATEMENTS
# rv = int(input("Enter a number"))
# print(rv)
# print(type(rv))

#wap to take eid,ename,esal,emarried_status from user and print it

# eid=int(input("enter the employee id: "))
# ename=str(input("enter your name: "))
# esal=int(input("enter your salary: "))
# emarried_status=str(input("enter your maritial status: "))

# print(eid,ename,esal,emarried_status,sep="-")

#OUTPUT STATEMENT
# print('Hello')
# print('hello'+'world')
# print('hello \t world \n ji')

# a=10
# b=20
# c=20

# print(a,b,b,sep="*")

# name='AAA'
# marks= 98.23
# rollno= 111
# print("name :",name)
# print("Marks :",marks)
# print("rollno :",rollno)

# print(f"hello {name}, roll number {rollno} you got {marks}% congratulations")

# print('hello',end=' ')
# print('how are your',end=' ')
# print('goodmorning')


#format()

# name='AAA'
# marks= 98.23
# rollno= 111

# print("hello, {x} roll no {y} you got {z}% Congratulations".format(x=name,y=rollno,z=marks))







# CONDITIONAL:
# 1) if STATEMENT

# if 10>5:
#     print("hello welcome")

# 2) if-else statement

# if 10>5:
#     print("welcome")

# else:
#     print("cant enter sorry")


#WAP take 2 numbers from user print greatest number
# num1 = int(input("Enter num1= "))
# num2 = int(input("Enter num2= "))

# if num1 > num2:
#     print("number 1 is greater")

# else:
#     print("Number 2 is greater")


#WAP take cp and sp print profit and loss

# cp= int(input("enter cost price="))
# sp= int(input("enter selling price= "))

# if sp>cp:
#     print("there's a profit ")

# else:
#     print("there's a loss")


#ELIF STATEMENT

# a = int(input("enter a number= "))

# if a==0 :
#     print("Zero")

# elif a==1 :
#     print("one")

# elif a==2 :
#     print("two")

# elif a==3 :
#     print("three")

# elif a==4 :
#     print("four")

# elif a==5 :
#     print("five")

# elif a==6 :
#     print("six")

# elif a==7 :
#     print("seven")

# elif a==8 :
#     print("eight")

# elif a==9 :
#     print("nine")

# else:
#     print("ENTER NUM BETWEEN 0-9 ")





# WAP PRINT BUZZ IF NUM IS DIVISIBLE BY 5,PRINT FIZZ IF NUM IS DIVISIBLE BY 3,,PRINT BUZZ-FIZZ IF NUM IS DIVISIBLE BY 5&3, IF NOT BY BOTH PRINT THE NUMBER


# a=int(input("Enter a number"))

# if a%5==0 and a%3==0:
#     print("BUZZ-FIZZ")

# elif a%3==0:
#     print("FIZZ")

# elif a%5==0:
#     print("BUZZ")

# else:
#     print(a)



# for i in range(10):
#     print(i)

# for i in range(2,10):
#     print(i)

# for i in range(2,20,2):
#     print(i)

# n=int(input("enter a number"))
# for i in range(n):
#     print(str(i+1)*(n))

# n = int(input("Enter a number: "))
# for i in range(n):
#     print((str(n-i)+" ")*n)


#ASCII
# n=int(input("Enter a number:"))
# for i in range (n):
#     print((chr(65+i)+" ")*n)


# n=int(input("Enter a number:"))
# for i in range(n):
#     print((chr(65-i-1+n)+" ")*n)



# n= int(input("Enter a number"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i, end =' ')
#     print()  # to create new line after each row


#reverse pattern

# n= int(input("Enter a number"))
# for i in range(1,n):
#     for j in range(i+1):
#         print(n+1-i, end =' ')
#     print()  # to create new line after each row


#star pattern 

# n= int(input("enter a number :"))
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=" ")
#     print()

# NUMBER PATTERNS

# n= int(input("Enter a number :"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i),end=" ")
#     print()


# REVERSE NUMBER PATTERN

# n = int(input("Enter a number :"))
# for i in range(n):
#     for j in range(n-i):
#         print(chr(65+i),end=" ")
#     print()



# n = int(input("Enter a Number : "))
# for i in range (1,n+1):
#     print(" " * (n-i),end="")
#     for j in range (i):
#         print("*",end="")
#     print()


# n = int(input("Enter a Number : "))
# for i in range (1,n+1):
#     print(" " * (n-i),end="")
#     for j in range (i):
#         print(chr(64+i),end="")
#     print()


# ---------------------------------------------WHILE LOOP------------------------------------------------------------

# i=1
# while i<=10:
#     print(i)
#     i+=1

# WAP to take name from user until it enters correct value
# name= "python"
# a = input("Enter the term: ")
# while a!=name:
#     a = input("Incorrect term, please enter again: ")
# print("Correct term entered:",a)


# WAP to take a number and print the table of it
# num = int(input("Enter a number: "))
# i=1
# print("Table of",num,"is:")
# while num>0 and i<=10:
#     print(num * i)
#     i=i+1

# ------------------------------------------------------Break & Continue----------------------------------------------------------------

# for i in range(11):
#     if i==7:
#         break
#     print(i)

# i=0
# while i<10:
#     if i==7:
#         print("Breakin the loop at i =",i)
#         break
#     print(i)
#     i+=1

# for i in range(11):
#     if i==5:
#         continue
#     print(i)

# PROGRAM 1- A person is running.He completes 1 km . We have to ask whether he want to continue. If yes run for more 1km. if no print "OK". If 5km are completed then print "Congrats!".

# init_km = 1
# print("You have ran 1km")
# while init_km<5:
#     quest = input("Do you want to continue ? (yes/no)")
#     if quest =="yes":
#         init_km = init_km + 1
#         print("You have ran ", init_km , "km")
#     if quest == "no":
#         print("OK")
#         break
#     if init_km==5:
#         print("Congrats!")
#         break

# PROGRAM 2- Take speed from user in KM. Convert speed in mile/hr and print both speeds in km and miles.
# speed = float(input("Enter your speed: "))
# miles = speed*0.6213
# print("Your speed in km/hr =",speed,"and your speed in Miles/hr is: ",miles)

# PROGRAM 3 - Take 2 numbers from user and print its summation and multiplication
# num1 = float(input("Enter Number 1 : "))
# num2 = float(input("Enter Number 2 : "))

# sum = num1 + num2
# mult = num1 * num2

# print("sum= ",sum,"Multiplication= ",mult)

# PROGRAM 4 - take a number from user and print its square and cube

# number =  float(input("Enter a number: "))

# square = number ** 2
# cube = number ** 3

# print("Square of number is: ",square)
# print("Cube of number is: ",cube)

#PROGRAM 5 - take temperature input from user and print it in celcius and farenheit.
# temp = float(input("Enter temperature: "))
# farenheit = (temp * 9/5)+32

# print("Temperature in celcius = ",temp , "& in farenheit = ",farenheit)

# PROGRAM 6 - take length & breadth of rectangle and print its area and perimeter

# len = float(input("Enter length of rectangle: "))
# breadth = float(input("Enter breadth of rectangle: "))

# Area = len*breadth
# Perimeter = 2*(len+breadth)

# print(f"Area of rectangle with lenghth = {len} & breadth = {breadth} is {Area} & Perimeter of Rectangle with length = {len} & breadth = {breadth} is {Perimeter}")

#PROGRAM 7 - Take radius of a circle and print its area and circumference
# radius = float(input("Enter a radius: "))
# area = 3.14 * radius**2
# circumference = 2 *3.14*radius

# print(f"area = {area} & circumference = {circumference}")


#------------------------------------ Accessing the string datatype------------------------------------------------------

# Using index number
# s='python'
# print("Accessing the string using index number: ")
# print(s[0]) # accessing the first character of the string
# print(s[1]) # accessing the second character of the string
# print(s[2]) # accessing the third character of the string
# print(s[5])
# print(s[7]) #This will give an IndexError: string out of range
# print(s[-4]) #print 't'

#Using Slicing
# print(s[0:6:1])
# print(s[2:5:2])
# print(s[::])
# print(s[-5:-1:2])
# # print(s[0:6:2]) #This will give an IndexError: string index out


#PROGRAM - take a string as input and print positive and negative index of the string
# str = input("Enter a string: ")
# print(str.__len__())
# print("Positive Index Value: ")
# for i in range(str.__len__()):
#     print(i)
# print("Negative index values:")
# for i in range(str.__len__(),0):
#     print(i)

# # ------------------------------------------------------------------------------------------------------

# # printing characters of a string using a loop
# s='python'
# for c in s:
#     print(c)

# # printing characters of a string using while loop
# print("Using while loop")
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+1

# ----------------------------------------------------------------Functions of a String------------------------------
# 1.index()
# S="Python"
# print(S.index("P")) #0
# print(S.index("y")) #1
# print(S.index("t")) #2
# print(S.index("th")) #it will only print the index number of first character i.e. t
# print(S.index("A")) #it will give error because A is not present in the string
# X = 'Pythonpythonpython'
# print(X.index('y',2)) #it will start searching from index 2 and will return the index of first occurence of y after the index2 
# print(X.index('y',8,15)) #it will start search for y in the range of 8 to 15 and will return the index of first occurance of y in the range 


#2.find()
# a = 'Python'
# print(a.find('P')) #0   
# print(a.find('o')) #4
# print(a.find('A')) #-1

# 3.count()
# a='PythonPythonPython'
# print(a.count('P')) #3
# print(a.count('y')) #3
# print(a.count('A')) #0
# print(a.count('th')) #3

# 4.split()
# s = 'Python is a programming language'
# print(s.split()) #Default separator space

# a='Python*is*a*programming*language'
# print(a.split('*'))

# 5.join()
# l = ['Python','is','a','programming','language']
# s = ' '.join(l) #joining with space
# print(s) #Python is a programming language 

# s = '*'.join(l) #joining with *
# print(s) #Python*is*a*programming*language  


# 6.replace(oldString, newString)
# s= "Python is difficult to learn and difficult to understand"
# print(s.replace('difficult', 'easy'))  # Replaces 'difficult' with 'easy'

# ----------------------------------------------change case of the string----------------------------------------------------------

# 7.upper()
# s = "Python is a programming language"
# print(s.upper())  # PYTHON IS A PROGRAMMING LANGUAGE

# 8.lower()
# s = "PyThOn"
# print(s.lower())  # python

# 9.title()
# s= "python"
# print(s.title())  # Python

# 10.swapcase()
# s = "Python is a Programming Language"
# print(s.swapcase())  # pYTHON IS A pROGRAMMING lANGUAGE

# ------------------------------------------------------------checking case of the string---------------------------------------------

# 11.isalnum()
# s = "Python123"
# print(s.isalnum())  # True
# s = "Python123"
# print(s.isalnum())  # True
# s= "Python@123"
# print(s.isalnum())  # False, because of the '@' character

# 12.isalpha()
# s = "Python"
# print(s.isalpha())  # True
# s = "Python123"
# print(s.isalpha())  # False, because of the '123'

# 13.isupper()
# s = "PYTHON"
# print(s.isupper())  # True
# s = "Python"
# print(s.isupper())  # False

# 14.islower()
# s = "python"
# print(s.islower())

#  15.istitle()
# s = "Python Is A Programming Language"
# print(s.istitle())  # True

# --------------------------------------------------------------------------------------------------------------------
# WAP to take string input and print type of case
# --------------------------------------------------------------------------------------------------------------------

# name = input("Enter a String: ")
# if name.isupper():
#     print("the name is in upper case")
# elif name.islower():
#     print("the name is in lower case")
# elif name.istitle():
#     print("The name is in title case")
# elif name.isalpha():
#     print("The name is in alpha case")
# elif name.isnumeric():
#     print("the name is in numeric case")
# elif name.isalnum():
#     print("The name is in alpha numeric case")

#--------------------------------------------------------------------------------------------------------------------
# WAP that takes an input from A user, splits it into words and print them on the screen
# --------------------------------------------------------------------------------------------------------------------
# Fullname = input("Enter your name: ")
# print(Fullname.split())

# ---------------------------------------------------------------------------------------------------------------------
# WAP that takes input from a user, convert it to upper case and print them on screen
#-----------------------------------------------------------------------------------------------------------------------
# name = input("Enter something: ")
# print(name.upper())

# -----------------------------------------------------------------------------------------------------------------------
# WAP that prompts a user requesting email and then extracts the username
#-------------------------------------------------------------------------------------------------------------------------
# email = input("Enter email: ")
# username = email.split('@')
# print('Username is:',username[0])

#-------------------------------------------------------------------------------------------------
# Expand on the previous code to print "Hello FirstName LastName" FIRSTNAME.LASTNAME@GMAIL.COM
#-------------------------------------------------------------------------------------------------
# email = input("Enter your email: ")
# username = email.split('@')
# print('Hello',username[0])

# ------------------------------------------------------------------------------------------------------
# Write a code that requests the FIRSTNAME ,LASTNAME, AGE and prints : "HELLO "FIRSTNAME" "LASTNAME",
# YOU ARE NOW "AGE", FYI: AGE IS JUST A NUMBER, YOU ARE YOUNGER THEN EVER"

# firstname = str(input("Enter your first name: "))
# lastname = str(input("Enter your last name: "))
# age = int(input("Enter your age: "))
# print(f"Hello {firstname} {lastname} you are now {age}, FYI: Age is just a number, you are younger than ever")

# ------------------------------------------------------------------------------------
# Repeat the previous exercise but print the name and age in a new line
#------------------------------------------------------------------------------------------------
# firstname = input("Enter your first name: ")
# lastname = input("Enter your last name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {firstname} {lastname}\nyou are now {age}, FYI: Age is just a number, you are younger than ever")

# ---------------------------------------------------------------------------------------------
# WAP that takes the user email and counts the number of username characters
#------------------------------------------------------------------------------------------------
# email = input("Enter your email: ")
# username = email.split('@')
# print("characters in username are: ",username[0].__len__())

#List to be continued
# list, tuple, set, frozenSet, dictonary => iterable objects 

# --------------------CreatingList------------------------

# l = [10, 20, 30]
# print(l)
# print(type(l)) 
#OUTPUT => [10, 20, 30]
# <class 'list'> 

#emptyList
# l = []
# print(l)
# print(type(l)) 
# OUTPUT => <class 'list'>
# []

# l = ()
# print(l)
# print(type(l)) 
# OUTPUT =>()
# <class 'tuple'>

# by using val
# l = eval(input('Enter values: '))
# print(l)
# print(type(l))   
# OUTPUT => Enter values: 88-33
# 55
# <class 'int'>

# --------------------CRUD-operations------------------------------------------------------------------------------------------------

### 1. Accessing element from list
    # =>indexNo
    # =>slice

# ---------------------------------------------INDEX NUMBER--------------------------------------------------------------------------
# l = [10, 20,'AA', True, 30 ,10]
# print(l)
# print(type(l))
#indexNo 
# print(l[0]) 
# print(l[1]) 
# print(l[2]) 
# print(l[6]) #IndexError: list index out of range

# -------------------------------------------SLICE OPERATOR---------------------------------------------------------------------------
# print(l[1:5]) #OUTPUT=> [20, 'AA', True, 30]
# print(l[5:1]) #OUTPUT=> [] the first index must be always greater
# print(l[2:]) #OUTPUT=> ['AA', True, 30, 10]
# print(l[::2]) #OUTPUT=> [10, 'AA', 30]
# print(l[-5:-1]) #OUTPUT=> [20, 'AA', True, 30]

### 2. Adding element in list

#--------------------------------------------APPEND-------------------------------------------------------------------------------------
# l = [10, 20, 30]
# print(l)
# print(type(l))
# l.append(77) 
# print(l)

# ------------------------------------------INSERT-------------------------------------------------------------------------------------
# l.insert(2, 88)
# l.insert(-3, 'Apple')
# print(l)
# OUTPUT => [10, 20, 'Apple', 88, 30, 77]

# l.insert(8, 'BBB') #if we specify indexNo which is greater than the maximum indexNo the element will be added to the end of the list
# l.insert(-8, 'CCC') #if we specify indexNo which is greater than the maximum indexNo the element will be added to the start of the list

# -------------------------------------------EXTEND-----------------------------------------------------------------------
# l1 = ['AAA', 'BBB', 'CCC']
# l2 = [10, 20, 30, 40]
# l1.extend(l2)
# print(l1)
# OUTPUT => ['AAA', 'BBB', 'CCC', 10, 20, 30, 40]

#----------------------------------------------POP----------------------------------------------------------------------------

# l = [10, 20, 30, 40]
# print(l)
# print('Removed Element is/are:',  l.pop()) #removes last element
# print(l) 
# #output => Removed Element is/are: 40

# print('Removed Element is/are:', l.pop(2)) #removes element from specified index
# print(l)#output => Removed Element is/are: 30

# print('Removed Element is/are:', l, l.pop(20)) #IndexError: list index out of range
# print(l)
# l= []
# print('Removed Element is/are:', l, l.pop()) #IndexError: list index out of range
# print(l)

#-----------------------------------------REMOVE-------------------------------------------------------------------------------
# l = [10, 20, 30, 40]
# print(l)
# l.remove(20)
# print(l)
# l.remove('AAA')
# print(l) #ValueError: list.remove(x): x not in list

#------------------------------------CLEAR-----------------------------------------------------------
# l = [10, 20, 30, 40]
# l.clear()
# print(l)

#---------------------------------------------Sorting List Elements-----------------------------------------------------
# l = [2,4,3,6,5,1,9,7,8]
# print(l)

# l.sort() #default sorting /ascending order
# print(l)
# #OUTPUT:[1, 2, 3, 4, 5, 6, 7, 8, 9]

# l.sort(reverse=True) #desending order sorting
# print(l)
# #OUTPUT:[9, 8, 7, 6, 5, 4, 3, 2, 1]

# l=['cat', 'apple', 'bat']
# l.sort()
# print(l) #OUTPUT: ['apple', 'bat', 'cat']

# for sorting list elements must be homogeneous 
# l=['cat', 10, 'apple', 20, 'bat']
# l.sort()
# print(l) #TypeError: '<' not supported between instances of 'int' and 'str'

# --------------------Other List functions-------------------------------------------------------------------

# l= [1,2,2,1,3,5,6,4,3,5,7,8]

##1. count()
# print(l.count(1))
# print(l.count(2))
# print(l.count(5))
# print(l.count(9)) #0

##. index()
# print(l.index(3))
# print(l.index(3, 5))
# print(l.index(3, 5, 9))

##3. reverse()
# l.reverse()
# print(l) #OUTPUT => [8, 7, 5, 3, 4, 6, 5, 3, 1, 2, 2, 1]

##4. length:
# print('Total number of values/elements in list:', len(l) ) 

##5. list Aliasing 
# fruits = ['apple', 'mango', 'banana', 'orange']
# print(fruits)

# fruit_list = fruits #aliasing
# print(fruit_list)

# fruit_list[0] = 'Tomato'
# print(fruit_list)#OUTPUT => ['Tomato', 'mango', 'banana', 'orange']
# print(fruits) #OUTPUT => ['Tomato', 'mango', 'banana', 'orange']

# l = [10, 20, 30]
# l2 = l.copy()
# print(l)
# print(l2)
# l[0] = 77 # the change is only happen in l not l2

## the difference between aliasing and cloning is that if a change is made to one list then in cloning the only list which is change is changed in coloning both list changes.
# another difference is that in cloning no new list is created the same list is assigned two names in alising two new list are available

#---------------------------------LIST COMPARISON---------------------------------------------

# l1 = [1,2,3,4,5]
# l2 = [1,2,3,4,5]
# l3 = [1,2,4,5]

# print(l1==l2)
# print(l1==l3)

# l1 = ['apple','banana','cat']
# l2 = ['apple','banana','cat']
# print(l1 == l2)

# l3 = [10,20,30]
# print(l1 == l3)
# print(l1>l3) #TypeError: '>' not supported between instances of 'str' and 'int'

#--------------------------------------------------LIST COMPREHENSION---------------------------------------------------

# l = [1,2,3,4]
# out = []
# for i in l:
#     out.append(i*2)
# print(out)

# out = [i*i for i in range(1,5)]
# print(out)

# l=[10,20,30]
# print(l)
# print(id(l))
# print('After modification')
# l[0] = 777
# print(l)
# print(id(l)) #same id as before

#------------------------------------------Tuples--------------------------------------------------

#creation of tuple
# t =(10,20,30,10,'AAA')
# print(t)
# print(type(t))

#Empty Tuple
# t=()
# print(t)
# print(type(t))

#by using tuple()
# t=tuple()
# print(t)
# print(type(t))

#tuple for single element
# t=10,
# print(t)
# print(type(t))

# t=(10,)
# print(t)
# print(type(t))

#---------------------------------------------Slicing and indexing in tuple----------------------------------------------------
#----------------------------------------------------indexing--------------------------------------------------------------------
# t=(10,20,30)
# print(t[0]) #10
# print(t[1]) #20
# print(t[2]) #30
# print(t[-1]) #30
# print(t[-3]) #10
# print(t[6]) #indexerror

#---------------------------------------------------------slicing--------------------------------------
# t=(10,20,30,40,50)
# print(t[1:3]) #20,30
# print(t[1:]) #20,30,40,50
# print(t[:3]) #10,20,30
# print(t[:]) #10,20,30,40,50

#-----------------------------------------using for and while loops---------------------------------------------
# t=(10,20,30,40,50)

# # for loop
# for i in t:
#     print(i)

# #while loop
# i=0
# while i<len(t):
#     print(t[i])
#     i=i+1




#-----------------------------------------------methods----------------------------------------------------------------
# t=(10,20,30,40,50,10)
# print(t.index(30))
# print(t.count(10))
# # print(len(t))

# t2 = sorted(t)
# print(t)
# print(t2)

#min() and max()

# t=(5,1,4,6,2,3)
# print('Min element in tuple is :', min(t))
# print('Max element in tuple is :', max(t))

#tuple packing

# a=10
# b='kaustubh'
# c=True
# t=a,b,c #packing
# print(t)
# print(type(t))

#tuple unpacking

# t=(10,'kaustubh',True)
# a,b,c=t
# print(a)
# print(b)
# print(c) 


#----------------------------------------Lists questions---------------------------------------------------
#1. print 1st,2nd,last element in the list
# names=["sara","chanel","mike","ryan","holy","alex","rob"]
# print(names[0])
# print(names[1])
# print(names[-1])

#2. print(1) all elements in the list,(2)"chanel""mitch""ryan",(3) First three elements, (4)Last three elements, (5) Skip each other element
 
# names=["sara","chanel","mitch","ryan","holy","alex","rob"]
# print(names)
# print(names[1:4])
# print(names[:3])
# print(names[4:])
# print(names[::2])

#3. print (1)Sally,(2)sara,sally,joe(3)aly(with two different ways)

# my_list = ["Mitch",["sara","sally","joe"],"peter","aly"]
# print(my_list[1][1])
# print(my_list[1])
# print(my_list[3])
# print(my_list[-1])

# 4.print the length of the list and add your name to the list (External research)
# my_list = ["Mitch",["sara","sally","joe"],"peter","aly"]
# print(len(my_list))
# my_list.append("Hritik")
# print(my_list)

# 5. remove peter from the list using two diff methods
# my_list = ["Mitch",["sara","sally","joe"],"peter","aly"]
# # my_list.remove("peter")
# del my_list[-2]
# print(my_list)

#6. Sort elements in a list and reverse all elements to go from maximum to minimum
# my_list = [50,20,30,10,40,15,45]
# my_list.sort()
# print(my_list)
# my_list.reverse()
# print(my_list)

#7. create a new list that contains the last elements in the nested lists
# grocery_list = [['chips','jelly','chocolate'],['sweet potatoes','potatoes'],['peanuts','protein bar']]
# grocery = [grocery_list[0][-1],grocery_list[1][-1],grocery_list[2][-1]]
# print(grocery)

#8. create a list with 5 of your closest friends and sort them alphabetically

# friends = ['Saniya',"Rachit","Advay","Kshitij","Divya"]
# friends.sort()
# print(friends)

# ---------------------------------------------- SET ----------------------------------------------------- 

# s = {5,1,2,4,6,3,2,True}
# print(s) 
#o/p: {1, 2, 3, 4, 5, 6}

#---------------------print data using for loop---------------------------------------------------------
# s = {5,1,2,4,6,3,2,True}
# for i in s:
#     print(i)

# print('total elements in set:' ,len(s))

#we cannnot print using while loop

# ---------------------------------------Exmpty set--------------------------------------------------------
# s = {}
# print(s)
# print(type(s))
#<class 'dict'>

# s = set()
# print(s)
# print(type(s))
#set()
#<class 'set'>

# -----------------------------------Operations on set------------------------------------------------------------
#1. add()
# s = {2,3,4,5,6}
# print(s)
# s.add(100)
#print(s)

#2. update()

# s ={2,3,4,5,6}
# s.update([555,666,777],'Katrina',("Apple","Orange","Banana"),range(5,20,5))
# print(s)

#3. pop()

# s ={20,30,40,50,60}
# s.pop()
# print(s) #o/p: {20, 40, 60, 30}
# print(s.pop()) #returns random element from set

#4. remove()

# s ={20,30,40,50,60}
# s.remove(30)
# print(s) #o/p: {20, 40, 50, 60}
# s.remove(111) #KeyError: 111
# print(s)

#5. clear()

# s ={20,30,40,50,60}
# s.clear()
#print(s)

#6. copy()

# s1 ={20,30,40,50}
# s2 = s1.copy()
# print(s1)
# print(s2)

# {40, 50, 20, 30}
# {40, 50, 20, 30}

#7. sort()

# s= {20,30,40,50}
# s2=sorted(s)
# print(s2)
# [20, 30, 40, 50]

#-------------------------------------------Mathematical Operations on set-------------------------------------------
#1. union()
# s1 = {10,20,30,40}
# s2 = {30,40,50,60}
# print(s1.union(s2))
# print(s1 | s2)

# #2. intersection()
# print(s1.intersection(s2))

# #3. difference()
# print(s1.difference(s2))

# {40, 10, 50, 20, 60, 30}
# {40, 10, 50, 20, 60, 30}
# {40, 30}
# {10, 20}

# WAP to take input from user and print vowels in it

# name = set(input("Enter your name: "))
# vowels ={"a","e","i","o","u"}
# print (name.intersection(vowels))


#--------------------------------------DICTIONARY----------------------------------------
# d={}
# print(d)
# print(type(d))

# --------------------OR------------------

# d=dict()
# print(d)
# print(type(d))

#if we already know the key-value pair in advance
# d={'apple':200,'banana':50,'mango':250}
# print(d)

# d = dict({'apple':200,'banana':50,'mango':250})
# print(d)

# print (d['apple'])
# print(d['Litchi']) #KeyError: 'Litchi'


#Add element in dictionary if the key is not present
# d['Oranges'] = 120
# print(d) # {'apple': 200, 'banana': 50, 'mango': 250, 'Oranges': 120}

#Add element in dict if the key is already present in dict
# d['banana'] = 140
# print(d) # {'apple': 200, 'banana': 140, 'mango': 250}

#----------------------------Delete----------------------------------------------------


# del d['banana']
# print(d)  #{'apple': 200, 'mango': 250}

#WAP: take input from user no_of_student and then add name and marks then print the dict

# number_of_students = int(input("Enter number of students: "))
# student_grade = {}
# for i in range(number_of_students):
#     name = str(input("Enter student name: "))
#     marks = int(input("Enter marks: "))
#     student_grade[name] = marks

# print(student_grade)

# ----------------------------------------------functions in dict---------------------------------------
#1) get(key)

# d={'apple':200,'banana':50,'mango':250}
# print(d.get('apple')) #200
# print(d.get('litchi')) #None

#2) get(key,default_value)

# print(d.get('apple',100))
# print(d.get('litchi',100)) #100

#3) keys()

# for k in d.keys():
#     print(d)

#4) values()

# print(d.values())

#5) items()
# for i in d.items():
#     print(i)


#WAP if name present in dict print marks of that student_name

# number_of_students = int(input("Enter number of students: "))
# student_grade = {}
# for i in range(number_of_students):
#      name = str(input("Enter student name: "))
#      marks = int(input("Enter marks: "))
#      student_grade[name] = marks

# print(student_grade)

# askname = input("Ask for student name: ")
# for n in student_grade:
#      if askname in student_grade:
#           print( "marks = ",student_grade.values())
#      else :
#           print("Student not found")

# --------------------------------------------05-07-2025-----------------------------------------------------------------------
# ----------------------------------------------------Assignment--------------------------------------------------------------

#1. Create a dict with 3 of your fav friends and their respective age and print out the age of second name your choose

# friends = {"Hritik" : 20,
#            "Rachit" : 20,
#            "Sushant" : 21,
#            }
# print(friends.get("Rachit"))

#2. Create a dict with 3 of your fav friends and their respective hourly wage and obtain the avg of their salaries.

# friends = {"Hritik" : 1000,
#            "Rachit" : 200,
#            "Sushant" : 2100,
#            }
# print(sum(friends.values()) / len(friends))

# 3. Update the prev dict with two of your next fav friends and their respective salaries and obtain the avg of their salaries.

# friends = {"Hritik" : 1000,
#            "Rachit" : 200,
#            "Sushant" : 2100,
#            }
# friends["Rohan"] = 1000
# friends["Gohan"] = 2000

# print(sum(friends.values())/len(friends))

# 4. Write a code that multiplies all the elements in the following dictionary
# 
# my_dict = {'data1':500,
#            'data2':-10,
#            'data3':300}

# result =1

# for value in my_dict.values():
#     result = result * value
# print("Multiplication = ",result)




#5. For each of the students list below calculate the avg of marks for the midterm and final exams for each student and put the average in a separate dict along with the student id

# student_details = [
#     {'student_id' : 1, 'subject': 'math', 'midterm' : 60, 'final' :85},
#     {'student_id' : 2, 'subject': 'math', 'midterm' : 800, 'final' :78},
#     {'student_id' : 3, 'subject': 'math', 'midterm' : 90, 'final' :85}
# ]

# avg_marks = {}
# for student in student_details:
#     for key, value in student.items():
#         if key == 'student_id':
#             student_id = value
#         elif key == 'midterm':
#                midterm = value
#         elif key == 'final':
#              final = value
#              avg_marks[student_id] = (midterm + final) / 2
# print(avg_marks)



#6. repeat the prev exercise but add the avg in a new dict line with "average" as a key

# student_details = [
#     {'student_id' : 1, 'subject': 'math', 'midterm' : 60, 'final' :85},
#     {'student_id' : 2, 'subject': 'math', 'midterm' : 800, 'final' :78},
#     {'student_id' : 3, 'subject': 'math', 'midterm' : 90, 'final' :85}
# ]

# avg_marks = {}
# for student in student_details:
#      for key, value in student.items():
#           if key == 'student_id':
#                student_id = value
#           elif key == 'midterm':
#                midterm = value
#           elif key == 'final':
#                final = value
#                avg_marks[student_id] = {'average': (midterm + final) / 2}
# print(avg_marks)


#7. square each element in the following dictionary
# dictionary = {"C1" :[10,20,30],
#               "C2" :[20,30,40]}
# squared = {} 
# for key, value in dictionary.items():
#     squared[key] = [elem**2 for elem in value]
# print(squared)



#8. Create a list of all keys and a list of all the values and the total sum of all values
# my_salary = {"alex":25,"sally":28,"dina":30}
# keys = list(my_salary.keys())
# values = list(my_salary.values())
# total = sum(values)
# print(keys,values,total)

#9 obtain the length of the following dictionary and sort its elements
# my_dict = {"sally": 23, "dina" : 22, "holy": 50,"Joe": 10,"Peter": 44}
# print(len(my_dict))
# print(sorted(my_dict.items()))


#10. Filter out values that are greater than or equal to 30
# my_dictionary = {"Key 1": 20,
#                  "Key 2": 30,
#                  "Key 3": 50}
# for i in my_dictionary.values():
#     if (i>=30):
#         print(i)


# ----------------------------------------------functions in python-----------------------------------------------------------

# def sayHello():
#     print("Hello Welcome to Python Function")

# sayHello()

#------function with parameters :Parameters are the input to the function
# def sayHello(name):
#     print("Hello",name)
# sayHello("Hritik")

#WAP to create a function which take number as a parameter and print square of number , double of number
# def square_double(num):
#     print("Square of number is:",num**2)
#     print("double of number is: ",num*2)

# square_double(4)


#WAP to create a function which take list as a parameter and print double of all numbers present inside list
# def double_list(num):
#     for i in num:
#         print(f"double of {i} is ",i*2)
# double_list([1,2,3,4,5])

#WAP to create a function which take number as a parameter and print table of that number
# def table(num):
#     for i in range(1,11):
#         print(f"{num} x {i} =", num*i)

# table(3)

# -----------------------------------------Types of arguments-----------------------------------
# 1. Position argument

# def register(name,subject,duration,fees):
#     print('name : ',name)
#     print('subject : ',subject)
#     print('duration : ',duration)
#     print('fees : ',fees)

# register("Hritik","Python",'6 months',35000)

#2. Keyword argument

# def register(name,subject,duration,fees):
#     print('name : ',name)
#     print('subject : ',subject)
#     print('duration : ',duration)
#     print('fees : ',fees)

# register(name="Hritik",duration='6 months',subject="Python",fees=35000)

#--------------Mixing of Positional and Keyword arguments-------------------
# def register(name,subject,duration,fees):
#     print('name : ',name)
#     print('subject : ',subject)
#     print('duration : ',duration)
#     print('fees : ',fees)
# register("Hritik",duration='6 months',subject="Python",fees=350) # positional argument first then keyword argument

# 3. Default argument
# def sum(a,b,c=0):
#     print("sum of a,b,c is:",a+b+c)
# sum(10,20)

#-------------------------------Mixing of default and non default arguments-------------------
# def sum(a,b,c=0):
#     print("sum of a,b,c is:",a+b+c)
# sum(10,20) # here c is default argument and a,b is non default
             # non default first then default arguments

#4. Variable argument
# def f1(*a):
#      print (a)
#      print(type(a))

# f1(2,3)
# f1()
# f1(3,4,5,6,6)

# WAP create a function to add any number of args

# def sum(*a):
#     sum=0
#     for i in a:
#         sum+=i
#         return sum
# print(sum(2,3))

# -------------------------------------------Return Keyword----------------------------------

# def f1(name):
#     return name.upper()

# print(f1("python"))

# rv = f1("java")
# print(rv)

# ------------python function can return multiple values----------------

# def f1():
#     a=10
#     b=20
#     c=30
#     return (a+b+c)
# print(f1())

# ------------- default return------------

# def f2():
#     print("Hello")
#     return 

# print(f2())   #returns none value

# WAP monkey problem-------------------

# def monkey_smile(m1,m2):
#     if((m1==m2)==True or False):
#         return True
    
#     else:
#         return False
    
# print(monkey_smile(True,False)) #returns False
# print(monkey_smile(False,False)) #returns True
# print(monkey_smile(True,True))   #returns True
# print(monkey_smile(False,True))  #returns False

# ------------------WAP police problem

# def police(speed,birthday):
#     if(birthday==True):
#         speed=speed-5 
#     if(60 < speed <= 80):
#         return "Fine rs 500"
#     elif(speed<=60):
#         return 'No fine'
#     else:
#         return "fine 1000"
    
# print(police(86,True))

#-----------------------------Lambda function---------------------------------------

# def square(num):
#     return num*num
# print(square(5))

#----with lambda function-----------------
# sq=lambda num: num*num
# print(sq(8))

# -----WAP (num,num2) return biggest num

# biggest = lambda num1,num2: max(num1,num2)
# print(biggest(20,15))

# -------WAP list ke andar ka naam whose length is divisible by 2-----------

# li = ['AA','AAA','AAA','AAAAA','AAAA','AAAAAA','AAAAAAA'] 

# even = lambda li : [i for i in li if len(i)%2==0]
# print(even(li))


#---WAP toupper(name) return name in capital letter--------------
# namee = lambda name : name.upper()
# print(namee("hritik"))

#------------------------------Functions---------------------------
# ----------1)map(func,sequence)

# l = [10,20,30,40]
# def double(list):
#     return list *2
# res = list(map(double,l))
# print(res)

# res = tuple(map(lambda list: list*2,l))
# print(res)

# res = set(map(lambda list: list*2,l))
# print(res)

# -----------2)filter(func,sequence)
# l = [1,2,3,4,5,6,7,8]
# l2 = list(filter(lambda num: num%2==0, l))
# print(l2)


#----------------------WAP where pname is laptop-------------------------------
# product = [
#     {'pid' : 111, 'pname': 'Mobile', 'price': 20000},
#     {'pid' : 111, 'pname': 'Laptop', 'price': 120000},
#     {'pid' : 111, 'pname': 'Mobile', 'price': 60000},
#     {'pid' : 111, 'pname': 'Laptop', 'price': 113000},
# ]

# laptop = list(filter(lambda product: product['pname'] == 'Laptop', product))
# print(laptop)

#------------------------------reduce(func,sequence)-------------------------------

# import functools
# l = [1,2,3,4,5,6,7,8,9,10]
# res = functools.reduce (lambda x,y: x+y, l)
# print(res)

# 1. WAP to take number from user and add that number in list reverse order(reverse() not in use)
# ex: enter number 8
# output: [8,7,6,5,4,3,2,1,0]

# num = int(input("Enter a number: "))
# l = []
# for i in range(num, -1,-1):
#     l.append(i)
# print(l)


# 2. WAP to take name from user and print common character from name 
# ex: enter first name john
# enter second name : Janardhan
# out =['J','n']

# first_name = set(input("Enter first name: "))
# second_name = set(input("Enter second name: "))
# inter = list(first_name.intersection(second_name))
# print(inter)


# 3. WAP to remove consecutive duplicate values from list
# ex: [1,1,2,2,3,4,5,1,4,4,9,6,5,5]
# out = [1,2,3,4,5,1,4,9,6,5]

# l = [1,1,2,2,3,4,5,1,4,4,9,6,5,5]
# l2 = list(filter(lambda i : [i for i in l if l.index(i) == l.index(i+1)]))
# print(l2)






# 4. WAP to create dictionary to add patients record like name,age,weight,bloodgroup and perform following operations
# (no duplicate patients will be allowed)
# (remove patients who are discharged)
# (update patients weight if required)
# (print particular patients record)

#5. WAP to define function which take list as a parameter and square its elements and add inside another list

# def square(l):
#     l2 = []
#     for i in l:
#         l2.append(i*i)
#     print(l2)
# square([2,3,4,5,6,7])


#6. WAP to print vowels from string (use filter())
# st = "Hritik"
# l2 = ['a','e','i','o','u','A','E','I','O','U']  
# vowels =list(filter(lambda x: x in l2, st))
# print(vowels)

#7. WAP to reverse words of given sentence (reverse() not allowed)
# s ='Nuclear is the ultimate power of india'
# h = s.split()

# for i in range(len(h)-1,-1,-1):
#     print(h[i])

# out='india of power ultimate the is nuclear' 








# ---------------------------------------02-08-2025------------------------------------------------------------

# ----------Nested Function----------

# def outer():
#     print('this is outer function')
#     def inner():
#         print('this is inner function')
#     print('outer function is calling inner function')
#     inner() 
# outer()

#function can return inner function 
# def outer():
#     print('this is outer function')
#     def inner():
#         print("This is inner function")
#     print("Outer function is returning inner function")
#     return inner

# rf = outer()
# rf()

#types of variable in a python function

# 1.local variable
# def f1():
#     a=10 #local variable
#     print(a)
# f1()

# ex2:local variable can be accessed only within function

# def f1():
#     a=10
#     print(a)
# f1()

# def f2():
#     print(a) #NameError: name 'a' is not defined

# f1()
# f2()

# 2.Global Variable 
# a=10
# def f1():
#     print(a)

# def f2():
#     print(a)

# f1()
# f2()


# Note: Global variable can be accessed in all functions present inside module (.py)

# global keyword
# -------------------
# 1) To declare global keyword inside function
# ex
# def f1():
#     global a
#     a=10
#     print(a)
# def f2():
#     print(a)

# f1()
# f2()

# 2) to modify global variable value inside function
# ex
# a=10
# def f1():
#     global a
#     a=100
#     print(a)
# def f2():
#     print(a)

# f1()
# f2()

# globals(): to access global variable inside function if global variable and ocal variable have same name

# a=10
# b=20

# def f1():
#     a=100
#     b=200
#     print(globals()['a']+globals()['b'])
#     print(a+b)
# f1()

# -------------------------------------Modules import concept--------------------------

# ex-1
# import modimport

# modimport.f1()
# modimport.f2()
# print(modimport.name)

# #ex-2: module aliasing
# import modimport as md
# md.f1()
# md.f2()
# print(md.name)

# # ex-3: from module import mem1,mem2,mem3
# from modimport import f1, f2, name
# f1()
# f2()
# print(name)

# ex-4
# from modimport import *
# f1()
# f2()
# print(name)

# ex-5: member aliasing
# from modimport import f1 as fun1,f2 as fun2,name
# fun1()
# fun2()
# print(name)

# ex-6:
# from modimport import f1 as fun1, f2 as fun2
# from Modmport2 import f1, f2
# fun1()
# fun2()
# f1()
# f2()

# ex-7
# from ModImport.modimport2 import f1, f2,name

# f1()
# f2()
# print(name)

# import math

# print(math.sqrt(16))  # OUTPUT: 4.0
# print(math.pi)        # OUTPUT: 3.141592653589793
# print(math.factorial(5))  # OUTPUT: 120
# print(math.pow(2, 3))  # OUTPUT: 8.0
# print(math.pow(2,3))
# print(math.fsum([1,2,3,4,5,6,7]))
# print(math.ceil(10.9))
# print(math.floor(10.9))
# print(math.e)


#-------------------------------------------------Random()------------------------------------------------
# import random
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())

#---------------------------random.uniform()-----------------------------------

# import random

# for i in range(5):
#     print(random.uniform(5,9))
#     print(random.randint(2,6))

# names = ['Hritik', 'Rachit', 'Sushant', 'Kshitij', 'Divya']
# print(random.choice(names))  # Randomly selects one name from the list


# Program for generating 4 otps with six digits
# import random

# for i in range(4):
#     for j in range(6):
#         print(random.randint(0,9),end = ' ')
#     print()

#---------------------------------------------File Handling---------------------------------------------------------------

# ex1:
# f=open('myfile.txt','w')
# print('file name : ',f.name)
# print('file mode :',f.mode)
# print('file is readable :',f.readable())
# print('file is writable :',f.writable())
# print('file is closed: ',f.closed)
# f.close()
# print('file is closed: ',f.closed)


# writing data into file 
# -----------------------------------
# ex1: data is in the same row 
# f=open('myfile.txt','w')
# f.write("Apple")
# f.write("Grapes")
# f.write("Banana")

# ex2: data is in the different rows
# f=open('myfile.txt','w')
# f.write("Apple\n")
# f.write("Grapes\n")
# f.write("Banana")

# ex3: write list of lines 
# f=open('myfile.txt','w')
# courses = ['java\n','python\n','react\n']
# f.writelines(courses)
# f.close()
# print('data is written in the file')

# ex4: appending data inside file 
# f=open('myfile.txt','a')
# f.write('devops')
# f.close()
# print('data is written in the file')

#-----------------------------------------------
# reading data from file
# -----------------------------------------------

# ex1: reading all records from file 
# f=open('myfile.txt','r')
# print(f.read())
# f.close()

# ex2: reading nth number of records from file 
# f=open('myfile.txt','r')
# print(f.read(10))  #reads only 10 letters
# f.close()

# #ex3: reading only one line from file
# f=open('myfile.txt',r)
# print(f.readline())  #reads only one line
# f.close()

#ex4: read all lines from file
# f=open('myfile.txt','r')
# print(f.readlines()) #reads all lines
# f.close()  #close the file

#--------------------------------------------file copy paste program-------------------------------

# f1=open('myfile.txt','r')
# f2=open('myfilecopy.txt','w')
# f2.write(f1.read())
# f2.close()
# f1.close()

# -----------------------------------------With Statements ----------------------------------
#Ex:

# with open('myfile.txt','r') as f:
#     print(f.read())
#     print('is file closed ::',f.closed) #returns false
# print('is file closed ::',f.closed) #returns true

# # ---------------------------------------tell()-----------------------------
# # ex 
# with open('myfile.txt','r') as f:
#     print(f.tell()) #returns 0
#     print(f.read(10)) #reads 10 letters
#     print(f.tell()) #returns 10

#-------------------------------------seek()--------------------------------------------
# ex
# with open('myfile.txt','r') as f:
#     print(f.tell()) #returns 0
#     f.seek(10) #sets the pointer to 10th position
#     print(f.tell()) #returns 10


# -------------------------------------OS Module ----------------------------------------------
# import os

# os.rename('myfile.txt','mynewfile.txt') #renamed the file myfile.txt to mynewfile.txt

# file_exist = os.path.exists('fruit.txt')
# print(file_exist) #returns false as file does not exist

# is_file = os.path.isfile('ModImport')
# print(is_file) #returns false as modimport is a folder

# os.remove('myfilecopy.txt')


#------------------------Program-------------------------
# import os

# file_name = input("enter the file name:")
# with open(file_name,'w') as f:
#     f.write('orange\n')
#     f.write('apple\n')
#     f.write('banana\n')
#     f.write('kiwi\n')
#     f.write('papaya\n')

# if(os.path.isfile(file_name) and os.path.exists(file_name)):
#     print('before delete\n')
#     with open(file_name,'r') as f:
#         print(f.read())

#     with open(file_name,'r') as f:
#         lines = f.readlines()
#         del lines[3]

#     with open(file_name, 'w') as f:
#         f.writelines(lines)

#     print("After delete\n")
#     with open(file_name, 'r') as f:
#         print(f.read())


#------------------------------------------------CSV-------------------------------------------
# import csv
# f= open('myfile.csv','w',newline='')
# #create csv writer
# csv_writer = csv.writer(f)
# csv_writer.writerow(['Name','rollno','marks','address'])
# csv_writer.writerow(['Rahul',1,90,'delhi'])
# f.close()


#--------------------------program--------------------------------------
# import csv
# f = open('students.csv', 'w', newline='')
# csv_writer = csv.writer(f)
# csv_writer.writerow(['Name', 'rollno', 'marks', 'address'])
# no_of_students = int(input("enter number of students: "))
# for i in range(no_of_students):
#     print('student ', i + 1)
#     name = input("enter name: ")
#     rollno = input("enter rollno: ")
#     marks = input("enter marks: ")
#     address = input("enter address: ")
#     csv_writer.writerow([name, rollno, marks, address])
# f.close()

# -----------------------------------------Exception Handling---------------------------------
# ex1 :

# print('statement 1')
# try : 
#     print(10/0)
# except ZeroDivisionError:
#     print('zero division error')
# print('statement 3')
# print('statement 4') 

# ex2 :

# print('statement 1')
# try:
#     print(a)
# except NameError:
#     print('Name error')
# print('statement 3')

# ex 3:

# print('statement 1')
# try:
#     l = [1,2]
#     print(l[3])
# except IndexError:
#     print('index error')
# print('statement 3')


# ex 4 :

# print('statement 1')
# try:
#     print(10/0)
#     print('hello') # this will not print
# except ZeroDivisionError:
#     print('Handled zero div error')
# print('3rd state')
# print('4th state')

# 1) print message of the error

# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print(msg)

# 2)

# try:
#     print(10/0)
# except (NameError,IndexError,ZeroDivisionError,ValueError) as msg:
#     print(msg)

# 3)

# try:
#     print(10/0)
# except Exception as msg:
#     print(msg)


# 4)

# try:
#     print(10/0)
# except :
#     print("default except block")

#----------------------username se filename lo and then open and read if not found then handle exception--------------------------

# file_name = input('Enter file name :')

# try: 
#     f= open(file_name,'r')
# except Exception as msg :
#     print(msg)

# ----------------------------------try-except-else------------------------------------------------------

# ex1: else block is not executed
# try:
#     print(10/0)
# except Exception as msg:
#     print(msg)
# else:
#     print('else block is executed')

# ex2: else block is executed
# try:
#     print(10/2)
# except Exception as msg:
#     print(msg)
# else:
#     print('else block is executed')

# ----------------------------------try-except-finally------------------------------------------------------

# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print(msg)

# finally:
#     print('finally block executed')
#     print('closing database')


#------------------------------------User defined exception -------------------------------------------------

# class MinimumAge(Exception):
#     def __init__(self, msg):
#         super().__init__(msg)


# class MaxAge(Exception):
#     def __init__(self,msg):
#         super().__init__(msg)

# age = int(input('Enter your age: '))

# if age>21 and age < 79:
#     print('congrat... you are eligible for marriage')
# elif age >= 80:
#     raise MaxAge('You already crossed the marriage limit ')
# else:
#     raise MinimumAge('sorry you are too small')

#-------------------------------------------program---------------------------------

# class pin(Exception):
#     def __init__(self,msg):
#         super().__init__(msg)

# actual_pin = 2282
# piin = int(input("Enter the pin"))

# if piin == actual_pin:
#     print("congrats you are logged in")
# else :
#     raise pin('sorry cannot login')

#---------------------------------OOPS------------------------------------------------

# ----------------------------class object-----------------------------------------------
class Test:
    " This is test class created for demo purpose"

print(Test.__doc__)

class Person:
    # objects :
    def __init__(self,name,age,city,gender):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender

    # Methods :
    def eat(self):
        print('person can eat veg and nonveg')
    def play(self):
        print('Playing ludo')

    def person_info(self):
        print('Person name :', self.name)
        print('Person age :', self.age)
        print('Person city :', self.city)
        print('Person gender :', self.gender)


# calling objects
p1 = Person('Hritik',20,'Badlapur','Male')
p1.person_info()

print("************************************")

p2 = Person('Rachit',21,'kalyan','Male')
p2.person_info()

# calling methods
p1.eat()
p1.play()

p2.eat()
p2.play()

print("*****************************")






