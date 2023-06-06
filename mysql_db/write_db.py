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

# 写入数据库数据
try:
    # name = input('name:')
    # age = int(input('age:'))
    # score = int(input("score:"))
    # sql = "insert into class (name,age,score) values ('%s',%d,%d)"%(name,age,score)
    # cur.execute(sql)
    # db.commit()

    # 修改
    sql = "update class set  name = 'wqz1' where name = 'wqz'"
    cur.execute(sql)
    db.commit()
except Exception as e:
    db.rollback() # 退回到commit执行之前的数据库状态
    print(e)



# 关闭
cur.close()
db.close()