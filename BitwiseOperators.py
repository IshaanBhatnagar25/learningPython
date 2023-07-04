#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------BITWISE OPERAOTRS---------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------FACTS----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
OPERATOR	DESCRIPTION	        SYNTAX      EXAMPLE
&	        Bitwise AND	        x & y       3 & 13 : 0011 & 1101 -> 0001
|	        Bitwise OR	        x | y       3 | 13 : 0011 | 1101 -> 1111
~	        Bitwise NOT	        ~x          ~13 : ~1101 -> 0010
^	        Bitwise XOR	        x ^ y       3 ^ 13 : 0011 ^ 1101 -> 1110
>>	        Bitwise right shift	x>>         13>>1 : 00001101>>1 -> 00000110
<<	        Bitwise left shift	x<<         13<<1 : 00001101<<1 -> 00011010

1) The left shift and right shift operators should not be used for negative numbers

2) The bitwise operators should not be used in place of logical operators.
The result of logical operators (&&, || and !) is either 0 or 1, but bitwise operators return an integer value.
Also, the logical operators consider any non-zero operand as 1. For example, consider the following program,
 the results of & and && are different for same operands.

int main()
{
   int x = 2, y = 5;
   (x & y)? printf("True ") : printf("False ");
   (x && y)? printf("True ") : printf("False ");
   return 0;
}
// Output: False True

3) The left-shift and right-shift operators are equivalent to multiplication and division by 2 respectively.
As mentioned in point 1, it works only if numbers are positive.

int main()
{
   int x = 19;
   printf ("x << 1 = %d\n", x << 1);
   printf ("x >> 1 = %d\n", x >> 1);
   return 0;
}
// Output: 38 9

4) The & operator can be used to quickly check if a number is odd or even
The value of expression (x & 1) would be non-zero only if x is odd, otherwise the value would be zero.

int main()
{
   int x = 19;
   (x & 1)? printf("Odd"): printf("Even");
   return 0;
}
// Output: Odd

6) The ~ operator should be used carefully
The result of ~ operator on a small number can be a big number if the result is stored in an unsigned variable.
 And result may be negative number if result is stored in signed variable (assuming that
 the negative numbers are stored in 2’s complement form where leftmost bit is the sign bit)
'''

'''
#Shift Operators:
a=19
print(a>>1)     #Eqivalant to a//2
print(a<<1)     #Eqivalant to a*2

# & Operator to check even or odd:
a=17
if a&1 == 1:
    print("Odd")
else:
    print("Even")
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------DECIMAL TO BINARY-------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------1--------------------------------------------------------------------------------------------------------
'''
n=bin(int(input()))
l=len(str(n))-2
'''
#------------------------------2----IN PYTHON 3.6 ABOVE---DON'T WORK WITH MOST ONLINE COMPILERS-------------------------------------------------------------------------------------------------
'''
n = int(input())
b = f'{n:b}'
print(b)
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------Bit-Wise XOR----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------FACTS--------------------------------------------------------------------------------------------------------

'''

The set bits of A^B will tell which bits of A & B are different.
eg. 1011 ^ 1000 ->0011  -> ie. 1st and 2nd bit of A and B are different.


A^A = 0     1010^1010=0000
A^~A = 1    1010^0101=1111

A^0 = A     1010^0000=1010
A^1 = ~A     1010^1111=0101

XOR of 'n' Consecutive numbers:
1- Find the remainder of n by moduling it with 4.
2- If rem = 0, then xor will be same as n.
3- If rem = 1, then xor will be 1.
4- If rem = 2, then xor will be n+1.
5- If rem = 3 ,then xor will be 0.
'''

#------------------------1. Find Item with single occourance from a list with 2 occourances of each item-----------------------------------------------------------------------------------------------------------------------------------

'''
def process(lst):
    ans=0
    for item in lst:
        ans = ans ^ item
    return ans

