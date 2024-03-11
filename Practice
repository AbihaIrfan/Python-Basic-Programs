# max no in array
arr=[10,2,12, 4,1,7,9]

for i in range (0, len(arr)-1):
    if arr[i]>arr[i+1]:
        arr[i], arr[i+1]=arr[i+1], arr[i]

print(arr[-1])


#factorial (recursive)
def fact(no):
    if no==1 or no==0:
        return 1

    return no*fact(no-1)

print(fact(4))

#factorial (iterative)
def facto(no):
    factorial=1
    for i in range (no,0, -1):
        factorial*=i
    return factorial

print(facto(4))

# string=LETTERS repeated alph print na kry
def noRepeat(string):
    seen_chars = []  # An empty list to keep track of seen characters
    result = ""  # An empty string to store the unique characters in order

    for char in string:
        if char not in seen_chars:
            seen_chars.append(char)  # Add the character to the list of seen characters
            result += char  # Add the character to the result string
        elif char in result:
            result = result.replace(char, '')  # Remove any repeated occurrences of the character from the result
    return result

print(noRepeat("LETTERS"))


# anagrams
s1= "liste"
s2="silent"
def sort_string(word):
    string= list(word)
    for i in range(len(string)-1):
        if string[i]>string[i+1]:
            string[i], string[i+1]= string[i+1], string[i]
    return ''.join(string)

if (sort_string(s1.lower())==sort_string(s2.lower())):
    print (f"{s1} and {s2} are anagrams")
else:
    print(f"{s1} and {s2} are not anagrams")

# arr= 1,3,5,7,9 even num agr req kia hai tou closed odd no dy. 20 req kia hai tou wo 19 dy e.g. 369
arr = [1, 3, 5, 7, 9]

try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

if user_input % 2 == 0:
    closest_odd = None
    min_difference = float('inf')

    for num in arr:
        if num % 2 == 1:
            difference = abs(user_input - num)
            if difference < min_difference:
                min_difference = difference
                closest_odd = num

    if closest_odd is not None:
        print(f"The closest odd number to {user_input} in the array is {closest_odd}.")
    else:
        print("There are no odd numbers in the array.")
else:
    print("The user input is not even.")

# dict ki values count kkrni thi
my_dict = {'a': 2, 'b': 3, 'c': 4}
sum=0
for x,y in my_dict.items():
    sum+=y

print(sum)

# prior datetime
from datetime import datetime, timedelta

# Assuming you have a datetime object
current_datetime = datetime.now()

# Calculate the prior datetime, for example, 1 day ago
prior_datetime = current_datetime - timedelta(days=20)

print("Current datetime:", current_datetime)
print("Prior datetime:", prior_datetime)



original_string = "Hello, World!"
char_to_remove = ","

# Removing the specified character using list comprehension
modified_string = "".join([char for char in original_string if char != char_to_remove])

print("Original String:", original_string)
print("Modified String:", modified_string)


# palindrome
word= "madam"
rev=""
for i in range(len(word)-1, -1, -1):
    rev+=word[i]

if word==rev:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")


# CATEGORIZING
date_list = [[25, 'Jan', 2022], [24, 'Jan', 2022], [20, 'Feb', 2022]]

result_dict = {}

for date in date_list:
    month_year = (date[1], date[2])
    if month_year in result_dict:
        result_dict[month_year].append(date)
    else:
        result_dict[month_year] = [date]

print(result_dict)
