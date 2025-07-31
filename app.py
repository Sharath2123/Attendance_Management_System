from flask import Flask,render_template,request,redirect
from flask_bcrypt import Bcrypt
import mysql.connector

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "Sharath@FLASK@2025"

db = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="sql12792986",
    password="9fnRZjulhI",
    database="sql12792986"
)

@app.route('/')
def hello():
    return render_template('Entry.html')

@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/homeadmin')
def adminh():
    return render_template('Home_s.html')

@app.route('/EMP_login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        email = request.form['email']
        password_in = request.form['password']

        cursor = db.cursor()
        cursor.execute("SELECT * FROM EMPLOYEE WHERE email=%s",(email,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user[2],password_in):
            return redirect('/home')
        else:
            return "Invalid credentials"
    return render_template('EMP_login.html')

@app.route('/EMP_register',methods=['GET','POST'])
def register():
    if request.method =='POST':
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        cursor = db.cursor()
        cursor.execute("INSERT INTO EMPLOYEE (email, password) VALUES (%s, %s)", (email, password))
        db.commit()
        return redirect('/EMP_login')
    return render_template('EMP_Register.html')
    


if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)