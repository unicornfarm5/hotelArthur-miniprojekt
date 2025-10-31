import sqlite3
import pandas as pd

df = pd.read_excel("data.xlsx")

conn = sqlite3.connect("data.db")
df.to_sql("records", conn, if_exists="replace", index=False)


##unktion der printer hele databasen bare for at teste at det virker
def printData():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#printData() #der er 1000 rækker så ikke print den hele for sjov bby

