#DATA TABLE:
#1
s=[100,"Zain","zain@gmail.com","Karachi",3.8]
print("Printing Student Data")
print("Name:%s, ID=%s,address=%s, Gpa=%f, number=%d" %(s[1],s[2],s[3],s[4],s[0]))

#2
emp=["John",100000,"USA"]
print("Printing Employee Data")
print("Name:%s\nSalary:%f\nCountry:%s"%(emp[0],emp[1],emp[2]))

#3
n = input("Enter Your Name:")
fn = input("Enter Your Father's Name:")
r = int(input("Enter Your Roll No:"))
l1 = []
l2 = []
for i in range(5):
    sub = (input("Enter Subject Name:"))
    l1.append((sub))
    print("Enter Obtained Marks Of", sub, ":", end="")
    l2.append(float(input()))
sum = sum(l2)
per = (sum / 500) * 100

if (per >= 85 and per <= 100):
    grade = "You obtained 'A' grade"
elif (per >= 75 and per <= 84):
    grade = "You obtained 'B' grade"
elif (per >= 65 and per <= 74):
    grade = "You obtained 'C' grade"
else:
    grade = "You have 'Failed'"

s = [n, fn, r, per, grade]
print("\n")
print('"RESULT"')
print("Name=%s\nFather's Name=%s\nRoll No=%d" % (s[0], s[1], s[2]))
print("Sub""\t""Marks")
print("", l1[0], "=", l2[0], "")
print("", l1[1], "=", l2[1], "")
print("", l1[2], "=", l2[2], "")
print("", l1[3], "=", l2[3], "")
print("", l1[4], "=", l2[4], "")
print("Total Marks:500")
print("Percentage=%f\nGrade=%s" % (s[3], s[4]))


#DATATYPES
#1
a=100.26
b="NED,SOFTWARE DEPART SEC A"
c=3.5679999
d=2+3j

