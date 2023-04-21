import mysql.connector as c
con=c.connect(host="localhost", user="root", password="radha_swami24", database="python",port='3306')
if con.is_connected():
    print("successfully connected")

cursor=con.cursor()
cursor.execute("CREATE TABLE project(project_id int primary key auto_increment,user_id int, task_id int, status varchar(244) not null, foreign key(user_id) references users(user_id),foreign key(task_id) references tasks(task_id))")
query="insert into project(project_id,user_id,task_id,status) values(%s,%s,%s,%s)"
val=[(1,2,1,"pending"),
       (2,2,3,"pending"),
       (3,1,3,"pending"),
       (4,2,4,"pending"),
       (5,1,2,"pending"),
       (6,4,2,"completed"),
       (7,4,1,"completed"),
       (8,1,4,"pending"),
       (9,1,1,"in-progress"),
       (10,2,3,"in-progress")]
cursor.executemany(query,val)
con.commit()
print("successful")