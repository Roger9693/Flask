from flask import Flask
from flask_restful import Resource,Api,marshal_with,fields,reqparse,abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api= Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class TodoModels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(100))
    summary = db.Column(db.String(500))

dict={
    'id' : fields.Integer,
    'task': fields.String,
    'summary': fields.String
}

pargs = reqparse.RequestParser()
pargs.add_argument('task', type=str,help='task is required', required = True)
pargs.add_argument('summary',type=str, help = 'summary is required', required=True)

uargs = reqparse.RequestParser()
uargs.add_argument('task', type=str)
uargs.add_argument('summary',type=str)

class Todolist(Resource):
    @marshal_with(dict)
    def get(self):
        return TodoModels.query.all()

class Todo(Resource):
    @marshal_with(dict)
    def get(self, todo_id):
        todo = TodoModels.query.filter_by(id=todo_id).first()
        if not todo:
            abort(404, message = "Task ID doesn't exit")
        return todo
    
    @marshal_with(dict)
    def post(self, todo_id):
        args = pargs.parse_args()
        task = TodoModels.query.filter_by(id=todo_id).first()
        if task:
            abort(409, message = 'Task ID taken')
        new_task = TodoModels(id = todo_id, task = args['task'], summary=args['summary'])
        db.session.add(new_task)
        db.session.commit()
        return new_task, 201
    
    @marshal_with(dict)
    def put(self, todo_id):
        args = uargs.parse_args()
        task = TodoModels.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message = "Task id doesn't exist")
        if task:
            task.task =args['task']
        if args['summary']:
            task.summary=args['summary']
        db.session.commit()
        return task
    
    @marshal_with(dict)
    def delete(self, todo_id):
        task=TodoModels.query.filter_by(id=todo_id).first()
        if not task:
            abort(404,message="Task id doesn't exist")
        db.session.delete(task)
        db.session.commit()
        return TodoModels.query.all()

api.add_resource(Todo,'/todo/<int:todo_id>')
api.add_resource(Todolist,'/todos')

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)