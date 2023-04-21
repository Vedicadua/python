
import mysql.connector as c
con=c.connect(host="localhost", user="root", password="radha_swami24", database="python",port='3306')
if con.is_connected():
    print("successfully connected")

cursor=con.cursor()
cursor.execute("CREATE TABLE users (user_id int primary key auto_increment, user_name VARCHAR(255) not null)")
query="insert into users(user_id,user_name) values(%s,%s)"
value=[(1,"vedica"),
       (2,"manish"),
       (3,"ravi"),
       (4,"mohan")]
cursor.executemany(query,value)
con.commit()
print("successfully inserted")
