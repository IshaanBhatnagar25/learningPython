
#------------------------------------------------Basics-----------------------------------------------------------------
'''
print("Hello")

age=18

if age>18:
    print("eligible")
else:
    print("Not eligible")


'''

#------------------------------------------------For-in loop:------------------------------------------------------------------
'''
sub=['ada','dsa','de','mpi']
for s in sub:
    print(s)
    print(len(s))

print("Using range:\n")

for x in range(1,10):
    print(x*2)
'''

#------------------------------------------------While loop:------------------------------------------------------------------
'''
print("Table of 2:\n")
i=2
while(i<=20):
    print(i)
    i+=2

#While loop with else

i=20
while(i>=0):
    print(i)
    i-=10
else:
    print("Out of range")

'''

#-----------------------------------------------Number Finder------------------------------------------------------------------
'''
num=32

for x in range(101):
    if  x is num:
        print("Number found : ",x)
        break
else:
    print("Not found")

lst=[1,4,6,8,10]
for x in range(11):
    if x in lst:
        continue
    else:
        print(x)
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------Operators in Python-------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#Python language supports the following types of operators −

#Arithmetic Operators
#Comparison (Relational) Operators
#Assignment Operators
#Logical Operators
#Bitwise Operators
#Membership Operators
#Identity Operators

#----------------------------------------Precision Handling in Python------------------------------------------------------------------------------------------------------------------

# Most of these functions are in math module

#1. trunc() :- This function is used to eliminate all decimal part of the floating point number and return the integer without the decimal part.
#2. ceil() :- This function is used to print the least integer greater than the given number.
#3. floor() :- This function is used to print the greatest integer smaller than the given integer.

'''
import math
a=3.6578
print("Integral value=",math.trunc(a))
print("The smallest integer greater than number is : ", math.ceil(a))
print("The greatest integer smaller than number is : ", math.floor(a))
'''

#-------------------Setting Precision-------------------------

#1. Using “%” :- “%” operator is used to format as well as set precision in python. This is similar to “printf” statement in C programming.

#2. Using format() :- This is yet another way to format the string for setting precision.

#3. Using round(x,n) :- This function takes 2 arguments, number and the number till which we want decimal part rounded.

'''
a=15.2254
print("%0.2f"%a)
print("{0:.2f}".format(a))
print(round(a,2))
'''

#------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------Functions in Python------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------

# def keyword is used to declare functions:

#1 Basics
'''
def myFun(var1,var2,var3):
    retVal=var1+var2*var3
    return retVal

def fun2():
    print("I'm awesome")

ans=myFun(5,2,9)
print(ans)
fun2()
'''

#2 Default argumenrs
'''
def fun(name="John",age=12,marks=89):
    print(name," ",age," ",marks)

fun("Max",15,97)
fun(age=15)
fun()
'''

#Scope:
'''
a=10

def f():
    print(a)

def fun(a):
    print(a)

def f2():
    a=5
    print(a)
f()
fun(6)
f2()
'''

#Function with flexible number of arguments:
'''
def fun(*args):
    total=0
    for x in args:
        total+=x
    print(total)

fun(2,5,9,8)
fun(1,3)
lst=[5,8,9.5,7.2]
fun(*lst)               #Unpacking of list
'''

#Returning multiple values from function: Using Tuple
'''
def fun():
    str = "Yoo"
    x = 20
    return str, x;  # Return tuple


# Driver code to test above method
str, x = fun()  # Assign returned tuple
print(str)
print(x)
'''

#Returning multiple values from function: Using List
'''
def fun(a,b):
    return [a+b,a*b,a-b,a%b]
print(fun(15,4))
'''

#Returning multiple values from function: Using Dictionary:
'''
def fun():
    d = {}
    d['str'] = "GeeksforGeeks"
    d['x'] = 20
    return d
# Driver code to test above method
d = fun()
print(d)
'''

#Functions can be referred by variables:
'''
def sayHi():
    print("Hi")
hi=sayHi
hi()
'''

#Functions can be passed as arguments to another function:
'''
def sayHi():
    print("Hi")
def sayHello(hiFun):
    print("Hello")
sayHello(sayHi())
'''

#Functions can be defined inside another function
'''
def sayHi():
    def sayHello():
        print("Hello")

    print("Hi")
    sayHello()
sayHi()
'''

#Functions can return references to another function
'''
def sayHi():
    def sayHello():
        print("Hello")
    print("Hi")
    return sayHello
hello=sayHi()
hello()
'''

#------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------DECORATORS---------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------

#Decorators are callable objects which are used to modify functions or classes.

#Callable objects are objects which accepts some arguments and returns some objects.
#Functions and classes are examples of callable objects in Python.

#Function decorators are functions which accepts function references as arguments and adds a wrapper around them
#and returns the function with the wrapper as a new function.

#eg
'''
def decorator_func(some_func):
    # define another wrapper function which modifies some_func
    def wrapper_func():
        print("Wrapper function started")

        some_func()

        print("Wrapper function ended")

    return wrapper_func  # Wrapper function add something to the passed function and decorator returns the wrapper function


def say_hello():
    print("Hello")


say_hello = decorator_func(say_hello)

say_hello()


#Python syntax for decorator:
@decorator_func
def say_hell():
    print 'Hello'

#The above statements is equivalent to:
def say_hello():
    print 'Hello'
say_hello = deocrator_func(say_hello)
'''

#-------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------YEILD OF FUNCTION-----AND-----GENERATOR FUNCTION-----------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------

#The yield statement suspends function’s execution and sends a value back to caller,
# but retains enough state to enable function to resume where it is left off. When resumed,
# the function continues execution immediately after the last yield run.
# This allows its code to produce a series of values over time, rather them computing them at once and sending them back like a list.

#Return sends a specified value back to its caller whereas Yield can produce a sequence of values.
#We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

#eg.
'''
def sq():
    yield 1
    yield 20
    yield 100
ans=list(sq())
print(ans)
'''

#----------------------------------------------------GENERATOR FUNCTION-------------------------------------------------------------------------------------------------------------------

#Fuction that produce Yield

#A generator function is defined like a normal function, but whenever it needs to generate a value,
#it does so with the yield keyword rather than return. If the body of a def contains yield,
#the function automatically becomes a generator function.


# An infinite generator function that prints
# next square number. It starts with 1

'''
def sq():
    i=1
    while(True):
        yield i*i
        i+=1
for n in sq():
    if(n>100):
        break
    print(n)
'''

#------------------------------------------------------------Pass Keyword ----------------------------------------------------------------------------------

'''
def fun():
    pass
fun()

while(True):
    pass
'''

#Empty Function -- pass keyword

#------------------------------------------------------------__Dictionaries ----------------------------------------------------------------------------------

#Stores values in key-value pair form.
'''
def fun():
   print(s)
s="Hello"
fun()

a="7024"
b=int(a,8)
print(b)
'''

'''
a=(5,4,48,5,6,2,4,5,8,2,3,265,256,1,48,4561,7)

if 25 not in a:
    print("absent")

print(len(a))
print(max(a))
print(min(a))
print(a*3)
'''

'''
print("Pyramid:")

def pyramid(n):
    for x in range(0,n):
        for y in range(0,x+1):
            print(" *",end="")
        print("\r")

print("\n")

def revPyramid(n):
    for x in range(0,n):
        for y in range(0,5-x):
            print(" *",end="")
        print("\r")

def oppPyramid(n):
    for x in range(n,0):
        print(" ",end="")
        for y in range():
            print(" *",end="")
        print("\r")

pyramid(5)
print("\n")
revPyramid(5)
print("\n")
oppPyramid(5)

'''

#-------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------Competitive-------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------ASSIGNMENTS---------------------------------------------------------------------------------------

'''
a=b=c=10
print(a,b,c)

a,b,c=10,20,35
print(a,b,c)
'''

#---------------------------------------------------Taking input from user----------------------------------------------------------------------------------------

#Python reads a line only in string format. To take multiple inputs from single line we just need to split the string.
#So, it depends how your input string looks like.
#It needs a delimiter character like comma(“,”), or blank space(“ “) between your inputs in single line and then we will split the input.

'''
#String input
a=input()
print(type(a))

