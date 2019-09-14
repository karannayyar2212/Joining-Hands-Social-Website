
from module.database import dba
from flask import Flask, flash, render_template, redirect, url_for, request, session
db = dba()
app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"

@app.route('/reg',methods = ['POST','GET'])
def reg():
        if request.method == 'POST' and request.form['save']:
                if db.insert(request.form):
                        print("inserted")
                        return redirect(url_for('success'))
                else:
                        print("not inserted")
                        return redirect(url_for('invalid'))
	else:
                return render_template('index.html')

@app.route('/ngoregister/')
def ngoregister():
        return redirect(url_for('ngo_register')
@app.route('/ngoadmin/')
def ngoadmin():
        return render_template('ngoadmin.html')

@app.route('/login/')
def login():
	return render_template('login.html')
@app.route('/data' ,methods = ['POST','GET'])
def data():
    if request.method == "POST":
        n =  db.check_login(request.form)
        if len(n) ==0:
            return redirect(url_for('invalid'))
        for row in n:
            t = row[3]
            if t =='admin':
                return redirect(url_for('ngoadmin'))
            else:
                return redirect(url_for('user'))
    else:
        return  render_template('login.html')


@app.route('/user/')
def user():
	return render_template('user.html')

@app.route('/new/')
def new():
	return render_template('new.html')



@app.route('/invalid/')
def invalid():
    return render_template('invalid.html')

@app.route('/')
def index():
	return render_template('index.html')
	
	

if __name__ == '__main__':
    app.run(debug = True, port=8181, host="0.0.0.0")
