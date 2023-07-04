#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#-----------------------------------NumPy------or Numeric Python--------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
'''
It's a Python package that, among others, provides a alternative to the regular python list: the Numpy array.
The Numpy array is pretty similar to a regular Python list, but has one additional feature:
you can perform calculations over all entire arrays.
It's really easy, and super-fast as well.

First of all, Numpy can do all of this so easily
because it assumes that your Numpy array can only contain values of a single type. It's
either an array of floats, either an array of booleans, and so on.

If you do try to create
an array with different types, like this for example,The resulting Numpy array
will contain a single type. The boolean and the float were both
converted to strings.

Second, you should know that a Numpy array is simply a new kind of Python type, like
the float, string and list types from before. This means that it comes with its own methods,
which can behave differently than you'd expect. Take this Python list and this numpy array,

for example:
If you do `python_list + python_list`, the list elements are pasted together, generating
a list . If you do this with the numpy arrays, on the other hand, Python
will do an element-wise sum of the array:
Just make sure to pay attention when you're juggling around with different Python types,
because the outcome can differ a lot!
'''

'''
import numpy as np

#The corressponding values will be added:
a1=np.array([1,2,3])
a2=np.array([3,4,5])
print(a1+a2)

height=[144,154,165,148]
weight=[65,48,69,57]

np_height=np.array(height)
np_weight=np.array(weight)

#bmi_simple=weight/height**2        #<---Error as can't iterate over entire list element-wise

#Solution without NumPy:

bmi_simple=[0]*len(height)
for i in range(len(height)):
    bmi_simple[i]=weight[i]/height[i]**2
print(bmi_simple)

#Conditional Subsequencing is not possible with list
#print(bmi_simple>0.03)         #<-------------Error

#Using Numpy Array
bmi=np_weight/np_height**2

#Printing NumPy Array
print(bmi)

#Subsequencing NumPy Array
print(bmi[1])

#Conditional Subsequencing
print(bmi>0.003)        #Boolean Result
print(bmi[bmi>0.003])   #Values in result

#Fact:
#In this NumPy Array all the values will be stored as a String
multiDataTypeArray=np.array([12,True,'Yo',18.5674,'A'])
print(multiDataTypeArray)

#The corressponding values will be added:
a1=np.array([1,2,3])
a2=np.array([3,4,5])
print(a1+a2)

#Type of NumPy Arrays:

print(type(a1))         #ndArray ie N-Dimenssional Array
'''

#------------------------------------------------------------------------------------------------------------------
#----------------------------------------------2D Arrays------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

'''
import numpy as np

#Declaring 2d Array:
# np.array([
# [...],
# [...]
# ])

np2d=np.array([
    [3,5,7,9],
    [8.3,1.2,4.9,2.1]
])

#.shape will give the size of array: (rows,columns)
print(np2d.shape)

######Subsetting:

#1: Row and Column
print(np2d[1][2])

print(np2d[1,2])

#Using ":" :

# np2d[row_i:row_j,col_l:col_m]
# From i to j(excluded) row, select the cell from l to m(excluded) column

# 2 or more columns at a time:
print(np2d[:,2:3])
#   : <--means from both rows
#   2:3 <--means 2 to 3 (excluded) column of earlier selected row

print(np2d[:,:]) #<--All rows all columns

a1=np.array([
    [1,2,3],
    [3,2,4]
])

a2=np.array([
    [1,1,2],
    [1,1,2]
])

print("Result:")
print(a1-a2)
'''

#------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Array Functions in NumPy---------------------------------------------
#------------------------------------------------------------------------------------------------------------------

'''
import numpy as np

#Generating Random Data for Computation:

#np.random.normal(distribution_mean,standard_deviation,number_of_samples)
#eg.    -->  np.random.normal(1.75,0.20,500)

height=np.round(np.random.normal(1.75,0.20,50),2)
weight=np.round(np.random.normal(60.32,15,50))
np_city=np.column_stack((height,weight))

#Mean():
#np.mean
#np.mean(arr,itr,int,float)

#eg.
#Average height:
# Taking mean of entries from 1st column of each row:
print(np.mean(np_city[:,0]))
#Average weight
print(np.mean(np_city[:,1]))

#Median()
print(np.median(np_city[:,0]))
'''