#Int input
b=int(input())
print(type(b))

#Comma Saperated Input - String by-default
p,q=input().split(",")

Better:
x,y = map(int, input().rstrip().split())

print(p,q)
print(type(p))
'''


#---------------------------------------------------N VARIABLES INPUT-----------------------------------------------------------------------------------------------

#Input in int type using List Comprehension:
'''
x,y=[int(x) for x in input().split(",")]
print(x,y)
'''

#---------------------------------------------------LIST INPUT-----------------------------------------------------------------------------------------------

'''
a=list(input().split())
print(a)

#List of variable number of elements:
arr=[int(x) for x in input().split()]   #Multiple Line Input
print(arr)

#List of size n:                <--------------Input from user with defined size
n = int(input())
lst = [0]*n
for i in range(0,n):
    lst[i] = int(input())
'''

#---------------------------------------------------FACTORIAL OF N NUMBERS-----------------------------------------------------------------------------------------------

'''
def fact(num):
    a=1
    while(num>1):
        a=a*num
        num=num-1
    print(a)
    
t=int(input())

while(t>0):
    fact(int(input()))
    t=t-1
'''

#---------------------------------------------------Taking input from user----------------------------------------------------------------------------------------

'''
n=int(input())  #Single line input

sum=0
for x in arr:
    sum+=x

print(sum)
'''

#---------------------------------------------------LIST COMPREHENSION---------------------------------------------------------------------------------------------


'''
List comprehension is an elegant way to define and create list in python. 
We can create lists just like mathematical statements and in one line only. 

A list comprehension generally consist of these parts :
   Output expression, 
   input sequence, 
   a variable representing member of input sequence and
   an optional predicate part. 

For example :

lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1] 

here, x ** 2 is output expression, 
      range (1, 11)  is input sequence, 
      x is variable and   
      if x % 2 == 1 is predicate part.
'''
#--------------------------------------------------- 1 ---------------------------------------------------------------------------------------------

'''
#Square of all odd numbers bw 1 to 10:
lst=[ x**2 for x in range(2,10) if x%2==1]
print(lst)

lst2=[2**x for x in range(1,200)]
print(lst2)

arr=[int(x) for x in input().split()]
sum=0
for x in arr:
    sum+=x
print(sum)

'''

#---------------------------------------------------FACTORIAL OF N NUMBERS-----------------------------------------------------------------------------------------------

'''
num=int(input())
a=[]
for i in range(num):
    a.append(int(input()))
a.sort()
for i in a:
    print(i)
'''



#-------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------DATA STRUCTURES------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------LIST------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------


#Declaration:
#lst=[]

#Hetrogeneous datatype- Can contain data of any type
#Lists are mutable, i.e., they can be altered once declared.
#Lists can also be used for implementing stacks and queues.

'''
l1=['a',34,21,"string"]
print(l1)

lst=[5,7,9,1,10]
for x in lst:
    print(x)
'''

#-----------------------------------------------LIST MEATHODS--------------------------------------------------------------------------------------------

'''
l=[5,'a',23,312,"Abcd"]
print(l)
l.append("myName")      #Add at the end
print(l)
l.pop()                 #Remove from the end
print(l)

#in
if 23 in l:
    print("true")
else:
    print("false")

#not in
if 21 not in l:
    print("true")
else:
    print("false")
print(len(l))

l1=[15,7,8,9,5,1,156,15]
print(l1)
print(min(l1))
print(max(l1))

l2=[15,4,8,2,156]

l3=l2+l1
print(l3)

for x in range(len(l3)):
    print(l3[x],end=' ')

l4=l2*2
print(l4)

#index(ele, beg, end) :- This function returns the index of first occurrence of element after beg and before end.
print(l3.index(1,0,len(l3)))

#count() :- This function counts the number of occurrences of elements in list.
print(l3.count(15))

#sum() :- Find sum of all elements of list
print(sum(l3))

print(min(l3))
print(max(l3))

# del lst[strt:end] : Delete elements end excluded
del l3[2:5]
print(l3)

l3.pop()
l3.pop(1)
print(l3)

l3.insert(1,15)
print(l3)

l3.remove(1)
print(l3)

l3.sort()
print(l3)

l3.reverse()
print(l3)

l3.append(200)
print(l3)
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------TUPLES-------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

#A Tuple is a collection of Python objects separated by commas.
## In someways a tuple is similar to a list in terms of indexing,
## nested objects and repetition but a tuple is immutable unlike lists which are mutable.
## Immutable ie. Cant be changed once created


#Creating:

#tup=()

'''
tup=()
print(tup)

#2 Ways to define:
t1="Ishaan","Bhatnagar"
print(t1)
t2="John","Cena"
print(t2)

t3=("python",)*3
print(t3)
'''

#----------------------------------------LIST INTO TUPLE AND TUPLE MEATHODS------------------------------------------------------------------------------

'''
lst=[23,431,34,4412]
print(tuple(lst))

t1=("Mark",112,14)
t2=("fsmk",213,22,31)

#Concatinition of tuples
print(t1+t2)

t3=(t1+t2)
print(t3)

#Slicing:
print(t3[5:])

#Reverse printing
print(t3[::-1])

print(len(t3))

if (cmp(t1,t3) !=0 ):
    print("NOt Same")
else:
    print("Same")
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------SETS-------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

#A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
#Python’s set class represents the mathematical notion of a set. The major advantage of using a set,
#as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.
# This is based on a data structure known as a hash table.

#Frozen Sets :-
# Frozen sets are immutable objects that only support methods and operators that produce a result without
# affecting the frozen set or sets to which they are applied.

#Operators for Sets

#Sets and frozen sets support the following operators:

#key in s       # containment check

#key not in s   # non-containment check

#s1 == s2       # s1 is equivalent to s2

#s1 != s2       # s1 is not equivalent to s2

#s1 <= s2    # s1is subset of s2 s1 < s2     # s1 is proper subset of s2 s1 >= s2    # s1is superset of s2

#s1 > s2     # s1 is proper superset of s2

#s1 | s2        # the union of s1 and s2

#s1 & s2 # the intersection of s1 and s2

#s1 – s2        # the set of elements in s1 but not s2

#s1 ˆ s2        # the set of elements in precisely one of s1 or s2

#creating :
#s=set()

'''
s=set()
s.add("5")
s.add("mike")
s1=set(['3',"jhon","max",'12',"5"])

print(s)
print(s1)

#Set Meathods:

#union:
s2=s1.union(s)
# OR : s2=s1 | s
print(s2)

#intersection:
print(s1.intersection(s))
# OR : s2=s1 & s

#Set Difference
print(s1-s)
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------ARRAY-------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

#Array can be handled in python by module named “array“.
## They can be useful when we have to manipulate only a specific data type values.

#Operations on Array :

# 1. array(data type, value list) :- This function is used to create an array with data type and value list specified in its arguments.

#2. append() :- This function is used to add the value mentioned in its arguments at the end of the array.

#3. insert(i,x) :- This function is used to add the value at the position specified in its argument.

#4. pop() :- This function removes the element at the position mentioned in its argument, and returns it.

#5. remove() :- This function is used to remove the first occurrence of the value mentioned in its argument

#6. index() :- This function returns the index of the first occurrence of value mentioned in arguments.

#7. reverse() :- This function reverses the array.

#Extra:

#1. typecode :- This function returns the data type by which array is initialised.

#2. itemsize :- This function returns size in bytes of a single array element.

#3. buffer_info() :- Returns a tuple representing the address in which array is stored and number of elements in it.

#4. count() :- This function counts the number of occurrences of argument mentioned in array.

#5. extend(arr) :- This function appends a whole array mentioned in its arguments to the specified array.

#6. fromlist(list) :- This function is used to append a list mentioned in its argument to end of array.

#7. tolist() :- This function is used to transform an array into a list.


#Data Types:
# i-int
# f-float
# d-double
# q-signed long long

'''
import array

a1=array.array("i",[15,24,256,224,44])

for i in range(5):
    print(a1[i])
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------DICTIONARY-------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

#In python, dictionary is similar to hash or maps in other languages.
#It consists of key value pairs. The value can be accessed by unique key in the dictionary.

# Create a new dictionary
#d = dict() # or d = {}
'''
d={}
d['1']="A"
d['2']="B"

