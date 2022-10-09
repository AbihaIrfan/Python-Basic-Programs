# TUPLES

# Empty Tuple
t=tuple()

# Nested Tuple
x=((0,1,2,3),("python","geek"))
print(x)

# Change in Tuples:
# No Changes as it is immutable and there are no pre-defined functions for it

# Converting List into Tuple:
l=[1,2,3,4,5]
print(tuple(l))

# Changes In Tuple:
# First Convert Tuple into List:
x=("apple","cherry","banana")
y=list(x)
print(y)
# Make Chnages:
y[1]="kiwi"
# Again Convert List Into Tuple:
x=tuple(y)
print(x)

# 2
t=(1,2,3,4)
l1=list(t)
l1.append(10)
l1.insert(0,12)
t=tuple(l)
print(t)