l=[15,20,15,25,20,17,25]
print(process(l))
'''

#------------------------2. Find missing consecutive number from list of n numbers (1 to n)-----------------------------------------------------------------------------------------------------------------------------------
'''
  1) XOR all the array elements, let the result of XOR be X1.
  2) XOR all numbers from 1 to n, let XOR be X2.
  3) XOR of X1 and X2 gives the missing number.
   Reason:
    x1= a1^a2^a3^a4^a5
    x2= a1^a3^a4^a5
    x1^x2=a2 (a^a=0 ans a^0=a)
'''

'''
def find(lst):
    x1=1
    x2=lst[0]
    n=len(lst)
    for i in range(n):
        x2 ^= lst[i]
    for i in range(n+2):
        x1 ^= i
    return x1 ^ x2
l=[1,5,6,2,3]
print(find(l))
'''

#------------------------3. Swap two numbers without using a temporary variable-----------------------------------------------------------------------------------------------------------------------------------

'''
a=10
b=15
a^=b
b^=a
a^=b
print(a,b)
'''

#------------------------4. Two numbers with odd occurrences in an unsorted array-------Classic---------------------------------------------------------------------------------------------------------------------------

'''
The idea is similar to method 2 of this post. Let the two odd occurring numbers be x and y. We use bitwise XOR to get x and y. 
The first step is to do XOR of all elements present in array. XOR of all elements gives us XOR of x and y because of the 
following properties of XOR operation.
1) XOR of any number n with itself gives us 0, i.e., n ^ n = 0
2) XOR of any number n with 0 gives us n, i.e., n ^ 0 = n
3) XOR is cumulative and associative.

So we have XOR of x and y after the first step. Let the value of XOR be xor2.
Every set bit in xor2 indicates that the corresponding bits in x and y have values different from each other.
For example, if x = 6 (0110) and y is 15 (1111), then xor2 will be (1001), the two set bits in xor2 indicate that the 
corresponding bits in x and y are different. In the second step, we pick a set bit of xor2 and divide array elements in two groups. 
Both x and y will go to different groups. In the following code, the rightmost set bit of xor2 is picked as it is easy to get rightmost
set bit of a number. If we do XOR of all those elements of array which have the corresponding bit set (or 1), then we get the first odd number.
And if we do XOR of all those elements which have the corresponding bit 0, then we get the other odd occurring number.
This step works because of the same properties of XOR. All the occurrences of a number will go in same set. XOR of all occurrences 
of a number which occur even number number of times will result in 0 in its set. And the xor of a set will be one of the
odd occurring elements.
'''

'''
def find(arr):
    xor=0
    n=len(arr)

    #Finding xor of 2 numbers:
    for i in range(n):
        xor^=arr[i]

    #Finding first set bit of xor:
    firstSetBit=xor & ~(xor-1)

    #Finding 2 numbers:
    x,y=0,0

    for i in range(n):

        #1st group with that bit set:  & will give 1 ->Give num1
        if firstSetBit & arr[i]:
            x^=arr[i]
        # 2nd group with that bit not set:  & will give 0   ->Give num2
        else:
            y^=arr[i]
    return x,y

arr=[2,5,8,5,2,7,6,8,7,12]
print(find(arr))
'''

#------------------------5. Add two numbers without using arithmetic operators----HALF ADDRER-----------------------------------------------------------------------------------------------------------------------

'''
def add(x,y):
    while(y!=0):
        carry = x & y
        x = x ^ y
        y = carry<<1
    return x
print(add(12,13))
'''

#------------------------6. Count number of bits to be flipped to convert A to B--------------------------------------------------------------------------------------------------------------------------

#XOR will give the number of different bits
#Count those bits to get ans

'''
a,b=[int(x) for x in input().split()]
a=a^b
count=0
while(a>0):
    count+=a&1
    a=a>>1
print(count)
'''

#------------------------7. Detect if two integers have opposite signs--------------------------------------------------------------------------------------------------------------------------

# Find a^b and left-shift by 31 bits: 0-Same Sign -1 - Opposite Sign
'''
a,b=[int(x) for x in input().split()]
a = ((a ^ b) >> 31)
print(a)
'''

#Find a^b if it is <0 ->Then opposite signs
'''
def oppositeSigns(x, y):
    return ((x ^ y) < 0)