print(d)
print(d.keys())
print(d.values())

#Iterating over the dictionary:
#1
for i in d:
    print(i,":",d[i])
print()
#2
for index,value in enumerate(d):
    print(index,value,d[value])

#check If the key exists:
print("2" in d)

'''

#Dictionary Meathods:

#1. str(dic) :- This method is used to return the string, denoting all the dictionary keys with their values.

#2. items() :- This method is used to return the list with all dictionary keys with values.

#3. len() :- It returns the count of key entities of the dictionary elements.

#4. type() :- This function returns the data type of the argument.

#5. copy() :- This function creates the shallow copy of the dictionary into other dictionary.

#6. clear() :- This function is used to clear the dictionary contents.

#1. fromkeys(seq,value) :- This method is used to declare a new dictionary from the sequence mentioned in its arguments. This function can also initialize the declared dictionary with “value” argument.

#2. update(dic) :- This function is used to update the dictionary to add other dictionary keys.

#3. has_key() :- This function returns true if specified key is present in the dictionary, else returns false.

#4. get(key, def_val) :- This function return the key value associated with the key mentioned in arguments.
                       # If key is not present, the default value is returned.

#5. setdefault(key, def_value) :- This function also searches for a key and displays its value like get() but,
                                # it creates new key with def_value if key is not present.

'''
d1={"Name":"Jhon","Age":20}
d2={"Id":101}
print(d1)
d1.update(d2)
print(d1)
print(str(d1))
print()

#Handling Missing Keys:

#1. get(key,def_val):
print(d1.get("Id","Not Present"))
print(d1.get("EId","Not Present"))
print()

#2. setdefault(key, def_value)
print(d1.setdefault("Id","Not Present"))
print(d1.setdefault("EId","100"))
print(d1)

print()
print(d1.get("EId","Not Present"))
'''

#-----------------------------------------FREQUENCY OF ALPHABETS IN STRING--------------------------------------------------------------------------------------------------------------

#Memset Equivalant:
#for i in range(257):
#    d[i]=0

#Converting Char to ASCII int:
# ord(character)

#Converting int to ASCII char value:
# chr(character)

'''
d={}
for i in range(257):
    d[i]=0
name=str(input())
for i in range(len(name)):
    d[ord(name[i])]+=1
#Same as: d[ord(name[i])-ord('a')]+=1   Then add char(i+97) -> Use if dictionary size is 26 
for i in d:
    if d[i]!=0:
        print(chr(i),':',d[i])
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------STRINGS-------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

#1. Strings are Immutable : Once a string is defined, it cannot be changed.
#2. Three ways to create strings:
#Strings in python can be created using single quotes or double quotes or a triple quotes .

#The single quotes and double quotes works same for the string creation.
#Now talking about triple quotes, these are used when we have to write a string in multiple lines and printing as it is without
# using any escape sequence.

#we can access each and every element of string through their index number and the indexing starts from 0.
# Python does index out of bound checking.

#So, we can obtain the required character using syntax :
#                                                        string_name[index_position]:

#The positive index_position denotes the element from the starting(0) and the negative index shows the index from the end(-1).

'''
name="John"
print(name)
lname="Cena"
print(name+" "+lname)
print(name[3])  #3 char from beg
print(name[-3]) #3 char from end
'''

#-----------------------------------REMOVING SPACE FROM STRING------------------------------------------------

'''
def remSpace(s):
    s=s.replace(' ','')
    return s
s=str(input())
print(remSpace(s))
'''

#------------------------------------------SLICING OF STRING--------------------------------

#Slicing:

#To extract substring from the whole string then then we use the syntax like

#               string_name[beginning: end : step]
# beginning represents the starting index of string
# end denotes the end index of string which is not inclusive
# steps denotes the distance between the two words.

'''
str="mygeeksgfggfg"
print(str[2:10:2])      #Starting from index 2(included) to 10 index(excluded) print skipping to 2nd char each time
print(str[2:10])
'''

#Multiline String:

#str='''This is a multi
#line string.
#Hello!!
#'''
#print(str)

#----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------STRING MEATHODS----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

'''
1. find(“string”, beg, end) :-
This function is used to find the position of the substring within a string.
It takes 3 arguments, substring , starting index( by default 0) and ending index( by default string length).
It returns “-1 ” if string is not found in given range.
It returns first occurrence of string if found.

2. rfind(“string”, beg, end) :- 
This function has the similar working as find(), but it returns the position of the last occurrence of string.

3. startswith(“string”, beg, end) :- 
The purpose of this function is to return true if the function begins with mentioned string(prefix) else return false.

4. endswith(“string”, beg, end) :-
The purpose of this function is to return true if the function ends with mentioned string(suffix) else return false.

5. islower(“string”) :- 
This function returns true if all the letters in the string are lower cased, otherwise false.

6. isupper(“string”) :- 
This function returns true if all the letters in the string are upper cased, otherwise false.

7. lower() :- 
This function returns the new string with all the letters converted into its lower case.

8. upper() :- 
This function returns the new string with all the letters converted into its upper case.

9. swapcase() :- 
This function is used to swap the cases of string i.e upper case is converted to lower case and vice versa.

10. title() :- 
This function converts the string to its title case i.e the first letter of every word of string is upper cased and else all are lower cased.
'''

#Demo:

'''
str = "Geeksforgeeks is for geeks"
str1 = "geek"

# using find() to find first occurrence of str2
# returns 8
print("The first occurrence of str2 is at : ", end="")
print(str.find(str1, 4))

# using rfind() to find last occurrence of str2
# returns 21
print("The last occurrence of str2 is at : ", end="")
print(str.rfind(str1, 4))

# using startswith() to find if str starts with str1
if str.startswith(str1):
    print("str begins with str1")
else:
    print("str does not begin with str1")

# using endswith() to find if str ends with str1
if str.endswith(str1):
    print("str ends with str1")
else:
    print("str does not end with str1")

# checking if all characters in str are upper cased
if str.isupper():
    print("All characters in str are upper cased")
else:
    print("All characters in str are not upper cased")

# checking if all characters in str1 are lower cased
if str1.islower():
    print("All characters in str1 are lower cased")
else:
    print("All characters in str1 are not lower cased")

# Coverting string into its lower case
str1 = str.lower()
print(" The lower case converted string is : " + str1)

# Coverting string into its upper case
str2 = str.upper()
print(" The upper case converted string is : " + str2)

# Coverting string into its swapped case
str3 = str.swapcase()
print(" The swap case converted string is : " + str3)

# Coverting string into its title case
str4 = str1.title()
print(" The title case converted string is : " + str4)
'''

#---------------------------------------STRING MEATHODS CONTINUE:

'''
1. len() :-
 This function returns the length of the string.

2. count(“string”, beg, end) :- 
This function counts the occurrence of mentioned substring in whole string. 
This function takes 3 arguments, substring, beginning position( by default 0) and end position(by default string length).

3. center() :- 
This function is used to surround the string with a character repeated both sides of string multiple times.
 By default the character is a space. Takes 2 arguments, length of string and the character.

4. ljust() :- 
This function returns the original string shifted to left that has a character at its right. 
It left adjusts the string. By default the character is space. It also takes two arguments, length of string and the character.

5. rjust() :- 
This function returns the original string shifted to right that has a character at its left. 
It right adjusts the string. By default the character is space. It also takes two arguments, length of string and the character.

eg.
print ( str.center(20,'-'))
print ("The string after ljust is : ",end="")
print ( str.ljust(20,'-'))
print ("The string after rjust is : ",end="")
print ( str.rjust(20,'-'))

The string after centering with '-' is : ---geeksforgeeks----
The string after ljust is : geeksforgeeks-------
The string after rjust is : -------geeksforgeeks

6. isalpha() :- 
This function returns true when all the characters in the string are alphabets else returns false.

7. isalnum() :- 
This function returns true when all the characters in the string are combination of numbers and/or alphabets else returns false.

8. isspace() :- 
This function returns true when all the characters in the string are spaces else returns false.

9. join() :- 
This function is used to join a sequence of strings mentioned in its arguments with the string.
'''

