from flask import Flask, render_template, request, redirect, url_for,get_flashed_messages, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///tasks.db'
app.config['SECRET_KEY'] ='secret_key'

db = SQLAlchemy(app)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable =False)
    Completed=db.Column(db.Boolean, default =False)

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!','success')
    else:
        flash('Task title cannot be empty','error')
    return redirect('/')

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = True
        db.session.commit()
        flash('Task marked as completed!','success')
    else:
        flash('Task not found!','error')
    return redirect('/')

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)

    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully!','success')
    else:
        flash('Task not found!','error')
    return redirect('/')

if __name__== '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=5432)