x = 100
y = -1
if (oppositeSigns(x, y) == True):
    print("Signs are opposite")
else:
    print("Signs are not opposite")
'''

#------------------------8. Given a set, find XOR of the XOR’s of all subsets.--------------------------------------------------------------------------------------------------------------------------

# {1,2,3}-> {1},{2},{3},{1,2},{1,3},{2,3},{1,2,3},{}
# Now XOR of all elements : Each element will appear even number of times, thus XOR = 0

#The number of subsets for (n-1) elements is equal to 2(n-1) which is always even when n>1.
# Thus, in the XOR result, every element is included even number of times and XOR of even occurrences of any number is 0.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------GENERAL----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------Finding the right-most set bit of a number:---------------------------------------------------------------------

'''
num & ~(num-1)
eg. 6 ->num=0110     
        num-1=0101
        ~(num-1)=1010
        num & ~(num-1)=0010   ->ie. 2nd bit is the set bit.
'''
#num=int(input())
#print(num & ~(num-1))

#---------------------------------PROGRAM TO COUNT ALL SET BIT OF A NUMBER:---------------------------------------------------------------------

#While the number is not 0, AND the bits of number with 1 and then lest shift it to get next bit of number.

'''
num=int(input())
count=0
while(num>0):
    count+=num&1
    num=num>>1
print(count)
'''

#---------------------------------PROGRAM TO FIND WHETHER A NUMBER IS POWER OF 2---------------------------------------------------------------------

'''
def isPow(x):
    return (x and not(x & (x-1)))
print(isPow((int(input()))))
'''

'''
n=int(input())
if (n & (n-1)) == 0:
    print("Power of 2")
else:
    print("No")
'''

#---------------------------------PROGRAM TO check if a number has bits in alternate pattern---------------------------------------------------------------------
'''
n=int(input())
num=n ^ (n >> 1)
if n^(n>>1):
    print("Yes")
else:
    print("No")
'''

#----------------------------------------------Equal Sum and XOR----- A+B=A^B-----------------------------------------------------------------------------------------------------

'''
Given a positive integer n, find count of positive integers i such that 0 <= i <= n and n+i = n^i

Since we know a + b = a ^ b + 2 * (a & b)

We can write, n + i = n ^ i + 2 * (n & i)

So n + i = n ^ i implies n & i = 0

Hence our problem reduces to finding values of i such that n & i = 0.

We can use the count of unset-bits in the binary representation of n.
For n & i to be zero, i must unset all set-bits of n. If the kth bit is set at a particular in n,
kth bit in i must be 0 always, else kth bit of i can be 0 or 1

Hence, total such combinations are 2^(count of unset bits in n)
'''

'''
#Finding unset bits in n:
def count(n):
    ans=0
    while n>0:
        if n&1==0:
            ans+=1
        n=n>>1
    return pow(2,ans)

n=int(input())
print(count(n))
'''

#-----------------------------------------------------FLIPPING THE BITS OF A NUMBER---------------------------------------------------------------------------------------------------------

'''
It can be done by a simple way, just simply subtract the number from
the value obtained when all the bits are equal to 1 .

eg. 1011-> 1111-1011=0100
'''

#n=bin(int(input()))
#l=len(str(n))-2
'''
n = int(input())
b = f'{n:b}'
print(b)
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------BIT MANIPULATION----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
N << 1	= N*2
N << 2 = N*pow(2,2)
N << k = N*(pow(2,k))
N >> 1	= floor(N/2)
N >> 2 = floor(N/pow(2,2))
N >> k = floor(N/pow(2,k))
N & 1	= last bit in N
N & 3	= last 2 bits in N
N & 7	= last 3 bits in N
N & (pow(2, k)-1) = last k bits in N
~N + 1 = -N
N & 0xFF = least significant byte of integer or the last 8 bits of integer.
An Integer normally has 4 bytes(32 bits)
F in hex is 1111 in binary, so FF(or 0xFF) is 11111111 in binary
Doing N & 0xFF removes the first 3 bytes and only keeps the last byte(8 bits) of integer
Eg 1783 in binary is 11011110111
1783 & 0xFF only keeps the last 8 bits of 11011110111, and is, 11110111, which is 247
'''

#---------------------------------------------------COUNTING NUMBER OF SET BITS-------------------------------------------------------------------------------------------------------------

#In GCC, we can directly count set bits using __builtin_popcount(). So we can avoid a separate function for counting set bits.

#-----------------------------------------------------BRUTE FORCE-------Theta(logn)----------------------------------------------------------------------------------------------------

#Using Loops:
'''
def  count(n):
    s = 0
    while (n):
        s += n & 1
        n >>= 1
    return s