'''
1. strip() :- 
This method is used to delete all the leading and trailing characters mentioned in its argument.

2. lstrip() :- 
This method is used to delete all the leading characters mentioned in its argument.

3. rstrip() :- 
This method is used to delete all the trailing characters mentioned in its argument.

# Python code to demonstrate working of 
# strip(), lstrip() and rstrip()
str = "---geeksforgeeks---"
 
# using strip() to delete all '-'
print ( " String after stripping all '-' is : ", end="")
print ( str.strip('-') )
 
# using lstrip() to delete all trailing '-'
print ( " String after stripping all leading '-' is : ", end="")
print ( str.lstrip('-') )
 
# using rstrip() to delete all leading '-'
print ( " String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') )

4. min(“string”) :- This function returns the minimum value alphabet from string.

5. max(“string”) :- This function returns the maximum value alphabet from string.

# Python code to demonstrate working of 
# min() and max()
str = "geeksforgeeks"
 
# using min() to print the smallest character
# prints 'e'
print ("The minimum value character is : " + min(str));
 
# using max() to print the largest character
# prints 's'
print ("The maximum value character is : " + max(str));


6. maketrans() :- It is used to map the contents of string 1 with string 2 with respective indices to be translated later using translate().

7. translate() :- This is used to swap the string elements mapped with the help of maketrans().

# Python code to demonstrate working of 
# maketrans() and translate()
from string import maketrans # for maketrans()
 
str = "geeksforgeeks"
 
str1 = "gfo"
str2 = "abc"
 
# using maktrans() to map elements of str2 with str1
mapped = maketrans( str1, str2 );
 
# using translate() to translate using the mapping
print "The string after translation using mapped elements is : "
print  str.translate(mapped) ;

8.replace() :- This function is used to replace the substring with a new substring in the string. This function has 3 arguments. The string to replace, new string which would replace and max value denoting the limit to replace action ( by default unlimited ).

# Python code to demonstrate working of 
# replace()
 
str = "nerdsfornerds is for nerds"
 
str1 = "nerds"
str2 = "geeks"
 
# using replace() to replace str2 with str1 in str
# only changes 2 occurrences 
print ("The string after replacing strings is : ", end="")
print (str.replace( str1, str2, 2)) 

9. expandtabs() :- It is used to replace all tab characters(“\t”) with whitespace or simply spaces using the given tab size, which is optional to supply.
Syntax: string.tabsize(tabsize)
Parameters: Specifying the number of characters to be replaced for one tab character. By default, the function takes tab size as 8.
Return Value: A string in which all the tab characters are replaced with spaces.

# Python code to illustrate expandtabs()
string = 'GEEKS\tFOR\tGEEKS'
 
# No parameters, by default size is 8
print (string.expandtabs())
 
# tab size taken as 2
print(string.expandtabs(2))
 
# tab size taken as 5
print(string.expandtabs(5))

'''



#-------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------LAMBDA FUNCTIONS-------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------MAP, REDUCE , FILTER AND LIST COMPREHENSION-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------


'''
The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. 
These functions are throw-away functions, i.e. they are just needed where they have been created.
 Lambda functions are mainly used in combination with the functions filter(), map() and reduce(). 
 The lambda feature was added to Python due to the demand from Lisp programmers. 

The general syntax of a lambda function is quite simple:
lambda argument_list: expression 

lambda operator can have any number of arguments, but it can have only one expression. 
It cannot contain any statements and it returns a function object which can be assigned to any variable.
'''

'''
#Normal Function:

def add(x,y):
    return (x+y)
print(add(4,5.66))

#Lambda Function:

add1=lambda x,y:x+y
print(add1(12.32,32))

cube=lambda x:x**3
print(cube(int(input())))
'''

#----------------------------------------------------MAP-------------------------------------------------------------------------------------------------------

#To perform same function on all the elements of the list

# MAP(function, iterable) will call the function defined for all the elements of the iterables and returns an iterable containing the result of function performed.

#map functions expects a function object and any number of iterables like list, dictionary, etc.
#It executes the function_object for each element in the sequence and returns a list of the elements modified by the function object.

#Syntax:
#map(function_object, iterable1, iterable2,...)

#Program to find square of every number in the list:

#Without lambda:



'''
def sq(x):
    return x**2
a=[5,7,8,9,1,24]
print(list(map(sq,a)))

#Using Lambda:
print(list(map(lambda x:x**2,a)))

#Program to find Cube of numbers entered as input:
print(list(map(lambda x:x**3,[int(x) for x in input().split()])))

#Iterating over dictionary using lambda and map:

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
#Displaying values of key "Name":
print(list(map(lambda x:x['name'],dict_a)))

#Adding the corresponding elements of the lists:

#Here l1 will be passed in x and l2 in y:

l1=[5,7,9,25]
l2=[8,6,7,31]
lans=list(map(lambda x,y:x+y,l1,l2))
print(lans)
l3=[7,7,4,4]
'''

#----------------------------------------------------FILTER-------------------------------------------------------------------------------------------------------

#To get some values out of list

# Filter(bool_function,iterable) will call the bool_function for all the items in the iterable
# and return an iterable containing only the items for which the result is true.

#filter function expects two arguments, function_object and an iterable.
#function_object returns a boolean value. function_object is called for each element of the iterable and filter returns only those element for which the function_object returns true.

#Like map function, filter function also returns a list of element.
#Unlike map function filter function can only have one iterable as input.

'''
a=[5,8,9,6,2,45,21,557,20,21,40,22,320,2452,15]
ans=list(filter(lambda x:x%2==0,a))
print(ans)

#Filtering Dictionary based on key

d=[{"Id":221,"Name":"John"},{"Id":220,"Name":"Mike"},{"Id":225,"Name":"Jim"},{"Id":224,"Name":"Mike"}]
ans1=list(filter(lambda x:x["Name"]=="Mike",d))
print(ans1)
'''

#----------------------------------------------------REDUCE----PRESENT IN functools PACKAGE---------------------------------------------------------------------------------------------------

#To perform a list-wide operation. eg. Sum/Product of all elements of list

# reduce(function,iterable) will call the function for each sequential pair of values in the iterable and store the
# result in the iterable thus reducing it.
#It will return a single value result.

#eg. Reduce on a list of int with sum() as function: (((((5+8)+10)+20)+50)+100)

'''
from functools import reduce

l=[15,515,21,15,11,48]
sum=reduce((lambda x,y:x+y),l)
print(sum)
'''

#---------------------------------------------------LIST COMPREHENSION---------------------------------------------------------------------------------------------

'''
List comprehensions are used for creating new list from another iterables.

As list comprehension returns list, they consists of brackets containing the expression which needs to be executed for 
each element along with the for loop to iterate over each element.

new_list = [expression for_loop_one_or_more condtions] 

A list comprehension generally consist of these parts :
   Output expression, 
   input sequence, 
   a variable representing member of input sequence and
   an optional predicate part. 

For example :

lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1] 

        expression for-loop    range        condition

here, x ** 2 is output expression, 
      range (1, 11)  is input sequence, 
      x is variable and   
      if x % 2 == 1 is predicate part.
'''

'''
#Square of all odd numbers bw 1 to 10:
lst=[ x**2 for x in range(2,10) if x%2==1]
print(lst)

#2^x for all num in range 1-20
#2^x for all num in range 1-20
lst2=[2**x for x in range(1,20)]
print(lst2)

#Taking input using list-comprehension and returning sum of array
from functools import reduce
arr=[int(x) for x in input().split()]
print(reduce((lambda x,y:x+y),arr))


#Operation on list:
l=[15,7,8,91,202]
print([x**2 for x in l])

#Comman numbers in 2 lists:

l1=[2,5,8,7,4,1,3,6,9]
l2=[7,5,30,11,29]

#Using loops:
ans1=[]
for a in l1:
    for b in l2:
        if(a==b):
            ans1.append(a)
print(ans1)

#Using list Comprehension:
print([a for a in l1 for b in l2 if(a==b)])

#Iterating over string:
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [str.lower() for str in list_a]
print(small_list_a)

#List Comprehension to create list of lists:

list1=[1,2,4,5,6,7,9]
dblLst=[[a**2,a**3] for a in list1]
print(dblLst)
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------UNDERSCORE IN PYTHON '_'--------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#There are 5 cases for using the underscore in Python.

# 1. For storing the value of last expression in interpreter.

'''
In REPL:
10
>>>10
_
>>>10
_*5
>>>50
'''

#2. Ignoring the values:
#The underscore is also used for ignoring the specific values.
#If you don’t need the specific values or the values are not used, just assign the values to underscore.

'''
#Ignoring Single value:
x,_,y=5,15,983
print(x,y)