#------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Broadcasting---------------------------------------------
#------------------------------------------------------------------------------------------------------------------

'''
The term broadcasting refers to the ability of NumPy to treat arrays of different shapes during arithmetic operations. 
Arithmetic operations on arrays are usually done on corresponding elements. If two arrays are of exactly the same shape,
then these operations are smoothly performed.


If the dimensions of two arrays are dissimilar, element-to-element operations are not possible. 
However, operations on arrays of non-similar shapes is still possible in NumPy, because of the broadcasting capability. 
The smaller array is broadcast to the size of the larger array so that they have compatible shapes.
'''

'''
import numpy as np

a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])

print('First array:')
print(a)
print('\n')

print('Second array:')
print(b)
print('\n')

print('First Array + Second Array')
print(a + b)
'''

'''
The following figure demonstrates how array b is broadcast to become compatible with a.

0   0   0       1   2   3
10  10  10      1   2   3       }
20  20  20  +   1   2   3       }- This is broadcasting of 'a'
30  30  30      1   2   3       }
'''

#------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Matrix Operations using NumPy---------------------------------------------
#------------------------------------------------------------------------------------------------------------------

'''
np.arange(start,stop,step)
np.arange(0,10,2)

What arange([start],stop,[step]) does is that it arranges numbers from starting to stop, in steps of step. 
eg.     np.arange(0,10,2):  
                        return an np list starting from 0 all the way upto 10 but don’t include 10 and increment numbers by 2 each time.



np.zeros((n,m)) returns an n x m matrix that contains zeros. It’s as simple as that.
(n,m) needs to be in a bracket inside the bracket.


np.eye() returns an identity matrix with the specified dimensions.


np.dot() performs matrix multiplication, provided both the matrices are “multiply-able”.
It just means that the number of columns of the first matrix must match the number of rows in second matrix.
 
 
np.sum() adds all the elements of the matrix.

1. Sum along the rows.
# sum along the rows
np.sum(M,axis=1)

2. Sum along the columns.
# sum along the cols
np.sum(M,axis=0)


np.random.rand(m,n):
    Will generate mxn matrix of mxn of random values (0 to 1)
eg. generate random values in a 2 x 3 matrix form
np.random.rand(2,3)


np.append() adds elements into the specified array.
It’s important that you capture the returned values or otherwise those elements wouldn’t be actually updated to the old list. 
eg.     
    A = np.append(A,[3,55,34,553])


np.diff(array,n=iterations): find A[n+1]-A[n] continuously
Instead of doing it twice explicitly, I could tell np.diff() to do it twice for me and still end up with the same results. Here’s what I mean:
 np.diff(A,n=2)
 
 It will find a[n+1]-a[n] for 2 iterations decreasing the size of original array by 1 in each iteration.
 

np.vstack((rowList1,rowList2,rowList3)):   Will stack the lists to form rows of matrix.
eg. np.vstack(a,b,c)


np.column_stack((rowList1,rowList2,rowList3)):   Will stack the lists to form rows of matrix column wise.
eg. np.column_stack(a,b,c)


a = [1,2,3]
b = [4,5,6]
c = [7,8,9]


np.vstack((a,b,c))
===================================================================
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
       
np.column_stack((a,b,c))
===================================================================
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
       

Slicing:

A[lowerbound(inclusive): upperbound(exclusive)]
eg.
A
===================================================================
array([  5,   7,   9,  11,  13,  19,   3,  55,  34, 553])

A[2:5]  
===================================================================
array([ 9, 11, 13])


'''

