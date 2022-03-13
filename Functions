# ITERATIVE FUNCTIONS
#Practice:
# 1
def increment(p,q):
    global inc
    if q in range(1, 15):
        inc=float(20/100)
    elif q in range(15,20):
        inc=float(10/100)
    elif q in range(20,23):
        inc=float(5/100)
    salary=(float(p*inc)+p)
    return salary

n=input("Employee's Name:")
s=float(input("Employee's Salary:"))
g=int(input("Employee's Grade Scale:"))

print("Increment Amount Is:",increment(s,g)-s)
print("The Updated Salary of ",n,"is:",increment(s,g))

# 2
def update(l2):
    print("l2 is",l2)
    print("location of l2 is",id(l2))
    l2[2]=30
    print("l2 is",l2)
    print("location of l2 is",id(l2))
    return l2

l1=[10,20,30]
print(l1)
print("location of l1 is",id(l1))
update(l1)
print("After returning from function my list is")
print(l1)
print("location of li is",id(l1))

#3
# Cannot input a whole listb/c then there will be no changes in original list!!
# It'll be a new list with separate location
def update(l2):
    print("l2=",l2,"and location is",id(l2))
    l2=[10,20,30]
    print("now l2=",l2,"and location is", id(l2))
    return l2

l1=[100,200,300]
print("l1=",l1,"and location is", id(l1))
update(l1)
print("After returning the fuction")
print("l1=",l1,"and location is", id(l1))

# 4
# In immutable datatype,The original data will not change but there will be a change in location!!
def modify(a):
    print("a=",a,id(a))
    a=50.4
    print("now a=",a,id(a))
    return a
x=20
print("x=",20)
modify(x)
print("After returning the fuction")
print("x=",x)

# 5
def modify(a):
    print("a=",a,"and location is", id(a))
    a=50.4
    print("now a=",a,"and location is", id(a))
    return a
x=20.5
print("x=",20)
modify(x)
print("After returning the fuction")
print("x=",x,"and location is", id(x))

#6
def update(l2):
    print(l2,"location of l2 is",id(l2))
    l2[0]=[2.09,"NED",45]
    l2[1]=100
    l2[2]=400
    print(l2,"location of l2 is",id(l2))
    return l2
l1=[10,20,30]
print(l1,"location of l1 is",id(l1))
update(l1)
print("After returning from function my list is")
print(l1,"location of l1 is",id(l1))

# 7
#airthematic sequence
def seq(p,q,r):
    Tn=a+(n-1)*d
    return Tn

a=int(input("Enter The First Term (a):"))
d=int(input("Enter The Common Difference (d):"))
n=int(input("Enter The No Of Terms (n):"))
seq(a,d,n)
print("The nth Term Of The Sequence Is:",seq(a,d,n))



# 8
#FACTORIALS
def fact(no):
    fact=1
    for i in range(no,1,-1): #OR for i in range(1,no+1)
        fact=fact*i
    return fact
num=int(input("enter no"))
print(num,"!","=",fact(num))

#AVERAGE BY APPLYING FUNCTIONS

#9 (by providing the numbers)
def avg(l2):
    size=len(l2)
    sum=0
    for i in l2:
        sum=sum+i
    avg=sum/size
    return avg
l1=[66,80,90,77,98]
print("The Average result of a class is",avg(l1))

#10 (by user input)
def avg(l2):
    size=len(l2)
    sum=0
    for i in l2:
        sum=sum+i
    avg=sum/size
    return avg
l1=[]
print("Enter marks")
for i in range(0,5):
    l1.append(int(input()))
print(l1)
print("The average result of a class is",avg(l1))

#11
def avg(l2):
    avg=sum(l2)/len(l2)
    return avg
l1=[]
print("Enter marks")
for i in range(0,5):
    l1.append(int(input()))
print(l1)
print("The average result of a class is",avg(l1))

# 12
def acronym(a):
    p=""
    for i in a:
       if i.isupper()==True:
          p=p+i  #Or simply print(i)
       else:
           pass
    return p

s=str(input("Enter A Phrase:").title())
print("The Acronym Of",s,"Is:",acronym(s))

