import sqlite3
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "qmcskljewfi13oj_wea323klfmfoik"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<letter>")
def letters(letter):
    data = get_db(letter)
    return render_template("letter.html", all_data=data, letter=letter)


def get_db(letter):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('oop-demo.db')
        cursor = db.cursor()
        cursor.execute("select * from graduates")
        raw_data = cursor.fetchall()
        all_data = [idx for idx in raw_data if idx[0].lower().startswith(letter.lower())]
    return all_data


# это написала Владаbbbb
# это написал Миша....
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
