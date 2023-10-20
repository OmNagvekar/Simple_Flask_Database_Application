from flask import Flask, redirect, url_for, request, render_template
import mysql.connector
app = Flask(__name__)

# Replace with your MySQL database credentials
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'register',
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                prn VARCHAR(10),
                class VARCHAR(20),
                email VARCHAR(255),
                phone_no VARCHAR(10)
            )''')

@app.route('/view')
def view_students():
    # Fetch data from the database
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('view_students.html', students=students)


@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':
      name = request.form['name']
      prn = request.form['prn']
      email = request.form['email']
      class_ = request.form['class']
      phone_no = request.form['phone_no']
      # Insert data into the database
      cursor.execute("INSERT INTO students (name, prn, class, email, phone_no) VALUES (%s, %s, %s, %s, %s)",(name, prn, class_, email, phone_no))
      conn.commit()
      return redirect(url_for('view_students'))

@app.route('/')
def index():
   cursor.execute("SELECT * FROM students")
   students = cursor.fetchall()
   return render_template('index.html',students =students)


if __name__ == '__main__':
   app.run(debug = True)
   #app.run(debug = True,host="192.168.36.48")