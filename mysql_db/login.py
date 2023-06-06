"""
模拟注册和登陆的过程
"""
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='Root',
                     database='stu',
                     charset='utf8')

cur = db.cursor()

def main():
    print("1 or 2")
    cmd = input(':')
    if cmd == "1":
        login()
    elif cmd == "2":
        registered()


def input_1():
    name = input("please input username:")
    password = input("please input password:")
    return name, password


def login():
    name, password = input_1()
    try:
        login_sql = "select password from user where name = %s;"
        cur.execute(login_sql,name)
        db.commit()
    except Exception:
        db.rollback()
        print("name or password error")
        login()
    else:
        if cur.fetchone()[0] == password:
            print("login success")
        else:
            print("password error")
            login()
    cur.close()
    db.close()


def registered():
    name, password = input_1()
    try:
        registered_sql = "insert into user values (%s,%s);"
        cur.execute(registered_sql,[name,password])
        db.commit()
    except Exception:
        db.rollback()
        print("Duplicate user name")
        registered()
    cur.close()
    db.close()

if __name__ == '__main__':
    main()
