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
# 执行sql语句
sql = "insert into class values (8,'wqz',26,'m',76.5,'2019-8-8');"
cur.execute(sql)
db.commit() # 将写操作提交，多次写操作一同提交

# 关闭
cur.close()
db.close()
