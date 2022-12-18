import sqlite3
from Scripts import parser

db = sqlite3.connect('oop-demo.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS graduates(
    name TEXT,
    biography TEXT
) """)
db.commit()

graduates = parser.parsing()

for graduate in graduates:
    sql.execute(f'SELECT name FROM graduates WHERE name = "{graduate}"')
    if sql.fetchone() is None:
        print('New graduate in the database:', graduate)
        sql.execute(f"INSERT INTO graduates VALUES (?, ?)", (graduate, graduates[graduate]))
        db.commit()





