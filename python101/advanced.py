from datetime import datetime
print(datetime.now().strftime("Today is %A, %B %d, %Y")) #-> Today is Monday, May 11, 2020; strftime (string from time)

#get year from datetime
age = input("How old are you?: ")
year = datetime.now().year - int(age)
print("U were born in %i year " %year)

#passwds generator
import random
chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?!@#$%^&*()?"
chosen = random.sample(chars,6)
passwd = "".join(chosen) #-> paste list into string
print(passwd)

#passwd checker
while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)


#jupiter distance
import ephem
jupiter = ephem.Jupiter()
jupiter.compute('1230/1/1')
distance_au_units = jupiter.sun_distance
distance_km = distance_au_units * 149597870.691
print(distance_km)

#screen info
"""
from screeninfo import get_monitors

width = get_monitors()[0].width
height = get_monitors()[0].height

print("Width: %s,  Height: %s" % (width, height))
"""

#pyglet
"""
import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label('Hello world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center',
                          anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
"""

#data strip
with open("countries_raw.txt", "r") as file:
    content = file.readlines()

content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i !=""]
content = [i for i in content if i != "Top of Page"]
content = [i for i in content if len(i) != 1]

print(content)

with open("countries_clean.txt", "w") as file:
    for i in content:
        file.write(i+"\n")


#data checker
checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries_clean.txt", "r") as file:
    content = file.readlines()

content = [i.rstrip('\n') for i in content]
checked = [i for i in content if i in checklist]

print(checked)


#sort and add to file
checklist_2 = ["Portugal", "Germany", "Spain"]
checklist_2 = [i + "\n" for i in checklist]

with open("countries_missing.txt", "r") as file:
    content_2 = file.readlines()

updated_list = sorted(checklist_2 + content)

with open("countries_added.txt", "w") as file:
    for i in updated_list:
        file.write(i)

#use pandas to read csv
import pandas
data = pandas.read_csv("countries_by_area.txt")
data["density"] = data["population_2013"]/data["area_sqkm"]
data = data.sort_values(by="density",ascending=False)

for i,row in data[:5].iterrows():
    print(row["country"])

