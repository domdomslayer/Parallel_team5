import pymysql.cursors
import random
import string
import time

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


if __name__ == '__main__':
    start = time.time()

    with conn.cursor() as cursor:
        for i in range(5000000):
            sql = "INSERT INTO user VALUES (%s, %s, %s)"
            cursor.execute(sql, (str(i), randomname(), str(i + i*9)))

    conn.commit()
    conn.close()

    elapsed_time = time.time() - start
    print("並列なし:{0}".format(elapsed_time) + "[sec]")