print(count(int(input())))
'''

#Using Recurssion:
'''
def count(n):
    s=0
    if n==0:
        return 0
    return (n & 1)+count(n >> 1)
n=int(input())
print(count(n))
'''

#----------------------------------------------------Brian Kernighan’s--------O(logn)---------------------------------------------------------------------------------------------------

'''
So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the rightmost set bit.
 If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.
The beauty of this solution is the number of times it loops is equal to the number of set bits in a given integer.
'''

'''
def count(n):
    s=0
    while n!=0:
       n = n & (n-1)
       s+=1
    return s
print(count(int(input())))
'''

#Using Recurssion:
'''
def count(n):
    if n==0:
        return 0
    return 1+count(n & (n-1))
print(count(int(input())))
'''

#---------------------------------------------------COUNTING NUMBER OF UNSET BITS-------------------------------------------------------------------------------------------------------------
'''
def  count(n):
    s = 0
    while (n):
        if n & 1 == 0:
            s=s+1
        n >>= 1
    return s
print(count(int(input())))
'''

#--------------------------------------Set the kth bit of N(counting from right) to 1------------------------------------------------------------------------------------------------------------

'''
take 1, shift it k-1 places left, so its at kth place.
do 'OR' with N.
N = N | (1 << (k-1))
'''
'''
n,k=[int(x) for x in input().split(" ")]
print(bin(n))
n=n|(1<<(k-1))
print(bin(n))
'''

#--------------------------------------Reset the kth bit of N(counting from right) to 1------------------------------------------------------------------------------------------------------------

'''
take 1, shift it k-1 places left, so its at kth place.
inverse it, so it becomes 0 and everything else is 1
do 'AND' with N.
N = N & ~(1 << (k-1))
'''

'''
n, k = [int(x) for x in input().split(" ")]
print(bin(n))
n = n & ~(1 << (k-1))
print(bin(n))
'''

#--------------------------------------Flip the kth bit of N(counting from right) to 1------------------------------------------------------------------------------------------------------------
'''
XOR is used for flipping(changing/reversing) the bit
take 1, shift it k-1 places left, so it is at kth place.
do 'XOR' with N.
N = N ^ (1 << (k-1))

eg. 0^1=1
    1^1=0 ie ~
'''
'''
n, k = [int(x) for x in input().split(" ")]
print(bin(n))
n = n ^ (1 << (k-1))
print(bin(n))
'''

#--------------------------------------Turn off the first set bit(1 bit) of a number N1------------------------------------------------------------------------------------------------------------
'''
Find the first set bit as n & ~(n-1)
Negete the first set bit and & it with num
'''
'''
n=int(input())
print(bin(n))
firstSetBit=(n & ~(n-1))
print(bin(n & ~firstSetBit))
'''


#----------------------------------------------Get the 5 highest bits of an integer(8 bit integer).-----------------------------------------------------------------------------------------------------------

'''
for getting the 5 highest bits, we will remove the lower 3 bits and do 'AND' with 11111.
we create 11111 by left shifting 1 by 5, 1 << 5, which gives 100000, and subtracting 1, which gives 11111.
so we create 11111 by (1 << 5)-1
we remove the lower 3 bits of x by (x >> 3)
Doing 'AND' gives us the final answer.
(x >> 3) & ((1 << 5)-1)
'''

'''
#n is 8 bit integer:
n=int(input())
print(bin(n))
print(bin(n>>3 & ((1<<5)-1)))
'''

#----------------------------------------------Check whether the kth bit in N is 1-----------------------------------------------------------------------------------------------------------
'''
Shift 1 by k-1 place to right
& it with num
Shift it right to k-1 places
'''

'''
n, k = [int(x) for x in input().split(" ")]
print(bin(n))
print((1<<(k-1) & n)>>(k-1))
'''






#-----------------------------------------------------Range Queries-----------------------------------------------------------------------------------------------------------

#Given Q queries, with each query consisting of two integers L and R, the task is to find the total numbers between L and R (Both inclusive),
# having "atmost" three set bits in their binary representation.


#Inefficient:
'''
def check(n):
    if n == 0:
        return 0
    return 1 + check(n & (n-1))
