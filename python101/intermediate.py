#import string
print(type("Hey".replace("ey","i")[-1]))

#just dont wanna typing this one
#firstname = input("Enter first name: ")
#secondname = input("Enter second name: ")
#print("Your first name is %s and your second name is %s" % (firstname, secondname))

d = {   "employees":[{"firstName": "John", "lastName": "Doe"},
            {"firstName": "Anna", "lastName": "Smith"},
            {"firstName": "Peter", "lastName": "Jones"}],
        "owners":[{"firstName": "Jack", "lastName": "Petter"},
            {"firstName": "Jessy", "lastName": "Petter"}]}
d['employees'].append({"firstName": "Albert","lastName": "Einstein" }) ## also works -> d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
d['employees'][3]['lastName'] = "Ajnsztajn"
print(d['employees'][3]['lastName'])

#json write read and append
import json
def dict_to_json(filepath,dictD):
    with open(filepath, "w") as file:
        json.dump(dictD, file, indent=4) # ident 4 means 4 spaces
dict_to_json('dict.json', d)

def append_to_json(filepath):
    with open(filepath, 'r+') as file:
        d = json.loads(file.read())
        d["employees"].append({"firstName":"Ernie", "lastName":"Ernie"})
        file.seek(0)
        json.dump(d,file,indent=4,sort_keys=True)
        file.truncate()
append_to_json('dict.json')

from pprint import pprint
def read_from_json(filepath):
    with open(filepath, "r") as file:
        d = json.loads(file.read())
pprint(d)

a = [1,2,3]
for i,x in enumerate(a):
    print("Item %s has index %s" % (x, i)) # -> i index; x items

#while loops
import time
i=0
while True:# -> this one is infinity
    i = i+1
    #time.sleep(i)
    if i == 5:
        print("End of loop")
        break
    print("Hello world!")

while True:
    print("Hello")
    if 2 > 1:
        print("Hi")
        break

i=0
while i<5:
    i = i+1
    print("Hello")
    if 2 > 1:
        continue
    print("Hi")

#try except
d = dict(weather = "clima", earth = "terra", rain = "chuva")
var = input("Enter word: ")
var = var.lower()
try:
    print(d[var])
except:
    print("No word %s in dictionary" %var)

#connect with https
import requests #installed by pip
response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
text = response.text
print(text)
print(text.count("a")) #how many a in string

#return web browser searching engine
import webbrowser
query = input("Your query:")
webbrowser.open("https://google.com/search?q=%s" %query)
webbrowser.get()



#read as table[csv] from text file with pandas
import pandas
data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("sample.txt")
data_12 = pandas.concat([data1,data2])
data_12.to_csv("sample12.txt", index = None)

#and in a classic way
import io
import pandas
import requests

r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
c = r.content
data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
data2 = pandas.read_csv("sample.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sample.txt", index=None)

#plot data
import pandas
import pylab as plt

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter') #scatter or bar or line etc.
plt.show()

## and in a different way
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

output_file("bokeh_plot.html")
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
f = figure()
f.circle(x=data["x"], y=data["y"])

show(f)