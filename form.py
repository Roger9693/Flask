from flask import Flask, render_template,request,url_for

app1=Flask(__name__)

@app1.route('/')
def login():
    return render_template('log_in.html')

@app1.route('/submit', methods=['POST'])
def sub():
    username=request.form['username']
    password=request.form['pwd1']
    return render_template('submit.html',u=username,p=password)

@app1.route('/register')
def sub2():
    return render_template('register.html')

@app1.route('/form', methods=['POST'])
def sub1():
    email=request.form['email']
    address=request.form['address']
    return render_template('form.html',e=email,a=address)

if __name__=="__main__":
    app1.run(debug=True,port=5005)