import pymysql.cursors
import random
import string
import time
import multiprocessing

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='parallel',
                       charset='utf8',
                       # 結果の受け取り方の指定。Dict形式で結果を受け取ることができる
                       cursorclass=pymysql.cursors.DictCursor)


def randomname():
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]
    return ''.join(randlst)


"""
with conn.cursor() as cursor:
    sql = "create table user (id int, name varchar(10), Number int)"
    cursor.execute(sql,)
with conn.cursor() as cursor:
    for i in range(5000000):
        sql = "INSERT INTO user VALUES (%s,%s, %s)"
        cursor.execute(sql, (i, randomname(), random.randint(0, 10000)))
conn.commit()
"""


def doSomething():
    with conn.cursor() as cursor:
        for i in range(5000000):
            sql = "INSERT INTO user VALUES (%s, %s, %s)"
            cursor.execute(sql, (str(i), randomname(), str(i)))
        cursor.close()


if __name__ == '__main__':
    start = time.time()

    p = multiprocessing.Process(target=doSomething)

    p.start()
    p.join()
    p.close()
    conn.commit()
    conn.close()

    elapsed_time = time.time() - start
    print("並列あり:{0}".format(elapsed_time) + "[sec]")