#Ignoring multiple values:
x,*_,y=5,3,5,5,54,2313,154,75
print(x,y)

#Ignoring index:

for _ in range(2):
    print('A')

# Ignore a value of specific location
a=[2,564,5,54,434]
for _, val in a:
    print("Hello")
'''

# 3. To give special meanings and functions to name of vartiables or functions.




#-------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------COMPETITIVE-------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------Even Odd Check--------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

#num & 1  -> If 0-Even if 1->Odd
# eg. 13->1101 & 0001 ->0001
# eg. 12->1100 & 0001 ->0000

'''
for i in range(int(input())):
    n=int(input())
    if n & 1 == 1:
        print("Odd")
    else:
        print("Even")
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------Prime Number Check:-------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------OPTIMIZED SCHOOL MEATHOD---------------------------------------------------------------------------------------------------

'''
import time,math

def isPrime(n):
    if(n<=1):
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n % 3 == 0:
        return False
    a=5
    while a < math.sqrt(n):
        if n%a==0 or n%(a+2)==0:
            return False
        a+=6
    return True

t0=time.time()
c=0
for i in range(1,1000):
    if isPrime(i):
        print(i,end=" ")
        c += 1
t1=time.time()
print(c)
print("Time:",t1-t0)
'''

#-----------------------------------------------------FERMAT MEATHOD---------------------------------------------------------------------------------------------------

# If n is Prime, then:
#   (a^(n-1))%n=1 where 1<=a<n

#eg. n=7,  n-1=6
# a=6 then 6^6%7=1->True
# a=5 then 5^6%7=1 ->True

# If a given number is prime, then this method always returns true.
# If given number is composite (or non-prime), then it may return true or false,
# but the probability of producing incorrect result for composite is low and can be reduced by doing more iterations.

'''
import random,time
def myPow(a,n):
    a=a%n
    return pow(a,(n-1))%n

def isPrime(n,k):
    if n<=1 or n==4:
        return False
    if n<=3:
        return True
    for i in range(k):
        a=random.randrange(2,n-2)
        if(myPow(a,n)!=1):
            return False
    return True

#t=int(input())
#while t>0:
#    n=int(input())
#    if isPrime(n,5):
#        print(True)
#    else:
#        print(False)
t0=time.time()
c=0
for i in range(1,1000):
    if isPrime(i,1000):
        print(i,end=" ")
        c += 1
t1=time.time()
print(c)
print("Time:",t1-t0)
'''




#---------------------------------------------------1. Power of 2 or not---------------------------------------------------------------------------------------------------------
'''
import math
t=int(input())
while(t>0):
    n=int(input())
    if(n<=0):
        print("NO")
    while(n>1):
        if(n%2!=0):
            print("NO")
            break
        n/=2
    if(n==1):
        print("YES")
    t-=1
'''

#2: x & x-1 == 0 if x if a power of 2
# eg. 8:  1000 & 0111 = 0000  (8&7)
'''
import math
t=int(input())
while(t>0):
    x=int(input())
    if( (x&(x-1)==0) and x!=0):
        print("YES")
    else:
        print("NO")
    t-=1
'''

#---------------------------------------------------2. Larger of sum of 2 lists: ---------------------------------------------------------------------------------------------------------

'''
from functools import reduce
t=int(input())
while(t>0):
    a,b=[int(x) for x in input().split(" ")]
    c1 = list(map(int,input().split(" ")))
    c2 = list(map(int, input().split(" ")))
    #if(reduce((lambda x,y:x+y),c1)>reduce((lambda x, y: x + y), c2)):
    if(sum(c1)>sum(c2)):
        print("C1")
    else:
        print("C2")
    t-=1
'''

#---------------------------------------------------3. Number of occourance of "gfg" in string---------------------------------------------------------------------------------------------------------

'''
t=int(input())
for i in range(t):
    str=input()
    n=len(str)
    if(n>3):
        count=0
        for j in range(n-2):    #n-2 is excluded here in loop
            if(str[j]=='g' and str[j+1]=='f' and str[j+2]=='g'):
                count+=1
        if(count!=0):
            print(count)
        else:
            print(-1)
    else:
        if(str=='gfg'):
            print(1)
        else:
            print(-1)
'''

#---------------------------------------------------5. Length of a*b result---------------------------------------------------------------------------------------------------------

'''
t=int(input())
while(t>0):
    a,b=[int(x) for x in input().split(" ")]
    print(len(str(abs(a*b))))
    t-=1
'''

#---------------------------------------------------5. Boundry Elements of array---------------------------------------------------------------------------------------------------------

'''
t=int(input())
while(t>0):
    n=int(input())
    arr=[int(x) for x in input().split()]
    print(arr)
    t-=1
'''
'''
m,n=[int(x) for x in input().split(" ")]
l=[[]]*m
for x in range(m):
    l[x]=[int(x) for x in input().split(" ")]
print(l)
'''

# code
'''
for t in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    for i in range(len(l)):
        row = i // n
        col = i % n
        res = []
        if (row == 0 or col == 0 or row == n - 1 or col == n - 1):
            res.append(str(l[i]))
    print(' '.join(res))
'''

#---------------------------------------------------6. Nearest Prime---------------------------------------------------------------------------------------------------------





#---------------------------------------------------6. Insertion Sort---------------------------------------------------------------------------------------------------------
'''
def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])
'''

#---------------------------------------------------6. Binary Insertion Sort---------------------------------------------------------------------------------------------------------
'''
def bSearch(arr,key,min,max):
    if min==max:
        if arr[min]>key:
            return min
        else:
            return min+1
    if min>max:
        return min
    mid=(min+max)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return bSearch(arr,key,min,mid-1)
    else:
        return bSearch(arr,key,mid+1,max)
def biSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        loc = bSearch(arr,key,0,i-1)
        #Array Concatination-------------------------------GOOD POINT
        arr=arr[:loc]+[key]+arr[loc:i]+arr[i+1:]
    return arr

print("Sorted array:")
print(biSort([37, 23, 0, 17, 12, 72, 31,46, 100, 88, 54]))
'''

#--------------------------------------------------INDEX OF ITEM IN ROTATED SORTED ARRAY------------------------------------------------------------------------------

'''
def find(arr,l,u,key):
    if l>u:
        return -1
    mid=(l+u)//2
    if key==arr[mid]:
        return mid
    if arr[l]<=arr[mid]:
        if key>=arr[l] and key<=arr[mid]:
            return find(arr,l,mid-1,key)
        return find(arr,mid+1,u,key)
    if key>=arr[mid] and key<=arr[u]:
        return find(arr,mid+1,u,key)
    return find(arr,l,mid-1,key)

arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 9
res=find(arr,0,len(arr)-1,key)
if res != -1:
    print(res)
else:
    print ("Key not found")
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------HEAPQ MODULE-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Heap data structure is mainly used to represent a priority queue. In Python, it is available using “heapq” module. 
The property of this data structure in python is that each time the smallest of heap element is popped(min heap).
 Whenever elements are pushed or popped, heap structure in maintained. The heap[0] element also returns the smallest element each time.

Operations on heap :

1. heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.

2. heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap. The order is adjusted, so as heap structure is maintained.

3. heappop(heap) :- This function is used to remove and return the smallest element from heap. The order is adjusted, so as heap structure is maintained.

4. heappushpop(heap, ele) :- This function combines the functioning of both push and pop operations in one statement, increasing efficiency. Heap order is maintained after this operation.

5. heapreplace(heap, ele) :- This function also inserts and pops element in one statement, but it is different from above function. 
In this, element is first popped, then element is pushed.i.e, the value larger than the pushed value can be returned.

6. nlargest(k, iterable, key = fun) :- This function is used to return the k largest elements from the iterable specified and satisfying the key if mentioned.

7. nsmallest(k, iterable, key = fun) :- This function is used to return the k smallest elements from the iterable specified and satisfying the key if mentioned.

'''

