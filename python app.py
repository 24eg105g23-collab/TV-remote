from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# create database
def get_db():
    conn = sqlite3.connect("students.db")
    return conn

@app.route("/")
def home():
    return "Student Backend is Running"

# add student
@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    roll = request.form["roll"]

    conn = get_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (name TEXT, roll TEXT)")
    cur.execute("INSERT INTO student VALUES (?,?)", (name, roll))
    conn.commit()
    conn.close()

    return "Student Added Successfully"

# view students
@app.route("/students")
def view_students():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    conn.close()

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
