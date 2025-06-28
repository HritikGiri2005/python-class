----------------------------------# PYTHON-----------------------------------------------------------------------------------------

python: Python is a general purpose high level programming language.

WHY WE USE PYTHON
---------------------------
1. Simple and easy to understand Because it is more about analysis and less about coding
2. Open source and Freeware


PYTHON SUPPORTS WHICH TYPE OF PROGRAMMING FEATURES 

1. OOPS ---> C++
2. POPS ---> C
3. SCRIPTING LANGUAGE --> PEARL
4. MODULAR PROGRAMMING --> MOUDULA3


FLAVOURS OF PYTHON
---------------------

1. STANDARD PYTHON / C-PYTHON
2. JYTHON  / JAVA + PYTHON
3. IRON PYTHON --> .NET
4. ANACONDA PYTHON --> DS,ML,AI



PYTHON VERSIONS:

0.1
1.X
2.X
3.X
3.10


**FUNDAMENTAL OF PYTHON**
--------------------------
1. IDENTIFIER : NAME IN PYTHON IS CALLED IDENTIFIER IT MAY BE VARIABLE NAME , FUNCTION NAME , CLASS NAME..

print()
username = "katrina"

RULES TO IDENTIFY
-----------------
allowed character

DATA TYPE : TYPE OF DATA REPRESENTED IN A VARIABLE IS CALLED A DATA TYPE

### PYTHON BASIC DATA TYPE :
---------------------------

INT : used to represent integer value eg: 1,2,3,4
FLOAT : 
COMPLEX
BOOL
STR


### SEQUENTIAL DATATYPE:
-----------------------------
LIST
TUPLE
SET
DICT
BYTEARRAY
FROZENSET
RANGE
NONE...........

PYTHON IS DYNAMICALLY TYPED PROGRAMMING LANGUAGE
TYPE OF VARIABLE IS DECIDED ON RUN TIME BASED ON PROVIDED VALUE


WE CAN REPRESENT INT VALUES USING 4 WAYS

1. DECIMAL NUMBER SYSTEM(default number system):base10
allowed values 0-9
2. OCTAL NUMBER SYSTEM : base 8
allowed values 0-7 written using 0o before number
3. BINARY NUMBER SYSTEM : base 2
allowed values 0,1 written using 0b before number
4. HEXADECIMAL NUMBER SYSTEM : base 16
allowed values 0-9 and a-f written using 0x before number


### CONVERSIONS

bin():




**-------------------------COMPLEX NUMBER----------------------**
we cannot use another letter than j/J if we use it will throw an error

we cannot do modulus operation on complex datatype

FOR REAL PART ANY NUMBER SYSTEM IS ALLOWED BUT NOT APPLICABLE FOR IMAGINARY PART

**------------------------------------BOOLEAN DATATYPE---------------------------------**

IN BOOL TRUE = 1 AND FALSE = 2


**----------------------------STRING DATATYPE---------------------------------**

TRIPLE QUOTES ARE USED TO PRINT THE STRING AS IT IS WRITTEN


**---------------------------------TYPE CASTING--------------------------------**

int(): convert any type to integer type

print(int('Ten'))  #ValueError: invalid literal for int() with base 10: 'Ten'


float(): convert any type to float type
complex(): to convert any type to complex type
bool():to convert any type to bool      koi bhi number denge toh True ayega agar 0 denge to false ayega


### OPERATORS

###### 1. Arithmetic Operators
+,-,/,*,%,//(floor division)


###### 2. LOGICAL OPERATORS
ANY NUMBER OTHER THAN O IS TRUE
EMPTY STRING MEANS FALSE


----------------------------------------------------------------------------------------
<!-- INPUT OUTPUT STATEMENTS -->

**input():** to take input from user
 it is echo i.e it takes input as well as it returns too
 IT ALWAYS RETURN STRING TYPE OF DATA

**OUTPUT STATEMENT:print()**

# sep =''  ` ---------------by default sep ki value \n rheti hai`

**format()** = used to arrange your string in specific format




**CONTROL FLOW STATEMENT** : TO CONTROL THE FLOW OF EXECUTION CONTROL FLOW STATEMENT WAS MADE

# TYPES OF CONTROL FLOW STATEMENT : 1.CONDITIONAL 2.ITERATIVE AND 3.TRANSFER STATEMENTS

1. CONDITIONAL: IF,IF-ELSE,IF-ELIF-ELSE
2. ITERATIVE: FOR,WHILE
3. TRANSFER: BREAK, RETURN, CONTINUE, PASS, TRY


---------------------------------RANGE----------------------------------

range(start,end,gap)