'''
import heapq

h=[10,20,1,532,132,12]
heapq.heapify(h)
print(h)
heapq.heappush(h,-2)
print(h)
print(heapq.heappop(h))
print(h)

#Largest
l=heapq.nlargest(1,h)[0]        #  <--------Taking 1st element of this list
print(l)

#3rd Largest
_,_,a=heapq.nlargest(3,h)
print(a)

#OR
b=heapq.nlargest(len(h)-1,h)[2]     #<------------ Taking 3rd element index=2 from list of n largest elements
print(b)
'''


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------MATRIX-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------MATRIX INPUT--------------------------------------------------------------------------------------------------------------

# N X N
'''
n=int(input())
lst=[[]]*n
for i in range(n):
    lst[i]=[int(i) for i in input().split()]
print(lst)
'''

# N X M
'''
n,m=[int(x) for x in input().split()]
lst=[[]]*n
for i in range(n):
    lst[i]=[int(i) for i in input().split()]
print(lst)
'''

#-----------------------------------------------COLLECT MAXIMUM COINS-----------------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/collect-maximum-coins-before-hitting-a-dead-end/
# 0-Left
# 1-Right

'''
n,m=[int(x) for x in input().split()]
def isSafe(i,j):
    if i>=0 and i<n and j>=0 and j<m:
        return True
    return False
def collMaxCoins(lst,irow,icol,d):
    if isSafe(irow,icol)==False or lst[irow][icol]=='#':
        return 0
    if lst[irow][icol]=='c':
        result=1
    else:
        result=0

    if d==0:
        return result+max(collMaxCoins(lst,irow,icol-1,0),collMaxCoins(lst,irow+1,icol,1))      #Left
    return result + max(collMaxCoins(lst, irow, icol + 1, 1), collMaxCoins(lst, irow + 1, icol, 0))     #Right

lst=[[]]*n
for i in range(n):
    lst[i]=[chr(ord(i)) for i in input().split()]       #<----- Taking Multiple Character input
print(collMaxCoins(lst,0,0,1))
'''

#-----------------------------------------------MINIMUM WEIGHT IN CART----------------------------------------------------------------------------------------------------------------

#http://prepinsta.com/tcs-digital-advanced-coding-question-0/

'''
n=int(input())

def isSafe(i,j):
    return (i>=0 and i<n and j>=0 and j<n)

def findMinWeight(lst,irow,icol,wt):

    #Terminating Condition
    if isSafe(irow+1,icol)==False and isSafe(irow,icol+1)==False:
        return wt

    w=wt

    #For Boundry Cells:
    if isSafe(irow+1,icol)==False:
        if w<lst[irow][icol]:
            return findMinWeight(lst,irow,icol+1,lst[irow][icol])
        return findMinWeight(lst,irow,icol+1,w)

    if isSafe(irow, icol+1) == False:
        if w < lst[irow][icol]:
            return findMinWeight(lst, irow+1, icol, lst[irow][icol])
        return findMinWeight(lst,irow+1,icol,w)

    #For InBetween Cells:
    wr=lst[irow][icol+1]
    wd=lst[irow+1][icol]

    if wr<wd:   #Go in Right
        if w<wr:
            return findMinWeight(lst,irow,icol+1,wr)
        return findMinWeight(lst,irow,icol+1,w)
    else:       #Go Down
        if w<wd:
            return findMinWeight(lst,irow+1,icol,wd)
        return findMinWeight(lst,irow+1,icol,w)

lst=[[]]*n
for i in range(n):
    lst[i]=[int(x) for x in input().split(',')]
wt=lst[0][0]
print(findMinWeight(lst,0,0,wt))
'''

#-----------------------------------------------MAXIMUM SUBSQUARE SUM---------------------------------------------------------------------------------------------------------------

'''
#https://mail.google.com/mail/u/0/?zx=9azl1slla6s7#search/sample+tcs?projector=1

n=int(input())

def findMaxSubSq(lst):
    

lst=[[]]*n
for i in range(n):
    lst[i]=[int(x) for x in input().split()]
print(findMaxSubSq(lst))
'''

#-----------------------------------------------PANGRAM CHECKER--------------------------------------------------------------------------------------------------------------

#Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.

#Examples : The quick brown fox jumps over the lazy dog ” is a Pangram [Contains all the characters from ‘a’ to ‘z’]
#“The quick brown fox jumps over the dog” is not a Pangram [Doesn’t contains all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing]

'''
s=str(input())
s=s.lower()
s=s.replace(' ','')
res=1
d={}
for i in range(26):
    d[i]=0
#Mapping occourances of alphabets
for i in range(len(s)):
    d[ord(s[i])-ord('a')]+=1
#Checking for atleast 1 frequency of each alphabet
for i in range(len(d)):
    if d[i]==0:
        res=0
        break
if res==1:
    print(True)
else:
    print(False)
'''

#--------------------------------------------------LARGEST SUM SUBSEQUENCE------------------------------------------------------------------------------------------------------------
'''
maxSoFar=-1000000000
maxEndingHere=0
l=[int(x) for x in input().split(',')]
for i in range(len(l)):
    maxEndingHere+=l[i]
    if maxSoFar<maxEndingHere:
        maxSoFar=maxEndingHere
    if maxEndingHere<0:
        maxEndingHere=0
print(maxSoFar)
'''

#------------------------------------Given an n x n square matrix, find sum of all sub-squares of size k x k------------------------------------------------------------------------------------------------------------

'''
#2. Finding Sub-Squares:

def findSubSq(preSum,n,k):
    subSq=[[]]*(n-k+1)
    for i in range(n-k+1):
        subSq[i]=[0]*k

    #Going Row-By-Row
    for i in range(n-k+1):
        sum=0
        #For 1st block of that row
        for j in range(k):
            sum+=preSum[i][j]
        print(sum, end=' ')
        #subSq[i][0]=sum

        #For subsequent blocks
        for j in range(1,n-k+1):
            sum+=preSum[i][j+k-1]-preSum[i][j-1]
            #subSq[i][j]=sum
            print(sum,end=' ')
        print()

#1. Find PreSums
def findPreSum(lst,n,k):

    #preSum will be Matrix of sum of vertical strips of size k in lst
    # Its size will be Rows -> n-k+1 (In 5*5 for 2*2-> rows=4 ie 5-2+1) Cols -> n

    preSum=[[]]*(n-k+1)     #n-k+1 rows in preSum
    #Initializing preSum
    for i in range(n-k+1):
        preSum[i]=[0]*n

    #For each column
    for j in range(n):
        sum=0
        #Finding the Sum of first k cells of that column j
        #ie. For 1st SubSquare:
        # 2,1,2,5,6
        # 3,4,7,8,6
        # 4,-5,-5,-7,6
        # 7,-7,1,2,-3
        # 8,-8,4,2,5
        # We will get Sum of 2+3+4 of !st column
        for i in range(k):
            sum+=lst[i][j]
        preSum[0][j]=sum

        #Sum of remaining SubSquares of that Column j:
        #For 2nd SubSquare in 1st subsquare, remove 1st entry and add k+1th entry
        #ie. Remove 2 from 2+3+4 and add 7 to it.
        #Add till k-1 th row thus left = n-(k-1) = n-k+1
        for i in range(1,n-k+1):                                #Upto n-k+1 bcoz n-k+1 rows in pre-sum
            sum+=lst[i+k-1][j]-lst[i-1][j]
            preSum[i][j]=sum
    print(preSum)
    findSubSq(preSum,n,k)

n,k=[int(x) for x in input().split(' ')]
lst=[[]]*n
for i in range(n):
    lst[i]=[int(x) for x in input().split(' ')]
findPreSum(lst,n,k)
'''

#------------------------------------Given an n x n square matrix, find max-sub square-sum of all sub-squares of size k x k------------------------------------------------------------------------------------------------------------

