import multiprocessing 
import pymysql.cursors
import random
import string
import time

def init():
    global connection #接続オブジェクトをグローバル変数で定義する。
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='pararell',
                             charset='utf8',
                             # 結果の受け取り方の指定。Dict形式で結果を受け取ることができる
                             cursorclass=pymysql.cursors.DictCursor)
                             

def doSomething():
    with connection.cursor() as cursor:
        for i in range(1000000):
            sql = "INSERT INTO prac1 VALUES (%s, %s, %s)"
            cursor.execute(sql, (str(i), randomname(), str(i)))
        cursor.close()

def randomname():
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]
   return ''.join(randlst)


if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='2-xvZifV',
                             db='pararell',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor) 

    start = time.time()

    p = multiprocessing.Process(target = doSomething) 

    p.start()
    p.join()
    p.close()
    connection.commit()
    connection.close()

    elapsed_time = time.time() - start
    print("並列あり:{0}".format(elapsed_time) + "[sec]")
    # 並列あり:406.8516218662262[sec]


"""
mysql> SHOW FULL COLUMNS FROM prac1;
+-------+-------------+-----------------+------+-----+---------+-------+---------------------------------+---------+
| Field | Type        | Collation       | Null | Key | Default | Extra | Privileges                      | Comment |
+-------+-------------+-----------------+------+-----+---------+-------+---------------------------------+---------+
| id    | int(11)     | NULL            | YES  |     | NULL    |       | select,insert,update,references |         |
| name  | varchar(10) | utf8_general_ci | YES  |     | NULL    |       | select,insert,update,references |         |
| power | int(11)     | NULL            | YES  |     | NULL    |       | select,insert,update,references |         |
+-------+-------------+-----------------+------+-----+---------+-------+---------------------------------+---------+
"""