import sqlite3
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "qmcskljewfi13oj_wea323klfmfoik"


@app.route("/", methods=['post', 'get'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')  # запрос к данным формы
        biography = request.form.get('biography')
        if name != '' and biography != '':
            message = "Выпускник добавлен"
            db = sqlite3.connect('database/oop_demo.db')
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO graduates VALUES (?, ?)", (name, biography))
            db.commit()
            print('New graduate in the database:')
    return render_template("index_vlada.html")


@app.route("/<letter>")
def letters(letter):
    data = get_db(letter)
    return render_template("letter.html", all_data=data, letter=letter)


def get_db(letter):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database/oop_demo.db')
        cursor = db.cursor()
        cursor.execute("select * from graduates")
        raw_data = cursor.fetchall()
        all_data = [idx for idx in raw_data if idx[0].lower().startswith(letter.lower())]
        all_data.sort()
    return all_data



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
