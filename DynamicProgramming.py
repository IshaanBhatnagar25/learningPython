#----------------------------------Fibonacci Series-------------------------------------------------------------

#------------------------Bottom-Up------(Tabulation)-----Time:4.4345855712890625e-05-----------------------------------

'''
import time
tbl=[-1]*1000
def fab(n):
    if tbl[n]!=-1:
        return tbl[n]
    else:
        tbl[0]=0
        tbl[1]=1
        for i in range(2,n+1):
            tbl[i]=tbl[i-1]+tbl[i-2]
        return tbl[n]
t0=time.time()
print(fab(14))
print(fab(7))
t1=time.time()
print(t1-t0)
'''

#-----------------------Top-Down------(Memorization)-------Time:7.534027099609375e-05---------------------------------

'''
import time
mem=[-1]*1000
def fab(n):
    if mem[n]==-1:
        if n<=1:
            mem[n]=n
        else:
            mem[n]=fab(n-1)+fab(n-2)
    return mem[n]
t0=time.time()
print(fab(14))
print(fab(7))
t1=time.time()
print(t1-t0)
'''

#----------------------------------Factorial-------------------------------------------------------------

#------------------------Bottom-Up------(Tabulation)-----Time:5.7220458984375e-05-----------------------------------

'''
import time
tbl=[-1]*1000
def fact(num):
    if tbl[num]!=-1:
        return tbl[num]
    else:
        tbl[0]=1
        for i in range(1,num+1):
            tbl[i]=tbl[i-1]*i
        return tbl[num]
t0=time.time()
print(fact(14))
print(fact(7))
t1=time.time()
print(t1-t0)
'''

#------------------------Top-Down------(Memorization)-----Time:5.1021575927734375e-05----------------------------------

'''
import time
mem=[-1]*1000
def fact(num):
    if mem[num]==-1:
       if num==0:
           return 1
       else:
           return fact(num-1)*num
    return mem[num]

t0=time.time()
print(fact(14))
print(fact(7))
t1=time.time()
print(t1-t0)
'''

# code
ugly = [-1] * 10000
def nthUgly(n):
    ugly[0] = 1
    if ugly[n] != -1:
        return ugly[n]
    else:
        u2, u3, u5 = 0, 0, 0
        for i in range(1000):
            mulU2 = ugly[u2]*2
            mulU3=ugly[u3]*3
            mulu5=ugly[u5]*5
            nextUgly=min(mulU2,mulU3,mulu5)
            ugly[i]=nextUgly
            if nextUgly==u2:
                u2=u2+1
                mulU2=ugly[u2]*2
            if nextUgly==u3:
                u3=u3+1
                mulU3=ugly[u3]*3
            if nextUgly==u5:
                u5=u5+1
                mulu5=ugly[u5]*5
        return ugly[n]
for t in range(int(input())):
    n = int(input())
    print(nthUgly(n))