# OR
def acronym(p):
    words=p.split()
    data=" "
    for i in words:
        data=data+i[0].upper()   #OR print(i[0].upper())
    return data
s=str(input("Enter a String:"))
print("The Acronym Of",s,"Is:",acronym(s))

# Printing last letter of each word in capital:
def cap(p):
     print("The last letters of Strings Are:",end="")
     word=p.split()
     for i in word:
         print(i[-1].upper(),end="")

s=str(input("Enter a phrase:"))
cap(s)

# 13 (Product Of Two Lists)
def xmult(a,b):
    l3=[]
    for (num1,num2) in zip (a,b):
        l3.append(num1*num2)
    return l3

l1=[]
l2=[]

n=int(input("No Of Integers In l1:"))
print("Input Integers For List 'l1'")
for i in range(n):
    p=int(input())
    l1.append(p)

m=int(input("No Of Integers In l2:"))
print("Input Integers For List 'l2'")
for i in range(m):
    q=int(input())
    l2.append(q)

print("")
print(l1)
print(l2)
print("")
print("Product Of Integers From l1 and l2:",xmult(l1,l2))

# 14
# Table by While Loop:
def table(tno,trange):
    i=0
    while(i<trange):
        i = i + 1
        t=print(tno,"*",i,"=",tno*i)

no=int(input("Enter table no:"))
range=int(input("Enter table range:"))
table(no,range)

#  Table by for loop
def table(a,b):
    for i in range(1,b+1):
        print(a,"*",i,"=",tno*i)

tno=(int(input("Enter table no:")))
trange=(int(input("Enter table range:")))
table(tno,trange)

# 15
def novowel(v):
    for i in v:
        if i not in "aeiouAEIOU":
            return (print(True))
        else:
            return (print(False))


s = str(input("Enter string:"))
novowel(s)

# 16
# All Integers in the List Are Even:
def alleven(a):
    for i in a:
        if i%2 == 0:
            return (print("True"))
        else:
            return (print("False"))

l = []
n=int(input("Enter The no of integers:"))
for i in range(1,n+1):
    print("Enter integer",i,":")
    n = int(input())
    l.append(n)
print(l)
alleven(l)

# 17
# Printing Negative Numbers Only
def negative(p):
    for i in p:
        if i<0:
            print(i)
            return(print("Negatives"))
        else:
            return(print("No Negative Integers"))

l=[]
n=int(input("Enter no of Integers:"))
for i in range(1,n+1):
    print("Enter integer",i)
    x=eval(input())
    l.append(x)
print(l)
negative(l)

# 18
def even(a):
    print("The numbers divisible by 2 or by 3 are:")
    for i in range(1,a+1):
        if i%2==0:
           print(i,end=" ")
        elif i%3==0:
           print(i,end=" ")

n=int(input("Enter Number:"))
even(n)

# 19
def month(m):
    months=('Jan Feb Mar Apr May June July Aug Sep Oct Nov Dec').split()
    return (months[m-1])

n=int(input("Enter number between 1-12:"))
print("The month is:",month(n))

# 20
def cheer(n):
    print("How do you spell Winner?\nI know I know!")
    for i in n:
        print(i.upper(),end=" ")
    print('!')
    print("")
    print("And that's how you spell Winner!\nGO",n.title(),"!")

name=input("Enter A Team Name:")
cheer(name)



# RECURSIVE FUNCTIONS:

# factorial:
def fact(no):
    if no==0 or no==1:
        return 1
    else:
        return no*fact(no-1)

    # 5*fact(5-1)
    # 4*fact(4-1)
    # 3*fact(3-1)
    # 2*fact(2-1)

num=int(input("Enter any number:"))
print("The factorial of",num,"is:",fact(num))


#Fibonacci sequence (0 1 1 2 3 5 8 13):
def seq(no):
    if no==0:
        return 0
    elif no==1:
        return 1
    else:
       return seq(no-1)+seq(no-2)

num=int(input("Enter number:"))
print("The fibonacci sequence is:",seq(num))

# Table generate:
def table(tnum,i):
    if(i>10):
        return
    else:
       print(tnum,"*",i,"=",tnum*i)
       return table(tnum,i+1)

tno = int(input("Enter the table number:"))
table(tno,1)
