from flask import Flask, jsonify
import sqlite3
import pandas as pd

################  DB  ################
app = Flask(__name__)
DB_Hotel = "data.db"

def import_csv_to_db(filename):
    df = pd.read_csv(filename)

    conn = sqlite3.connect(DB_Hotel)

    df.to_sql("hotelData", conn, if_exists="replace", index=False)

    conn.close()
    print(f"Importerede {len(df)} rækker fra {filename}")

import_csv_to_db("DataService\hotelData.csv")

conn = sqlite3.connect(DB_Hotel)
print(pd.read_sql_query("SELECT * FROM hotelData", conn))



################  API  ################
@app.route("/data", methods=["GET"])
def get_all():
    conn = sqlite3.connect(DB_Hotel)
    cur = conn.cursor()

    #Hent alle rækker
    cur.execute("SELECT * FROM hotelData;")
    #Henter query svaret fra databasen
    rows = cur.fetchall()

    # Luk databaseforbindelsen
    cur.close()
    conn.close()


    # Returnér som JSON
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 