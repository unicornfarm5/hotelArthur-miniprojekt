from flask import Flask, jsonify
import sqlite3
import pandas as pd

################  DB  ################
app = Flask(__name__)
from pathlib import Path

DB_Hotel = Path(__file__).parent / "data.db" #for at databasen laves i denne mappe


def import_excel_to_db(filename):
    df = pd.read_excel(filename, engine="openpyxl")
    conn = sqlite3.connect(DB_Hotel)
    df.to_sql("hotelData", conn, if_exists="replace", index=False)
    conn.close()

    print(f"Importerede {len(df)} rækker fra {filename}")

if not DB_Hotel.exists():
    import_excel_to_db("data.xlsx")

conn = sqlite3.connect(DB_Hotel)
print(pd.read_sql_query("SELECT * FROM hotelData", conn))



################  API  ################
@app.route("/data", methods=["GET"])
def get_all():
        #ide fra chatGPT 
    with sqlite3.connect(DB_Hotel) as conn:
        df = pd.read_sql_query("SELECT * FROM hotelData;", conn)
    return df.to_json(orient="records")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 