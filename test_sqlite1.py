import sqlite3 as lite
import sys


def saveData(l_name, l_age):
    con = lite.connect('phones.db')
    cur = con.cursor()
    # смонтируем таблицу...
    cur.execute("""CREATE TABLE IF NOT EXISTS phones(
      id INT PRIMARY KEY,
      name TEXT,
      price float,
      info TEXT)
     """)
    # cur.execute('SELECT * FROM lovers')
    # idx = len(cur.fetchall())
    # cur.execute('INSERT INTO lovers(id, name, age) VALUES(?, ?, ?)', (idx, l_name, l_age, l_town))
    con.commit()
    con.close()
saveData("Ivanoff",77)