# List Functions

# Seq(Converts any sequence to lists)
s='Hello world'
p=1,2,3,4
print(list(s))
print(list(p))

#  Extends sequence to the list
s="Hello World"
l=[1,2,3,4]
l.extend(s)
print(l)

# Indexing
pets=["dog","cat","ferrat","piegon"]
print(pets[::])
print(pets[::-1])
print(pets[0:4:2])

# Append(adds at the end of list)
pets.append("rabbit")
print(pets)

# Insert(inserting element at a paritcular index)
(pets.insert(0,"puppy"))
print(pets)

# Extend(inserts a whole list at the end of the existing list)
(pets.extend(["cat","dog"]))
print(pets)

# Count(count the specified element)

# 1
print(pets.count("dog"))

# 2
grades=['B','B','F','C','B','A','A','D','C','D','A','A','B','D']
l2=[grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('E'),grades.count('F')]
print(l2)

# Remove(remove the specified element from the list)
(pets.remove("cat"))
print(pets)

# Pop(removes the last item of list)
(pets.pop())
print(pets)
(pets.pop(2))
print(pets)

# Reverse(reverses the list)
(pets.reverse())
print(pets)

# Index
print(pets[2])

# Clear(Clear the whole list but the structure will be there)
(pets.clear())
print(pets)

# Delete(delete list+structure)
del pets

# SWAPPING OR SORTING
# 1
l1=[6,3,25,1,90,9,7,100,95]
for i in range(len(l1)-1):
    for j in range(len(l1)-1):
        if l1[j]>l1[j+1]:
            t=l1[j+1]
            l1[j+1]=l1[j]
            l1[j]=t
    print(l1)

    # OR
l1=[6,3,25,1,90,9,7,100,95]
l1.sort()
print(l1)

# 2
g=[9,7,7,10,3,9,6,6,2]
for i in range(len(g)-1):
    for j in range(len(g)-1):
       if g[j]>g[j+1]:
        temp=g[j+1]
        g[j+1]=g[j]
        g[j]=temp
    print(g)

# NESTING OF A LIST:
# MATRIX FROM USER INPUT:

x=[]
for i in range(3):
    print("Enter Elements for",i,"Row:")
    y=[]
    for j in range(3):
        y.append(int(input()))
    x.append(y)
print()
for i in x:
    print(i)

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
# print(R)
print()
for i in R:
    print(i)

# Matrix Multiplication
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
    for j in range(len(B[0])):
        for k in range(len(B)):
            R[i][j] += A[i][k] * B[k][j]
print()
for i in R:
    print(i)

print("\n")


# Practice
# 1
l=[]
n=int(input("Enter no of integers you want to input:"))
for i in range(1,n+1):
    print("Enter Integer",i,":")
    x=int(input())
    l.append(x)
print(l)
print("")
#a and b(middle element and its index)
if len(l)%2==0:
    import math
    m= math.ceil(len(l)/2)
    print(l[m])
    print(l.index(l[m]))
else:
    m=int(len(l)/2)
    print(l[m])
    print(l.index(l[m]))

print("")

# c
print("Sorting Of List In Descending Order")
l.sort(reverse=True)
print(l)
print("")

# d (removes 1st item and puts it at the end)
x=l.pop(0)
print(l)
y=l.append(x)
print(l)

print("")

# 2
l=[]
for i in range(5):
    print("Enter floating point number",i,"")
    x=float(input())
    l.append(x)
print(l)
print()
sum=sum(l)
print("sum=",sum)
print()
avg=sum/len(l)
print("avg=",avg)
print()
print("max=",max(l))
print()
print("min=",min(l))

#
print("Sorting Of List In Descending Order")
for i in range(len(l)-1):
    for j in range(len(l)-1):
         if l[j+1]>l[j]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
    print(l)

