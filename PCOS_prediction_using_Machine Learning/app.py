from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import numpy as np
from flask_mysqldb import MySQL
import MySQLdb.cursors


model = pickle.load(open('D:\PCOS_Pred\Model\PCOSPredictionModel_2.pkl', 'rb'))

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'medical'
  
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('index_updated.html')

@app.route('/Registration')
def reg():
    return render_template('Registration.html')

@app.route('/logged')
def log():
    return render_template('login.html')

@app.route('/profile')
def pr():
    return render_template('profile.html')

@app.route('/profile_1')
def pr1():
    return render_template('profile_1.html')

@app.route('/profile_2')
def pr2():
    return render_template('profile_2.html')

@app.route('/profile_3')
def pr3():
    return render_template('profile_3.html')

@app.route('/profile_4')
def pr4():
    return render_template('profile_4.html')

@app.route('/profile_5')
def pr5():
    return render_template('profile_5.html')

@app.route('/calender')
def cal():
    return render_template('calender.html')

@app.route('/predict', methods=['POST'])
def predict():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11 = request.form['k']
    data12 = request.form['l']
    data13 = request.form['m']
    data14 = request.form['n']
    data15 = request.form['o']
    data16 = request.form['p']
    data17 = request.form['q']
    data18 = request.form['r']
    data19 = request.form['s']
    data20 = request.form['t']
    data21 = request.form['u']

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10,
                   data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21]])
    pred = model.predict(arr)
    return render_template('a.html', data=pred)


@app.route('/login', methods=['POST'])
def login():
    usern = request.form['UserName']
    password = request.form['PSW']
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM registered_user WHERE Username = %s AND Password = %s', (usern, password))
    user = cursor.fetchone()
    if user:
            mesage = 'Logged in successfully !'
            return render_template('prediction_updated.html')
    else:
            mesage = 'Please enter correct email / password !'
            return render_template('login.html')




@app.route('/register', methods=['POST'])
def register():
    message=''
    name = request.form['Name']
    usern = request.form['UserName']
    password = request.form['PSW']
    email = request.form['Email']
    address = request.form['Adds']
    age = request.form['Age']
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM registered_user WHERE Username = % s AND Password = % s', (usern, password))
    account = cursor.fetchone()
    if account:
            message='Account exists!'           
    else:
            cursor.execute('INSERT INTO registered_user VALUES (%s, %s, %s, %s, %s, %s)', (name, usern, password, email, address, age))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
            return render_template('login.html')

if __name__ == "__main__":
    app.run()
