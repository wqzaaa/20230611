"""
对二进制文件进行存储
"""

import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='Root',
                     database='stu',
                     charset='utf8')

cur = db.cursor()

# with open('xiaogou.jpeg','rb') as f:
#     date = f.read()
# try:
#     sql = "update class set image = %s where name = 'wqz1';"
#     cur.execute(sql,[date])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取图片
sql = "select image from class where name = 'wqz1';"
cur.execute(sql)
date = cur.fetchone()
with open('wqz.jpg','wb') as f:
    f.write(date[0])

cur.close()
db.close()



