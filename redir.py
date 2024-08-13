from flask import Flask, render_template, redirect,url_for

req=Flask(__name__)

@req.route('/')
def fg():
    s="welcome"
    return s

@req.route('/<name>/<age>')
def wel(name,age):
    return f"<h1>Welcome {name}.Your age is {age}</h1>" 

@req.route('/home')
def home():
    return render_template('filter.html',a="hai...hello guys")

@req.route('/about')
def againhome():
    return redirect('/home')

@req.route('/visit')
def front():
    return redirect(url_for('fg'))

@req.route('/css')
def htl():
    return render_template('html_css.html')

if __name__=="__main__":
    req.run(debug=True,port=5006)