# SETS
# cannot contain lists and other sets(hashable)
# EMPTY SET:
thisset=set()

# ADDING ELEMENTS TO A SET:
#adds at any random index in a set(unordered)

# Add (Single element addition)
x=thisset.add("orange")
print(thisset)

# Update(multiple element addition)
thisset.update(["cherry","apple","banana"])
print(thisset)

# REMOVING ELEMENTS FROM A SET:

# remove(deletes specified element)
# (will produce error if the element is not present in set):
thisset.remove("apple")
print(thisset)

# discard(deletes specified element)
# (will not produce error if the element is not present in set):
thisset.discard("strawberry")
print(thisset)

# pop(removes any random item from the set)
thisset.pop()
print(thisset)

# clear(empty the list)
thisset.clear()
print(thisset)

# delete(empty the list as well as delete the structure)
del(thisset)


# SET FUNCTIONS:

s1=set()
s2=set()
for i in range(10):
    s1.add(i)
print("s1=",s1)
for i in range(3,12):
    s2.add(i)
print("s2=",s2)

# UNION:
union=s1.union(s2)
# OR
# union=s1|s2
print("union of s1 and s2 is:",union)

# INTERSECTION:
intersecton=s1.intersection(s2)
# OR
# intersecton=s1&s2
print("intersecton of s1 and s2 is:",intersecton)

# DIFFERENCE:
diff=s1.difference(s2)
# OR
# diff=s1-s2
print("difference of s1 and s2 is:",diff)

# SYMMETRIC DIFFERENCE
# (keep those elements only which are not present in both sets)
symm=s1.symmetric_difference(s2)
# OR
# symm=s1^s2
print("symmetric difference of s1 and s2 is:",symm)

# PROPER SUBSET,SUBSET AND SUPER SET:
if s1>s2:
    print("s1 is superset")
elif s1<s2:
    print("s1 is proper subset of s2")
elif s1<=s2:
    print("s1 is subset of s2")
else:
    print("s1 and s2 are same sets")

# PRACTICE:
#1
s=set()
n=int(input("Enter No Of Dishes You Want To Input:"))
print("BEST DISHES")
for i in range(1,n+1):
    print("Enter Your Best Dish",i,":")
    dish=(input())
    s.add(dish)
print(s)
for i in range(len(s)):
    y=s.pop()
print(s)

print()

# 2
s=set()
print("Best Five Student's Name")
for i in range(1,6):
    print("Student",i,"Name:")
    x=[input()]
    s.update(x)
print(s)