for t in range(int(input())):
    for q in range(int(input())):
        a, b = [int(x) for x in input().split(" ")]
        count = 0
        while a != b+1:
            if check(a) <= 3:
                count += 1
            a += 1
        print(count)
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------- CONVERSIONS --------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------DECIMAL TO BINARY-------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------CONVERTING TO BINARY-------------------------------------------------------------------------------------------------

#Using Strings:
'''
def convert(n):
    ans=''
    while n>0:
        ans=ans+str(n%2)
        n=n//2
    return "".join(reversed(ans))
n=int(input())
print(convert(n))
'''

#Using Array--Incorrect
'''
def toBin(n):
    i=0
    lst=[]
    while n>0:
        lst.append(n%2)
        i+=1
        n=n//2
    s=''.join(str(e) for e in lst)      #Converting list to String
    return int(s)                       #Returning int after converting string to int
n=int(input())
print(toBin(n))
'''

#Stack Based-Reccursive:
'''
def toBin(n):
    if n>1:
        toBin(n//2)
    print(n%2,end='')
n=int(input())
toBin(n)
'''

#Iterative:
#For any number, we can check whether its ‘i’th bit is 0(OFF) or 1(ON) by bitwise ANDing it with “2^i” (2 raise to i).
#unsigned integer (32 bit), which consist of 0-31 bits. To print binary representation of unsigned integer, start from 31th bit,
#check whether 31th bit is ON or OFF, if it is ON print “1” else print “0”.
'''
def f(n):
    i=1<<31
    while i>0:
        if n&i:
            print('1',end='')
        else:
            print('0',end='')
        i=i//2
n=int(input())
f(n)
'''

#----------------------------------------------------DECIMAL TO OCTAL-------------------------------------------------------------------------------------------------------------------------------------------------
'''
def f(n):
    if n>1:
        f(n//8)
    print(n%8,end='')
n=int(input())
f(n)
'''

#----------------------------------------------------DECIMAL TO HEXA-------------------------------------------------------------------------------------------------------------------------------------------------
'''
def f(n):
    if n>1:
        f(n//16)
    if n%16<10:
        print(n % 16, end='')
    else:
        if n%16==10:
            print('A',end='')
        elif n%16==11:
            print('B',end='')
        elif n%16==12:
            print('C',end='')
        elif n%16==13:
            print('D',end='')
        elif n%16==14:
            print('E',end='')
        elif n%16==15:
            print('F',end='')
n=int(input())
f(n)
'''

#----------------------------------------------------GREY CODE-----------------------------------------------------------------------------------------------------------------------------------------------

'''
Gray code has property that two successive numbers differ in only one bit because of this property gray code does the 
cycling through various states with minimal effort and used in K-maps, error correction, communication etc.
'''

#------------------------------------------------BINARY TO GREY CODE-----------------------------------------------------------------------------------------------------------------------------------------------

'''
1. The Most Significant Bit (MSB) of the gray code is always equal to the MSB of the given binary code.
2. Other bits of the output gray code can be obtained by XORing binary code bit at that index and previous index.
'''

'''
def f(n):
    lst=[]
    if n>1:
        f(n//2)
    lst.append(n%2)
    s=''.join(str(e) for e in lst)
    return int(s)
n=int(input())
print(f(n))
'''



