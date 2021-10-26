#sql requesting in python,
import sqlite3
import pandas

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

for i in rows:
    print(i)

#put in csv
df = pandas.DataFrame.from_records(rows)
df.columns = ["Rank", "Country", "Area", "Population"]
print(df)
df.to_csv("countries_big_area.csv", index=False)

#insert into db
data = pandas.read_csv("ten_more_countries.txt")
conn = sqlite3.connect("database.db")
cur = conn.cursor()
for index,row in data.iterrows():
    print(row["Country"],row["Area"])
    cur.execute("INSERT INTO countries VALUES(NULL,?,?,NULL)",(row["Country"],row["Area"]))
conn.commit()
conn.close()

#files counter
import glob

file_list = glob.glob1("files", "*.py")
print(len(file_list))

#recursive files counter
file_list = glob.glob("files/subdirs/**/*.py", recursive=True)
print(len(file_list))