'''
def maxSubSq(preSum,n,k):
    maxSum=-1000000000
    for i in range(n-k+1):
        s=0
        for j in range(k):
            s+=preSum[i][j]
        if maxSum<s:
            maxSum=s
        for j in range(1,n-k+1):
            s+=preSum[i][j+k-1]-preSum[i][j-1]
            if maxSum < s:
                maxSum = s
    return (maxSum)

def findPreSum(lst,n,k):
    preSum=[[]]*(n-k+1)
    for i in range(n-k+1):
        preSum[i]=[0]*n

    for j in range(n):
        sum=0
        for i in range(k):
            sum+=lst[i][j]
        preSum[0][j]=sum

        for i in range(1,n-k+1):
            sum+=lst[i+k-1][j]-lst[i-1][j]
            preSum[i][j]=sum
    #print(preSum)
    return maxSubSq(preSum,n,k)

#n,k=[int(x) for x in input().split(' ')]
n=int(input())
lst=[[]]*n
for i in range(n):
    lst[i]=[int(x) for x in input().split(' ')]

max=-10000000000
for k in range(2,n+1):
    res=findPreSum(lst,n,k)
    #print(res)
    if res>max:
        max=res
print(max)
'''

'''
4 
2 -8 4 -6
7 1 -5 3
-9 7 6 5
8 3 2 -4
'''

#----------------------------------------------------Inversions in Series------------------------------------------------------------------------------------------

'''
Mockvita-2 Ans2
The input will be a main sequence of N positive integers. From this sequence, a Derived derived sequence will be obtained
 using the following rule. The output is the number of inversions in the derived sequence.

Rule for forming derived sequence

The derived sequence is formed by counting the number of 1s bits in the binary representation 
of the corresponding number in the input sequence.

'''


#O(n^2)

'''
n = int(input())

def findInversions(seq):
    inv=0
    for i in range(n-1):
        for j in range(i+1,n):
            if seq[i]>seq[j]:
                inv+=1
    return inv

def findSetBits(num):
    count=0
    while num>0:
        num=num & num-1
        count+=1
    return count

lst = [int(x) for x in input().split(',')]
seq = [0] * n
for i in range(n):
    seq[i] = findSetBits(lst[i])

print(findInversions(seq))
'''

'''
count=0

def sol(seq,num,k):
    global count
    l=len(seq)
    i=l-1
    while i*i>=num:
        if k == 0:
            return
        m=seq[l-1]//seq[i]
        j=0
        tmp=[]
        while seq[j]<m:
            tmp.append(seq[j])
            j+=1
        count+=len(list(filter(lambda x,y:x*y==m,tmp)))
        i=i-1

def findFactors(num):
    lst=[]
    i=1
    while i*i<=num:
        if num%i==0:
            if num//i==i:
                lst.append(i)
            else:
                lst.append(i)
                lst.append(num//i)
        i+=1
    return lst

from functools import reduce
n,k=[int(x) for x in input().split()]
lst=[int(x) for x in input().split()]
mul=reduce(lambda x,y:x*y,lst)
seq=findFactors(mul)
print(sorted(seq))
sol(seq,mul,k)
print(count)
'''

#--------------------------------------------------------------DISTANCE BETWEEN 2 LOCATIONS ON EARTH-----------------------------------------------------------------------------

'''
It is well known that the shortest path between two points on the surface of the earth (assumed to be a perfect sphere of radius 6400 km) is a great circle route.
 To get this, draw the circle (on the surface of the earth) that goes through the two points which is centred at the centre of the earth. 
 The shorter arc of the circle between the two points is the shortest distance. In the figure below, the solid circle represents the earth 
 (assumed to be a sphere), with centre O. There are two points X and Y on the surface (whose positions can be specified by a latitude and longitude).
  The dotted line represents a circle on the surface of the earth, with centre O. The length of the arc of the circle between X and Y is the great circle distance, 
  which is the shortest distance between the two points while travelling on the surface.

'''

'''
import math
from functools import reduce
n=int(input())
r=6400
def findDist(cord):
    d=0
    for i in range(n-1):
        x = (cord[i][0] - cord[i+1][0])**2
        y = (cord[i][1] - cord[i+1][1])**2
        z = (cord[i][2] - cord[i+1][2])**2
        d+=math.sqrt(x+y+z)
    return d

lst=['']*n
cord=[[]]*n
for i in range(n):
    cord[i]=[0]*3

for i in range(n):
    lst[i]=[str(x) for x in input().split(',')]
    lat=lst[i][0]
    lon = lst[i][1]
    if lat.find('N')!=-1:
        lat=lat.strip('N')
        latR=math.radians(int(lat))
    elif lat.find('S')!=-1:
        lat=lat.strip('S')
        latR=-1*math.radians(int(lat))

    if lon.find('E')!=-1:
        lon=lon.strip('E')
        lonR=math.radians(int(lon))
    elif lon.find('W')!=-1:
        lon=lon.strip('W')
        lonR=(-1)*math.radians(int(lon))
    cord[i][0]=r*math.cos(latR)*math.cos(lonR)
    cord[i][1]=r*math.cos(latR)*math.sin(lonR)
    cord[i][2]=r*math.sin(latR)
print(findDist(cord))
'''
'''
import math
n=int(input())
r=6400
def findDist(cord):
    d=0
    for i in range(n-1):
        tmp=(math.sin((cord[i+1][0]-cord[i][0])/2)**2)+((math.cos(cord[i][0])*math.cos(cord[i+1][0]))*(math.sin((cord[i+1][1]-cord[i][1])/2))**2)
        angle=2*math.asin(math.sqrt(tmp))
        d+=r*angle
    return d

lst=['']*n
cord=[[]]*n
for i in range(n):
    cord[i]=[0]*2

for i in range(n):
    lst[i]=[str(x) for x in input().split(',')]
    lat=lst[i][0]
    lon = lst[i][1]
    if lat.find('N')!=-1:
        lat=lat.strip('N')
        latR=math.radians(int(lat))
        cord[i][0] = latR
    elif lat.find('S')!=-1:
        lat=lat.strip('S')
        latR=-1*math.radians(int(lat))
        cord[i][0] = latR

    if lon.find('E')!=-1:
        lon=lon.strip('E')
        lonR=math.radians(int(lon))
        cord[i][1] = lonR
    elif lon.find('W')!=-1:
        lon=lon.strip('W')
        lonR=(-1)*math.radians(int(lon))
        cord[i][1] = lonR

print(round(findDist(cord)))
'''

'''
3
0N,47E
45N,47E
45S,47E

3
0N,1W
0N,179E
90N,0E
'''

#Replacing items in list with other item
#lst[i].replace(',','')


#---------------------------------------------------TCS National Qualifier---------------------------------------------------------------------------------------------------------

'''
n=int(input())
jump=False
jump2=False

#Cost1-Initial 3 jump
#Cost2-3 Jump at max

def findCost1(lst,cost,index):
    global jump
    print('Item:',lst[index],' Cost1:',cost,' Jump:',jump)
    if index==n:
        return cost
    #Triple Jump
    if index+3<=n and jump==False and lst[index+1]+lst[index+2]+lst[index+3]<3*lst[index+3]:
        jump=True
        return findCost1(lst, cost + 3 * lst[index + 3], index + 3)
    #Double Jump
    if index+2<=n and lst[index+1]+lst[index+2]<2*lst[index+2]:
        return findCost1(lst,cost + 2*lst[index+2],index+2)
    #Single Jump
    return findCost1(lst,cost + lst[index+1],index+1)

def findCost2(lst,cost,index,maximum):
    global jump2
    print('Item:',lst[index],' Cost1:',cost,' Jump:',jump2)
    if index==n:
        return cost
    #Triple Jump
    if index+3<=n and jump2==False and lst[index+3]==maximum:
        jump2=True
        return findCost2(lst, cost + 3 * lst[index + 3], index + 3,maximum)
    if index + 4 <= n and lst[index + 4] == maximum:
        return findCost2(lst, cost + lst[index + 1], index + 1, maximum)
    #Double Jump
    if index+2<=n and lst[index+1]+lst[index+2]<2*lst[index+2]:
        return findCost2(lst,cost + 2*lst[index+2],index+2,maximum)
    #Single Jump
    return findCost2(lst,cost + lst[index+1],index+1,maximum)

lst=[]
lst.append(0)
lst+=[int(x) for x in input().split(',')]
print(lst)
cost=max(findCost1(lst,0,0),findCost2(lst,0,0,max(lst)))
print(cost)
'''

