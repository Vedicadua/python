import mysql.connector as c
con=c.connect(host="localhost", user="root", password="radha_swami24", database="python",port='3306')
if con.is_connected():
    print("successfully connected")

cursor=con.cursor()
cursor.execute("CREATE TABLE tasks (task_id int primary key auto_increment, task_name VARCHAR(255) not null)")
query="insert into tasks(task_id,task_name) values(%s,%s)"
value=[(1,"oops concept"),
       (2,"mysql-connection"),
       (3,"java introduction"),
       (4,"python introduction")]
cursor.executemany(query,value)
con.commit()
print("successfully inserted")

