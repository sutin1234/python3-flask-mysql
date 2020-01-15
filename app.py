from flask import Flask, redirect, request, render_template, url_for
import pymysql.cursors
import json
from instance.config import APP_CONFIG  # load configuration file

app = Flask(__name__)
app.config.from_object(APP_CONFIG)

title_text = 'Pyhton3 Flask Development'
topic_text = 'สอนเขียนเว็บด้วย Python3 Flask'

conn = pymysql.connect(
    host=app.config["DB_HOST"],
    user=app.config["DB_USER"],
    password=app.config["DB_PASSWORD"],
    db=app.config["DB_NAME"],
    charset=app.config['CHARSET'])


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html', title=title_text, topic=topic_text)


@app.route('/student/profile/<sid>', methods=['GET'])
def profile(sid):
    with conn.cursor() as cur:
        sql = "SELECT * FROM student WHERE sid=%s"
        cur.execute(sql, (sid))
        row_data = cur.fetchone()
    return json.dumps(row_data)


@app.route("/student", methods=['GET'])
def show():
    with conn.cursor() as cur:
        sql = "SELECT * FROM student"
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('show.html', title=title_text, topic=topic_text, rows=rows)


@app.route("/student/add", methods=['GET'])
def add_student():
    return render_template('add.html', title=title_text, topic=topic_text)


@app.route("/student/save", methods=["POST"])
def save_student():
    sfname = request.form['sfname']
    slname = request.form['slname']
    sage = request.form['sage']

    with conn.cursor() as cur:
        sql = "INSERT INTO  student VALUES(null, %s,%s,%s)"
        cur.execute(sql, (sfname, slname, sage))
        conn.commit()
    return redirect(url_for("show"))  # show is function name for redirect


@app.route("/student/delete/<id>")
def delete_student(id):
    with conn.cursor() as cur:
        sql = "DELETE FROM student WHERE sid=%s"
        cur.execute(sql, (id))
        conn.commit()
    return redirect(url_for("show"))  # show is function name for redirect


@app.route("/student/edit/<id>")
def edit_student(id):
    with conn.cursor() as cur:
        sql = "SELECT * FROM student WHERE sid=%s"
        cur.execute(sql, (id))
        row_data = cur.fetchone()
    return render_template('edit.html', title=title_text, topic=topic_text, row=row_data)


@app.route("/student/update", methods=["POST"])
def update_student():
    sid = request.form['sid']
    sfname = request.form['sfname']
    slname = request.form['slname']
    sage = request.form['sage']

    with conn.cursor() as cur:
        sql = "UPDATE student SET sfname=%s, slname=%s, sage=%s WHERE sid=%s"
        cur.execute(sql, (sfname, slname, sage, sid))
        conn.commit()
    return redirect(url_for("show"))  # show is function name for redirect


if __name__ == '__main__':
    app.run()


# FLASK_APP=app.py FLASK_DEBUG=1 flask run