print(a,"\t",b,"\t",c,"\t",d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("After type casting")
print("c is now",complex(c))

#2
datalist = [300, 12.65, 5 + 6j, True, 'Faisal', (5, -7), [8, 52], {"color":'blue',"color":'red'}]
for item in datalist:
     print ("Type of ",item, " is ", type(item))


#PROBLEMS SOLVING
#1
C=int(input("Enter Temperature In Degree Celsius"))
F=(C*9/5)+ 32
print("Temperature in Degree Fahrenheit is",F)

#2
F=int(input("Enter Temperature In Degree Fahrenheit"))
C=(F-32)* 5/9
print("Temperature in Degree Celsius is",C)

#3
l=int(input("Enter Length Of Your Rectangle"))
b=int(input("Enter Breadth Of Rectangle"))
area=l*b
print("The area of rectangle,with length",l,"and breadth",b,"is",area)

#4
import math
r=int(input("Enter Radius Of Sphere"))
volume=4/3*math.pi*r*r*r
print ("volume of sphere,with radius ",r," is",volume)

#5
import math
r=float(input("enter radius of a circle"))
area=math.pi*r*r
print("the area of a circle with radius ",r," is",area)

#6
import math
u=float(input("Give initial velocity of the car (in miles/hr):"))
a=float(input("Give acceleration of the car (in miles/hr^2):"))
t=float(input("Give time (in hrs):"))
#distance=(u*t)+(1/2*(a*t*t))
print("Ditance travelled by the car is (in miles)",(u*t)+(1/2*(a*t*t)))

#7
import math
r=float(input('Give radius of the wheel (in meters):'))
w= float (input('Give angular speed of the wheel (in rad/sec):'))
v=r*w
#linearvelocity=r*w
print("linear velocity(in meter/sec) is:",r*w)
t=float(input('Enter time (in sec):'))
#distance=v*t
print("Distance travelled by car (in meters):",v*t)

#8
import math
r=float(input('Give radius of the circle (in meters):'))
v=float(input('Give linear speed(in meter/sec):'))
#w=v/r
print("The angular speed (in rad/sec):",v/r)

#9
import math
velocity = float(input('Give me a velocity to fire at (in m/s): '))
angle = float(input('Give me an angle to fire at: '))
distance = float(input('Give me how far away you are from the structure: '))
height = float(input('Give me the height of the structure (in meters): '))
slingshot = 5 #Height of slingshot in meters
gravity = 9.8 #Earth gravity

angleRad = math.radians(angle)
x = math.cos(angleRad)
y = math.sin(angleRad)

time = distance/(velocity*x)
vx = x
vy = y + (-9.8 * time)
finalVelocity = math.sqrt((vx ** 2) + (vy ** 2))
print ("final velocity",math.sqrt((vx ** 2) + (vy ** 2)))

#10

h=float(input("Give height (in feet):"))
u=float(input("give initial velocity (in ft/s):"))
g=32

import math
v=math.sqrt((2*g*h)+(u*u))
finalvelocity=math.sqrt((2*g*h)+(u*u))
print("The velocity with which stone hits the ground is (in ft/s):",math.sqrt((2*g*h)+(u*u)))

#11
x=int(input("Sarah's age:"))
y=int(input("Mark's age:"))
z=int(input("Fatima's age:"))
average= (x+y+z)/3
print("The average age is:",average)

#12
#SOLVING QUADRATIC EQN:
import cmath
a=int(input('Enter The Value Of "a":'))
b=int(input('Enter The Value Of "b":'))
c=int(input('Enter The Value Of "c":'))
#Calculating the discriminant.
dis=((b*b)-(4*a*c))
#Calculating the values of X.
X1=(-b+cmath.sqrt(dis))/2*a
X2=(-b-cmath.sqrt(dis))/2*a
if ((2*a)==0):
    print('Error!,Cannot solve as there is "0" in the denominator')
else:
   print(X1,"\n",X2)

#14
# Airthematic Sequence:
a=int(input("Enter The First Term (a):"))
d=int(input("Enter The Common Difference (d):"))
n=int(input("Enter The No Of Terms (n):"))
# Tn=a+(n-1)*d
print("The ",n,"th Term Of The Sequence Is:",a+(n-1)*d)
ans=input("Want To Continue? Yes or No :")
if(ans=="No"):
    pass
elif(ans=="Yes"):
    n1 = int(input("Enter The No Of Terms(n1):"))
    print("The ",n1,"th Term Of The Sequence Is:", a+(n1-1)*d)

# 15
#COUNTING VOWELS:
print("This program will count total number of vowels from user defined sentence")
string=input("Enter your string:")
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'): #OR if(i in'aeiouAEIOU'):
     vowels=vowels+1
print("Number of vowels are:")
print(vowels)

# 16
# Booliean
north=False
south=True
west=False
east=False
if (north==True)or(south==True)or(east==True)or(west==True):
    print("You can Escape")

# 17
# Sum of fist five Integers
sum=0
for i in range(1,6):
    sum=sum+i
    print(sum)
print(sum)

# 18
# Average
S=23
M=19
F=31

avg=(S+M+F)/3
print(int(avg))

# 19
import math
for i in range(1,5):
     print("for data",i,"")
     length=int(input("length of ladder(ft):"))
     angle=int(input("angle(degree):"))
     # Angle in radian
     radians=((math.pi)*(angle))/180
     height=int(length*math.sin(radians))
     print("Height Reached by Ladder Is:",height,"ft")
     print("")

# IMPORT DATE TIME
import datetime
Dtime=datetime.datetime.now()
print("Current date and time is",Dtime)

# a
import time
print(time.strftime('%A,%B %d %y'))
# b
print(time.strftime('%I:%M %p %Z on %B/%d/%y'))
# c
print(time.strftime('I will meet you on %a %b %d at %I:%M %p'))





# IMPORT MATH
import math
x=54.4
print(math.ceil(x))
print(math.cos(x))
print(math.sin(x))
print(math.floor(x))
print(abs(x))

# Printing Numbers In Matrix Form:
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=" ")
    if i in range(1,6):
        print ("")

print("")
# MATRIX ADDITION:
A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
B=[[2,4,6],
   [1,3,5],
   [7,8,9]]
R=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        R[i][j] = A[i][j]+B[i][j]

print()
for i in R:
    print(i)

print("")
