# DICTIONARIES:

d={"name":"Sara",
   "address":"Karachi",
   "email":"sara@gmail.com",
   "phone":"78945"}

# Adding Elements To A Dictionary
d["GPA"]=3.5
d["Hobbies"]=['research','coding']
d["Gender"]="female"
print(d)

# KEY,VALUES AND ITEMS:
print()
print("Keys")
for i in d.keys():
    print(i)
print()

print("Values")
for i in d.values():
    print(i)
print()

print("Items")
for x,y in d.items():
    print(x,":",y)

# Creating Dictionary From List:
# 1
d={}   #or d=dict()
l=["Grocery","Fruits","Vegetables"]
for i in range(len(l)):
    m=l.pop()
    print("Enter",m,":")
    d[m]=str(input())
print(d)

#2
d=dict()
item=["Bread","Butter","Jam","Chocolate"]
for i in range(len(item)):
    x=item.pop()
    print("Enter price for",x,":")
    d[x]=int(input())
print(d)
# or
for k,y in d.items():
    print(k,":",y)


#3
dict = {'Name' : 'Jibran', 'Age': 12, 'Class':'Sixth', 'DOB':'16 April2006'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
print("dict['DOB']: ", dict['DOB'])
print("dict['Class']:", dict['Class'])

print("\n")

# NESTED DICTIONARIES:
# 1 FAMILY TREE
print("FAMILY TREE")
family={"Father":{"Name":"Alay Irfan","Occupation":"Electrical Engineer"},
        "Mother":{"Name":"Kanwal Fatima","Occupation":"House Wife"},
        "Sibiling_1":{"Name":"Sidra Fatima","Occupation":"Electronic Engineer"},
        "Sibiling_2":{"Name":"Farwa Fatima","Occupation":"Computer Scientist"},
        "Sibiling_3":{"Name":"Batool Fatima","Occupation":"Fashion Designer"}}
for i,j in family.items():
    x=print(i,":",j)

paternal={"Paternal Grand Father":{"Name":"Alay Imran"},
          "Paternal Grand Mother":{"Name":"Rubab"},
          "Paternal Aunt_1":{"Name":"Abida"},
          "Paternal Aunt_2":{"Name":"Shahida"}}
family.update(paternal)

maternal={"Maternal Grand Father":{"Name":"Ali Haider"},
          "Maternal Grand Mother":{"Name":"Nasreen"},
          "Maternal Uncle":{"Name":"Hassan"}}
family.update(maternal)


print("\n")
for k,l in family.items():
    print(k,":",l)

# 2
faculty={1:{"Name":"Sara","Address":"Karachi","Email":"sara@gmail.com","Designation":"Ass.Proffesor","Salary":"100000","Dept":"SE"},
         2:{"Name":"Faizan","Address":"Lahore","Email":"faizan@gmail.com","Designation":"Lecturer","Salary":"50000","Dept":"CIS"},
         3:{"Name":"Najmi","Address":"Islamabad","Email":"najmi@gmail.com","Designation":"Professor","Salary":"300000","Dept":"SE"}}

for k,y in faculty.items():
    print(k,":",y)

def phone_directory(no):
    phone_book={}
    for i in range(no):
        name=str(input("Enter name:")).title()
        phone_num=int(input("Enter number:"))
        print()
        phone_book[name]=phone_num
    return phone_book

num=int(input("Enter how many numbers you want to enter:"))
phone_book= phone_directory(num)
print(phone_book)

def delete(book,no_1,):
    for i in range(no_1):
        name_1=str(input("Enter name you want to delete:")).title()
        if name_1 in book.keys():
            book.pop(name_1)
        else:
            print("Number not in the phonebook")
    return book

num_1=int(input("How many numbers you want to delete:"))
del_num= delete(phone_book,num_1)
print("Members in Phone Directory after deleting are:")
print(del_num)

print("Total number of members in phone book are:",end="")
total=len(del_num)
print(total)
