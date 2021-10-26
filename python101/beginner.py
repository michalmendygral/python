#https://dbschenker-tsc.udemy.com/course/python-video-workbook/
#list elements
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# [start:end:step]
print(letters[1]) # -> a
print(letters[3:6]) # -> d e f
print(letters[:3]) # -> a b c
print(letters[-2]) # -> i
print(letters[-3:]) # -> h i j
print(letters[::2]) # -> a c e g i
print(list(range(1, 21))) # -> list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#range and value mapping
my_range = range(1, 21)
print([x*10 for x in my_range]) # -> [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
print(list(map(str, my_range))) # -> ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

#remove duplicates
a = ["1", 1, "1", 2]
print(set(a)) # -> {1, 2, '1'} remove duplicates

#dictionary
d = {"a": 1, "b": 2, "c": 3}
dDict = dict(a = 1, b = 2) # dict is mostly used to convert other objects to a dictionary.
print(d['b']) # -> 2
print(d['b'] + d['a']) # -> 3

d = {"Name": "John", "Surname": "Smith"}
print(d["Surname"])
print(d.items())

d2 = {"a": 1, "b": 2}
d2["c"] = 3
print(d2) # -> {'a': 1, 'b': 2, 'c': 3}
print(d2.values()) # -> dict_values([1, 2, 3])
print(sum(d2.values())) # -> 6

from pprint import pprint
d3 = {"a": list(range(1, 11)), "b": list(range(11, 21)), "c": list(range(21, 31))}
pprint(d3) # -> {'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
           # ->  'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
           # ->  'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}
print(d3['b'][2]) # -> 13
print(d3.items()) # ->dict_items([('a', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), ('b', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), ('c', [21, 22, 23, 24, 25, 26, 27, 28, 29, 30])])
for key,value in d3.items():
    print(key, "has value ", value) # -> a has value  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                    # -> b has value  [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
                                    # -> c has value  [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

import string
for letter in string.ascii_lowercase:
    print(letter, end=' ') # -> a b c d e f g h i j k l m n o p q r s t u v w x y z
