from flask import Blueprint, render_template, url_for, redirect, request
import pymysql.cursors
import json
from instance.connection import *

# inintailze
router_student = Blueprint('student_template', __name__)
title_text = 'Pyhton3 Flask Development'
topic_text = 'สอนเขียนเว็บด้วย Python3 Flask'

# routes
@router_student.route('/')
def get_student():
    with conn.cursor() as cur:
        sql = "SELECT * FROM student"
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('student/show.html', title=title_text, topic=topic_text, rows=rows)


@router_student.route('/profile/<sid>', methods=['GET'])
def profile(sid):
    with conn.cursor() as cur:
        sql = "SELECT * FROM student WHERE sid=%s"
        cur.execute(sql, (sid))
        row_data = cur.fetchone()
    return json.dumps(row_data)


@router_student.route("/add", methods=['GET'])
def add_student():
    return render_template('student/add.html', title=title_text, topic=topic_text)


@router_student.route("/save", methods=["POST"])
def save_student():
    sfname = request.form['sfname']
    slname = request.form['slname']
    sage = request.form['sage']

    with conn.cursor() as cur:
        sql = "INSERT INTO  student VALUES(null, %s,%s,%s)"
        cur.execute(sql, (sfname, slname, sage))
        conn.commit()
    # show is function name for redirect
    return redirect(url_for("get_student"))


@router_student.route("/delete/<id>")
def delete_student(id):
    with conn.cursor() as cur:
        sql = "DELETE FROM student WHERE sid=%s"
        cur.execute(sql, (id))
        conn.commit()
    # show is function name for redirect
    return redirect(url_for("get_student"))


@router_student.route("/edit/<id>")
def edit_student(id):
    with conn.cursor() as cur:
        sql = "SELECT * FROM student WHERE sid=%s"
        cur.execute(sql, (id))
        row_data = cur.fetchone()
    return render_template('student/edit.html', title=title_text, topic=topic_text, row=row_data)


@app.route("/update", methods=["POST"])
def update_student():
    sid = request.form['sid']
    sfname = request.form['sfname']
    slname = request.form['slname']
    sage = request.form['sage']

    with conn.cursor() as cur:
        sql = "UPDATE student SET sfname=%s, slname=%s, sage=%s WHERE sid=%s"
        cur.execute(sql, (sfname, slname, sage, sid))
        conn.commit()
    # show is function name for redirect
    return redirect(url_for("get_student"))