------------------------------------BREAK & CONTINUE----------------------------------
Break Statement is used to exit the loop when a certain condition is met.It is used to break the loop and exit from it. It can only be used inside a loop.

continue statement is used to skip the value and continue further

# -----------------------------------------FUNCTIONS OF A STRING-------------------------

1. index() : it returns the index of a specific character in the string only the first occurence of that character
2. find() : it is exactly same as index() but find() will return -1 if the character is not present in the string on the other hand index() will give an ValueError
3. count() : It returns the total number of occurances of a character in the string
4. split() : It splits the string into a list of substrings based on specified separator or token
5. join() : It is used for joining token into a string based on the specified separator
6. replace(oldString, newString) : It replaces all occurrences of oldString with newString in the string
7. upper() : It converts all characters in the string to uppercase
8. lower() : It converts all characters in the string to lowercase
9. title() : It converts the first character of each word to uppercase and the rest to lowercase
10. swapcase() : It converts uppercase characters to lowercase and vice versa
11. isalnum() : It checks if all characters in the string are alphanumeric (letters and digits)(A-Z, a-z, 0-9)
12. isalpha() : It checks if all characters in the string are alphabetic (A-Z, a-z)
13. isupper() : It checks if all characters in the string are uppercase
14. islower() : It checks if all characters in the string are lowercase
15. istitle() : It checks if the string is in title case (first character of each word is uppercase)

--------------------------------------------------------------------------------------------------------------------------------------------
# List => if we want to represent a group of individual values as a single entity here duplicate object is allowed insertion order is preserved then we can then we can use LIST

# List is a Mutable Datatype 

# -------------------------------------------------------------------CRUD-operations------------------------------------------------------------------------------------------------

### 1. Accessing element from list
    =>indexNo
    =>slice 

### 2. append(value) => adds data to the end of the list
### 3. insert => insert(indexNo, value) => it will add element to the specified index no of the list
### 4. extend() => it adds all the values of l2 to l1
### 5. pop() => it removes the last element from the list
### 6. remove => used to remove the specified element only
### 7. clear => used to clear/ remove all the elements from the list
### 8. sort() => it sorts the list in ascending order
### 9. count() => it returns the count of the specified element in the list
### 10. index() => it returns the index of the specified element in the list
### 11. reverse() => it reverses the list
### 12. len() => it returns the length of the list
### 13. list Aliasing => give another name to the existing object
### 14. clone() => creating exactly duplicate object of an existing list



#---------------------------------------------------List Comprehension-------------------------------------------

List comprehension offers a short syntax for creating a new list

# characteristics of List
1. duplicate objects are allowed
2. insertion order is preserved
3. heterogeneous objects are allowed
4. indexing and slicing are allowed
5. List is mutable
6. we can represent list object by using [] with comma separator

# ---------------------------------------TUPLE-----------------------------------------------------------

Tuple: tuple is exactly same as list but it is immutable i.e. once created it cannot be changed
tuple is read only version of list

1. duplicate objects are allowed
2. insertion order is preserved
3. heterogeneous objects are allowed
4. indexing and slicing are allowed
5. Tuple is immutable
6. we can represent list object by using [] with comma separator

# ------------------------------------ SET ---------------------------------------------------------

1. duplicate objects are not allowed
2. insertion order is not preserved
3. Represented using {} or set()
4. Heterogeneous data are allowed
5.Indexing and slicing is not allowed
6. by using while loop we cannot print the set as indexing and slicing is not possible

# ----------------------------------Operations on set
1. add() => it adds the specified element to the set
2. update() => it adds multiple elements to the set only adds  iterable objects
3. pop() => it removes random element from set
4. remove() => it removes the specified element from the set
5. clear() => it removes all the elements from the set
6. copy() => it returns a copy of the set
7. sorted() => it sorts the set but first convert to list

# -----------------------------------Mathematical operations on set------------------------

1. union() => it returns a set with all elements from the original sets
2. intersection() => it returns a set with elements common to the original sets
3. difference() => it returns a set with elements in the original set but not in the other set


# --------------------------------------------------DICTIONARY---------------------------------------
1. Values stored in key-value pairs
2. Duplicate keys are not allowed
3. Key must be immutable
4. Key-value pairs are ordered

#how to access value
value = dic_name[key]

# ----------------------------------------------------------------------------------------------

1.add =>  dict_name['key'] = value 
2. delete => del dict_name['key]

# --------------------------------------functions in dict-----------------------------------------

1. get(key) => it returns the value for the given key if it exists in the dictionary
2. get(key,default_value) => returns value of an specified key if the key is not available you will get default_value
3. keys() => returns the list of all keys available in the dictionary
4. values() => returns the list of all values available in the dictionary
5. items() =>  returns list of all key-value present inside dict





















