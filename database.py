import sqlite3
def create():
    return sqlite3.connect(r'prdb.db')
#create()

def createtable():
    table=create()
    col=table.cursor()
    query='create table student(id int primary key,name varchar(30),age int(3),mobilenumber int(10),place varchar(50))'
    col.execute(query)
    table.commit()
    print("Table created")
    col.close()
#createtable()

#insert data
def insertdata(id,name,age,mobilenumber,place):
    table=create()
    col=table.cursor()
    data=f"insert into student(id,name,age,mobilenumber,place)values('{id}','{name}','{age}','{mobilenumber}','{place}')"
    col.execute(data)
    table.commit()
    print('Datas inserted')
    col.close()
#insertdata(1,"Azhagarasan",29,8489324002,"Chennai")
# for i in range(2,5):
#     id=i
#     nm=input('Enter name:')
#     ag=int(input('Enter age:'))
#     mb=int(input('Enter mobile number:'))
#     pl=input('Enter location:')
#     insertdata(id,nm,ag,mb,pl)

def showalldata():
    con=create()
    cursor=con.cursor()
    query="select * from student"
    cursor.execute(query)
    result=cursor.fetchall()
    for i in result:
        print(i)
#showalldata()

def showalldatabyid(k):
    con=create()
    cursor=con.cursor()
    query=f"select * from student where id={k}"
    cursor.execute(query)
    result=cursor.fetchall()
    for i in result:
        print(i)
# i=int(input('Enter ID:'))
# showalldatabyid(i)

def updatedata(id,name,age):
    lol=create()
    cus=lol.cursor()
    quer=f"update student set name='{name}', age='{age}' where id='{id}' "
    cus.execute(quer)
    lol.commit()
    print("data was updated")
    lol.close()
# id=int(input('Enter the id:'))
# name=input("Enter the name:")
# age=int(input("Enter age:"))
# updatedata(id,name,age)
# showalldata()

def deletedata(k):
    con=create()
    cursor=con.cursor()
    query=f"delete from student where id={k}"
    cursor.execute(query)
    con.commit()
    print('Data deleted')
    con.close()
# insertdata(5,"Thareek",29,876543219,'Chennai')
# showalldata()
# i=int(input("Enter ID to delete:"))
# deletedata(i)