import mysql.connector as c
con=c.connect(host="localhost", user="root", password="radha_swami24", database="python",port='3306')
if con.is_connected():
    print("successfully connected")
print("using inner join")
cursor=con.cursor()
cursor.execute("""select users.user_id,count(project.status='pending') as pending
 from project inner join users on project.user_id=users.user_id where project.status='pending'
  group by users.user_id having pending >=3""")


result=cursor.fetchall()
for row in result:
    print(row)
print("left join")
cursor.execute("""select users.user_id,count(project.status='pending') as pending
 from project left join users on project.user_id=users.user_id where project.status='pending'
  group by users.user_id having pending >=3""")
result1=cursor.fetchall()
for row in result1:
    print(row)
print("right join")
cursor.execute("""select users.user_id,count(project.status='pending') as pending
 from project right join users on project.user_id=users.user_id where project.status='pending'
  group by users.user_id having pending >=3""")
result2=cursor.fetchall()
for row in result2:
    print(row)
print("cross join")
cursor.execute("""select users.user_id,count(project.status='pending') as pending
 from project cross join users on project.user_id=users.user_id where project.status='pending'
  group by users.user_id having pending >=3""")
result3=cursor.fetchall()
for row in result3:
    print(row)