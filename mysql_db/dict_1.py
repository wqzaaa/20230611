"""
将单词本存入数据库
1.创建数据库 dict （utf8）
2.创建数据表 words 将单词和单词解释分别存入不同的字段
3.将单词存入words存入单词表 超过19500即可

"""
import re
import pymysql

f = open('dict.txt','r')

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='Root',
                     database='dict',
                     charset='utf8')

cur = db.cursor()
sql = "insert into words (word,mean) values (%s,%s)"


for line in f:
    # if not line:
    #     break
    # date = line.split(' ',1)
    # word = date[0]
    # mean = date[1].strip(" ")
    tup = re.findall(r"(\S+)\s+(.*)",line)[0] # 正则表达式
    try:
        cur.execute(sql,tup)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)

cur.close()
db.close()



