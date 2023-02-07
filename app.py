from flask import Flask,render_template,request
import models




app=Flask(__name__)

@app.route('/',methods=['GET','POST'])


def login_page():
    return render_template('login.html')



@app.route('/sai/',methods=['GET','POST'])

def authencation():
    username=request.form['nam']
    password=request.form['pass']
    obj=models.db(username,password)
    flag=obj.authencate()
    if flag == "suc":
        return "suc"
    else:
        return "unsuc"



@app.route('/register',methods=['GET','POST'])


def register():
    return render_template('register.html')



@app.route('/snv/',methods=['GET','POST'])


def add_user():
    username=request.form['em']
    password=request.form['pass']
    obje=models.db(username,password)
    flag=obje.add_username()
    if flag == "suc created":
        return "suc"
    else:
        return "user alredy created"



if __name__==  "__main__":
    app.run(debug=True)