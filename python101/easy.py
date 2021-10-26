for i in range(1,11):
    print(i, end=' ') # -> 1 2 3 4 5 6 7 8 9 10
print()

#function
def acceleration(v1,v2,t1,t2):
    a = (v2 - v1) / (t2 - t1)
    return a
print(acceleration(0,10,0,20)) # -> 0,5


def foo(a, b):
    return a + b
print(foo(2, 3) * 10)

from math import pi
def volume(h, r = 10):
    liquid_volume = (4*pi*r**3)/3 - (pi*h**2*(3*r-h))/3
    return liquid_volume
print(volume(2)) # -> 4071.5040790523717

#default parameters are always first
def foo(b, a=2):
    return a*b
print(foo(3,3)) # -> 9

#local variable
c = 1
def foo():
    c = 2
    return c
c = 3
print(foo()) # -> 2

#global variable
def foo():
    global c
    c = 1
    return c
foo()
print(c)

#len function
string = "jakis string przykladowy do policzenia slow"
def lenght_function(str):
    return len(string.split())
print(lenght_function(string))

#file reading words.txt
def count_words(filepath):
    with open(filepath) as file:
        string = file.read()
        string_list = string.split()
        return len(string_list)
print(count_words("words.txt"))

#file reading words2.txt
def count_each_word(filepath):
    with open(filepath) as file:
        string = file.read()
        string_replaced = string.replace(","," ")
        print(string_replaced)
        string_list = string_replaced.split()
        return len(string_list)
print(count_each_word("words2.txt"))

#re module means ",| " to replace commas with spaces
import re
def count_words_re(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    string_list = re.split(",| ", text)
    return len(string_list)
print(count_words_re("words2.txt"))

#math
import math
dir(math) # to list all available functions
print(math.sqrt(9))
print(math.cos(1))
#help(math.pow) to know how function works
print(math.pow(2,2))

#file writing
import string
def aplhabet_to_file(filepath):
    with open(filepath, 'w') as file:
        for letter in string.ascii_lowercase:
            file.write(letter + "\n")
aplhabet_to_file("alphabet.txt")

#zip, tuple
a = [1, 2, 3]
b = (4, 5, 6)
for i,j in zip(a,b):
    print(i,j , end=' ') # zip means two-dimensional list
print(tuple(zip(a,b))) # -> needs to be tuple to show readable version

#multiple sequences ->
ad__ = string.ascii_lowercase[0::3]
be__ = string.ascii_lowercase[1::3]
cf__ = string.ascii_lowercase[2::3]

with open("letters.txt", "w") as file:
    for x, y, z in zip(ad__, be__, cf__):
        file.write(x + y + z+"\n")
    file.write("y"+"z"+"\n")

#letter per file
import string, os
if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_lowercase:
    with open("letters/" + letter + ".txt", "w") as file:
        file.write(letter+"\n")

#read from multiple file
import glob
letters = []
file_list = glob.glob("letters/*.txt")
file_list.sort()
for filename in file_list:
    with open(filename,"r") as file:
        letters.append(file.read().strip("\n"))
print(letters)

#read from multiple file
import glob
letters = []
file_list = glob.glob("letters/*.txt")
file_list.sort()
python_string = "python"
for filename in file_list:
    with open(filename,"r") as file:
        letter = file.read().strip("\n")
    if letter in python_string:
        letters.append(letter)
print(letters)

#input in python
password = input("Enter the password: ")

age = int(input("What's your age? "))
age_last_year = age - 1
print("Last year you were %s." %age_last_year)
