#OPERATORS

#MATHEMATICAL OPERATORS
# Sum
a= 10
b = 22
print ("Sum is:", a+b)
# Subtract
a=10
b=22
print ("Difference is", a-b)
# Multiplication
a=10
b=22
print ("Product is:", a*b)
# Division (Ans in FLoat)
a=10
b=22
print ("Division is:",a/b)
# Integer Division (Ans in int)
a=10
b=22
print ("Integer Division is:" , a//b)
# Notation (A to the Power B i.e.a^b)
a=10
b=22
print ("Raised to the Power is:", a**b)
# Modulus (remainder i.e. 2/2 R=0 or 3/2 R=1)
a=10
b=22
print ("Remainder is:", a%b)

#MEMBERSHIP OPERATORS (Ans in True or False)
# Not In
x = ["wasim", "lubaid", "shahroz", "usman", "faisal", "farhan"]
print("parkash" not in x)
# In
x = ["wasim", "lubaid", "shahroz", "usman", "faisal", "farhan"]
print("faisal" in x)

print("")

#IDENTITY OPERATOR (True/False)
# is not
x = ["ahmed", "bashir"]
y = ["ahmed", "bashir"]
z = x
print(x is not z)
print(x is not y)
print(x!=y)
# is
print(x is z)
print(x is y)
print(x == y)

print("")
#LOGICAL OPERATOR (True/False)
# And (If both are True Then it is true)
x = 15
print(x > 14 and x < 20)
# Or (If both are False then it is False)(True if any one is True)
x = 25
print(x >23 or x < 24)
#Not (Negation)
x = 35
print(not(x > 33 and x < 40))

# COMPARISON OPERATOR
# <
x = 20
y = 15
print("X is Less than Y:",x < y)
# <=
x = 20
y = 15
print("X is Less than or equal to Y:",x <= y)
# >
x = 20
y = 15
print("X is Greater than Y:",x > y)
# >=
x = 20
y = 15
print("X is Greater than or equal to Y:",x >= y)
# ==
x = 20
y = 15
print("X is equal to Y:", x == y)
# =!
x = 20
y = 15
print("X is not equal to Y:", x != y)


#ASSIGNMENT OPERATORS
# +
x = 5
x += 3
print(x)
# -
x = 5
x -= 3
print(x)
# *
x = 5
x *=3
print(x)
# /
x = 5
x /= 3
print(x)
# %
x = 5
x %= 3
print(x)
# //
x = 5
x //= 3
print(x)
# **
x = 5
x **= 3
print(x)

print("")
# BITWISE OPERATORS

# Bitwise And
x = 5
x &= 3
print(x)
# Bitwise Or
x = 5
x |= 3
print(x)
# Bitwise XOR
x = 5
x ^= 3
print(x)
# Shift Right
x = 5
x >>= 3
print(x)
# Shift Left
x = 5
x <<= 3
print(x)




#IN AND NOT IN
x = "Good Morning To Everyone In Class,Sec A "
for i in x:
    if i in 'aeiouAEIOU':
        print(i)

x = "Good Morning To Everyone In Class,Sec A "
for i in x:
    if i in 'aeiouAEIOU':
        print(i, "\t", x.index(i))

x = "Good Morning To Everyone In Class,Sec A "
for i in x:
    if i not in 'aeiouAEIOU':
        print(i, "\t", x.index(i))
