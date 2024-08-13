from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>hello welcome to my first page of project<h1>"

@app.route('/jinja')
def ss():
    ranges = [{"Language":"Python","Author": "Gudio van rossum"},
              {"Language": "HTML","Author": "Beneres lee"},
              {"Language": "Flask","Author": "Arminronacher"}]
    return render_template('loginpage.html',author='Armin Ronacher',Arminronacher=True,Post=ranges)


def content():
    a=10
    if a==9:
        return '10'
    else:
        return 'hi'
    
app.add_url_rule('/content1','content',content)

if __name__=="__main__":
    app.run(debug=True,port=5007)