'''
import numpy as np

#Making a
a = np.arange(1,10,1).reshape(3,3)
print(a)

#Making b
b=np.arange(9,0,-1).reshape(3,3)
print(b)

#Zero Matrix
zero=np.zeros((3,3))
print(zero)

#Identity Matrix
identity=np.eye(3)
print(identity)

#Multiple a with b
print(np.dot(a,b))

#Multiple a with zero matrix
print(np.dot(a,zero))

#Multiple b with identity matrix
print(np.dot(b,identity))

#Sum along rows:
print(np.sum(a,axis=0))

#Sum along columns
print(np.sum(a,axis=1))

#Random Matrix Generation:
r=np.random.rand(3,3)
print(r)


x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

rowRes=np.vstack((x,y,z))
colRes=np.column_stack((x,y,z))
print(rowRes,'\n',colRes)
'''



#------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Statistics using NumPy---------------------------------------------
#------------------------------------------------------------------------------------------------------------------


'''
numpy.amin() and numpy.amax()
These functions return the minimum and the maximum from the elements in the given array along the specified axis(row/column).


numpy.ptp()
The numpy.ptp() function returns the range (maximum-minimum) of values along an axis.



numpy.percentile()
Percentile (or a centile) is a measure used in statistics indicating the value below which a given percentage of observations 
in a group of observations fall. The function numpy.percentile() takes the following arguments.

numpy.percentile(a, q, axis)
Where,
Sr.No.	Argument    Description
1       a           Input array
2       q           The percentile to compute must be between 0-100
3       axis        The axis along which the percentile is to be calculated


numpy.median()
Median is defined as the value separating the higher half of a data sample from the lower half.


numpy.mean()
Arithmetic mean is the sum of elements along an axis divided by the number of elements.
The numpy.mean() function returns the arithmetic mean of elements in the array.
If the axis is mentioned, it is calculated along it.


numpy.average()
Weighted average is an average resulting from the multiplication of each component by a factor reflecting its importance. 
The numpy.average() function computes the weighted average of elements in an array according to their respective weight 
given in another array. The function can have an axis parameter. If the axis is not specified, the array is flattened.

Considering an array [1,2,3,4] and 
corresponding weights [4,3,2,1], 

the weighted average is calculated by 
adding the product of the corresponding elements and dividing the sum by the sum of weights.

Weighted average = (1*4+2*3+3*2+4*1)/(4+3+2+1)




numpy.std()
Standard deviation is the square root of the average of squared deviations from mean. 
The formula for standard deviation is as follows −
std = sqrt(mean(abs(x - x.mean())**2))

If the array is [1, 2, 3, 4], then its mean is 2.5.
 Hence the squared deviations are [2.25, 0.25, 0.25, 2.25] and 
 the square root of its mean divided by 4, 
 i.e., sqrt (5/4) is 1.1180339887498949.
 
 
numpy.var()
Variance
Variance is the average of squared deviations, i.e., mean(abs(x - x.mean())**2). In other words, the standard deviation is the square root of variance.

'''
'''
import numpy as np

a = np.random.rand(5,5)
b = np.arange(5,130,5).reshape(5,5)

print(a,'\n\n',b,'\n')

print(np.amin(b),' ',np.amax(b),'\n')

print(np.ptp(a),'\n')

#Will give the percent of values in b lying below the
print(np.percentile(b,40),'\n')

print(np.median(b),'\n')

print(np.mean(b),'\n')

print(np.average(b,weights=a),'\n')

print(np.std(b),'\n')

print(np.var(b),'\n')
'''

#------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Linear Algebra using NumPy---------------------------------------------
#------------------------------------------------------------------------------------------------------------------

'''
NumPy package contains numpy.linalg module that provides all the functionality required for linear algebra. 

Some of the important functions in this module are described in the following table.

Sr.No.	    Function     Description
1	        dot          Dot product of the two arrays
2       	vdot         Dot product of the two vectors
3       	inner        Inner product of the two arrays
4       	matmul       Matrix product of the two arrays
5       	determinant  Computes the determinant of the array
6       	solve        Solves the linear matrix equation
7       	inv          Finds the multiplicative inverse of the matrix
'''