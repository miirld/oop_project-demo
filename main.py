import sqlite3
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "qmcskljewfi13oj_wea323klfmfoik"


@app.route("/")
def index():
    data = get_db()
    return render_template("index.html", all_data = data)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('oop-demo.db')
        cursor = db.cursor()
        cursor.execute("select * from graduates")
        all_data = cursor.fetchall()
    return all_data

#это написала Владаbbbb
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
