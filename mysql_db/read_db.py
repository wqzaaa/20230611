import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='Root',
                     database='stu',
                     charset='utf8')
# 获取游标 （操作数据库，执行sql语句）
cur = db.cursor()

# 获取数据库数据
sql = "select * from class"
cur.execute(sql)

one_row = cur.fetchone()
print(one_row)
many_row = cur.fetchmany(2)
print(many_row)
all_row = cur.fetchall()
print(all_row)


# 关闭
cur.close()
db.close()