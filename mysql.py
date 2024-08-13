from flask import Flask,render_template,request
from flask_mysqldb import MySQL

db=Flask(__name__)

db.config['MYSQL_HOST'] = 'localhost'
db.config['MYSQL_USER'] = 'root'
db.config['MYSQL_PASSWORD'] = '1234'
db.config['MYSQL_DB'] = 'work'

mysql = MySQL(db)
@db.route('/')
def main():
    cursor=mysql.connection.cursor()
    # cursor.execute('create table student(user varchar(50),pass varchar(50))')
    # cursor.execute('insert into student values("rrr","12345")')
    cursor.execute('insert into student values("Ajith","23456")')
    cursor.execute('insert into student values("Azhagarasan","76543")')
    # cursor.execute('delete from student where user="Ajith"')
    cursor.execute('select * from student')
    users = cursor.fetchall()

    mysql.connection.commit()
    cursor.close()
    print("data was inserted")
    return render_template('index.html', users=users)

if __name__=='__main__':
    db.run(debug=True,port=7345)