'''
10
5,8,9,5,7,6,2,7,9,1
4
-1,4,8,-2
'''

#------------------------------------------------------------------------Mockvita 1 Solutions---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------Largest Integer--------------------------------------------------------------------------------------------------

#m,n=[int(x) for x in input().split(',')]

#-----------------------------------------------------------------------Codevita Solutions---------------------------------------------------------------------------------------------------

#------------------------------------------------------------------1 : Uncontrolled Cells----------------------------------------------------------------------------------------------------------

'''
m,n,k=[int(x) for x in input().split(',')]


lst=[[0]]*n
for i in range(n):
    lst[i]=[int(i) for i in input().split()]
print(lst)
'''


#------------------------------------------------------------------2 : Square Free Number-------------------------------------------------------------------------------------------------------------

'''
import math

def findFactors(num):
    lst=[]
    i=1
    while i*i<=num:
        if num%i==0:
            if num//i==i:
                lst.append(i)
            else:
                lst.append(i)
                lst.append(num//i)
        i+=1
    return lst

def findPrimeFacts(n):
    lst=set([])
    while n%2==0:
        n=n//2
        lst.add(2)
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            n=n//i
            lst.add(i)
    if n>2:
        lst.add(n)
    print('Prime Factors: ', lst)
    return len(lst)

def findAns(num):
    print(sorted(findFactors(num)))
    return int(math.pow(2,findPrimeFacts(num))-1)

n=int(input())
print(findAns(n))
'''

#------------------------------------------------------------------5 : Hop Max Score-----------------------------------------------------------------------------------------------------------

'''
n=int(input())

def findCost1(lst,cost,index,jump):
    print('Item:',lst[index],' Cost1:',cost,' Jump:',jump)
    if index==n:
        return cost
    #Triple Jump
    if index+3<=n and jump==False and lst[index+1]+lst[index+2]+lst[index+3]<3*lst[index+3]:
        return findCost1(lst, cost + 3 * lst[index + 3], index + 3,True)
    #Double Jump
    if index+2<=n and lst[index+1]+lst[index+2]<2*lst[index+2]:
        return findCost1(lst,cost + 2*lst[index+2],index+2,jump)
    #Single Jump
    return findCost1(lst,cost + lst[index+1],index+1,jump)

def findCost2(lst,cost,index,indexOfMax,jump):
    print('Item:',lst[index],' Cost1:',cost,' Jump:',jump)
    if index==n:
        return cost
    #Triple Jump
    if index+3<=n and jump==False and index+3==indexOfMax:
        return findCost2(lst, cost + 3 * lst[index + 3], index + 3,indexOfMax,True)
    if index + 4 <= n and index + 4 == indexOfMax:
        return findCost2(lst, cost + lst[index + 1], index + 1, indexOfMax,jump)
    #Double Jump
    if index+2<=n and lst[index+1]+lst[index+2]<2*lst[index+2]:
        return findCost2(lst,cost + 2*lst[index+2],index+2,indexOfMax,jump)
    #Single Jump
    return findCost2(lst,cost + lst[index+1],index+1,indexOfMax,jump)

lst=[]
lst.append(0)
lst+=[int(x) for x in input().split(',')]
print(lst)
maxLst=[]
for i in range(len(lst)):
    if lst[i]==max(lst):
        maxLst.append(i)
print('MaxIndexList : ',maxLst)
print()
cost=findCost1(lst,0,0,False)
print()
for i in maxLst:
    c=findCost2(lst,0,0,i,False)
    print('Jump at:',i,' Cost:',c)
    if c>cost:
        cost=c
    print()
print(cost)
'''
'''
n=int(input())

def findCost0(lst,cost,index):
    print('Item:',lst[index],' Cost1:',cost)
    if index==n:
        return cost
    #Double Jump
    if index+2<=n and lst[index+1]+lst[index+2]<2*lst[index+2]:
        return findCost0(lst,cost + 2*lst[index+2],index+2)
    #Single Jump
    return findCost0(lst,cost + lst[index+1],index+1)


def findCost1(lst,cost,index,jump):
    print('Item:',lst[index],' Cost1:',cost,' Jump:',jump)
    if index==n:
        return cost
    #Triple Jump
    if index+3<=n and jump==False and lst[index+1]+lst[index+2]+lst[index+3]<3*lst[index+3]:
        return findCost1(lst, cost + 3 * lst[index + 3], index + 3,True)
    #Double Jump
    if index+2<=n and lst[index+1]+lst[index+2]<2*lst[index+2]:
        return findCost1(lst,cost + 2*lst[index+2],index+2,jump)
    #Single Jump
    return findCost1(lst,cost + lst[index+1],index+1,jump)

def findCost2(lst,cost,index,indexOfMax,jump):
    print('Item:',lst[index],' Cost1:',cost,' Jump:',jump)
    if index==n:
        return cost
    #Triple Jump
    if index+3<=n and jump==False and index+3==indexOfMax:
        return findCost2(lst, cost + 3 * lst[index + 3], index + 3,indexOfMax,True)
    #Double Jump
    if index+2<=n and lst[index+1]+lst[index+2]<2*lst[index+2]:
        return findCost2(lst,cost + 2*lst[index+2],index+2,indexOfMax,jump)
    #Single Jump
    return findCost2(lst,cost + lst[index+1],index+1,indexOfMax,jump)

lst=[]
lst.append(0)
lst+=[int(x) for x in input().split(',')]
print(lst)
maxLst=[]

cost=max(findCost0(lst,0,0),findCost1(lst,0,0,False))
print()
for i in range(3,n):
    c=findCost2(lst,0,0,i,False)
    print('Jump at:',i,' Cost:',c)
    if c>cost:
        cost=c
    print()
print(cost)

'''

#print(~-35)

'''
12
8,4,7,3,7,9,4,2,1,9,7,8
'''

'''
n=int(input())

def findCost1(lst,cost,index,jump):
    if index==n:
        return cost
    #Triple Jump
    if index+3<=n and jump==False and lst[index+1]+lst[index+2]+lst[index+3]<3*lst[index+3]:
        return findCost1(lst, cost + 3 * lst[index + 3], index + 3,True)
    #Double Jump
    if index+2<=n and lst[index+1]+lst[index+2]<2*lst[index+2]:
        return findCost1(lst,cost + 2*lst[index+2],index+2,jump)
    #Single Jump
    return findCost1(lst,cost + lst[index+1],index+1,jump)

def findCost2(lst,cost,index,indexOfMax,jump):
    if index==n:
        return cost
    #Triple Jump
    if index+3<=n and jump==False and index+3==indexOfMax:
        return findCost2(lst, cost + 3 * lst[index + 3], index + 3,indexOfMax,True)
    if index + 4 <= n and index + 4 == indexOfMax:
        return findCost2(lst, cost + lst[index + 1], index + 1, indexOfMax,jump)
    #Double Jump
    if index+2<=n and lst[index+1]+lst[index+2]<2*lst[index+2]:
        return findCost2(lst,cost + 2*lst[index+2],index+2,indexOfMax,jump)
    #Single Jump
    return findCost2(lst,cost + lst[index+1],index+1,indexOfMax,jump)

lst=[]
lst.append(0)
lst+=[int(x) for x in input().split(',')]
maxLst=[]
for i in range(len(lst)):
    if lst[i]==max(lst):
        maxLst.append(i)
cost=findCost1(lst,0,0,False)
for i in maxLst:
    c=findCost2(lst,0,0,i,False)
    if c>cost:
        cost=c
print(cost)
'''


#----------------------------------------------------------Lapindrome Check---------------------------------------------------
'''
t = int(input())
while(t>0):
    t=t-1
    s = input()
    eo = len(s)
    print(s)
'''

#print('Hello World')































