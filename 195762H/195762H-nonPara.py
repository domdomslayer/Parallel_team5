import pymysql.cursors
import random
import string
import time

conn = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='palallel',
                             charset='utf8',
                             # 結果の受け取り方の指定。Dict形式で結果を受け取ることができる
                             cursorclass=pymysql.cursors.DictCursor)

def randomname():
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]
   return ''.join(randlst)


def doSomething():
    with conn.cursor() as cursor:
        sql = "SELECT id,name,TestScore FROM user WHERE TestScore=%s"
        cursor.execute(sql, (10000,))
        result = cursor.fetchall()
        print(result)


if __name__ == '__main__':
    start = time.time()

    doSomething()
    conn.commit()
    conn.close()

    elapsed_time = time.time() - start
    print("並列なし:{0}".format(elapsed_time) + "[sec]")