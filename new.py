from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>hello welcome to my first page of first project<h1>"

@app.route('/Content')
def content():
    return 'This is content page'

@app.route('/bin/<float:num>')
def two(num):
    return (f"float {num}")

@app.route('/Html')
def pack():
    return '''<!doctype html
    <html>
    <head>
<title>My Document</title>
<style>
table{border:5px solid black}
th,td{border:1px solid black}

td{width:250px}

body{background-color:lightyellow; text-align:center}

table{margin-left:450px}

</style>
</head>

<body>
<h1>Registration form</h1>
<table>
<tr>
<th style="color:pink">First name:</th>
<td>
<form>
<input type="text">
</form>
</td>
</tr>

<tr>
<th style="color:orange">Last name:</th>
<td>
<form>
<input type="text">
</form>
</td>
</tr>

<tr>
<th style="color:green">DOB:</th>
<td>
<form>
<input type="date">
</form>
</td>
</tr>

<tr>
<th style="color:blue">Gender</th>
<td>
<form>
<input type="radio">
<label>Male</label>
<input type="radio">
<label>Female</label>
</form>
</td>
</tr>

<tr>
<th style="color:red">Mail id:</th>
<td>
<form>
<input type="email" placeholder=".com">
</form>
</td>
</tr>

<tr>
<th>Create password:</th>
<td>
<form>
<input type="password">
</form>
</td>
</tr>

<tr>
<th>Confirm password:</th>
<td>
<form>
<input type="password">
</form>
</td>
</tr>

<tr>
<th>Address:</th>
<td>
<form>
<input type="text">
</form>
</td>
</tr>

<tr>
<th rowspan="2">Ph no:</th>
<td>
<form>
<input type="text" placeholder="official num">
</form>
</td>
</tr>

<tr>
<td>
<form>
<input type="text" placeholder="personal num">
</form>
</td>
</tr>

<tr>
<th>Language known:</th>
<td>
<form>
<input type="checkbox">
<label>English</label>
<input type="checkbox">
<label>Tamil</label>
<input type="checkbox">
<label>Malayalam</label>
</form>
</td>
</tr>

<tr>
<th>Degree:</th>
<td>
<form>
<select>
  <option value="option1">EEE</option>
  <option value="option2">Mech</option>
  <option value="option3">ECE</option>
  <option value="option4">CSE</option>
</select>
</form>
</td>
</tr>

<tr>
<th colspan="2">
<form>
<input type="submit">
<input type="reset">
</form>
</th>
</tr>

</table>
</body>
</html>'''

@app.route('/dict')
def dic():
    return '''<!doctype html
    <html>
    <title>project</title>
    </head>
    <body>
    <h1>PROJECT</h1>
    <p>{"launguage":"Python","Author": "Gudio van rossum"},
    {"Language": "HTML","Author": "Beneres lee"},
    {"Language": "Flask","Author": "Arminronacher"}
    </p>
    </body>
    </html>'''


if __name__=="__main__":
    app.run(debug=True,port=5008)