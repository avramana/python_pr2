import sqlite3

class DBOperations:
    def __init__(self):
        print("db operations initiated")

    def create_Table(self):
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tb2 (item TEXT,quantity INTEGER,price REAL)")
        conn.commit()
        conn.close()
        print("table created")

    def fetch_Data(self):
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb2")
        rows = cur.fetchall()
        conn.close()
        print("fetched data")
        return rows

    def insert_Data(self,item,quantity,price):
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO tb2 VALUES(?,?,?)",(item,quantity,price))
        conn.commit()
        conn.close()


