import pymysql
from config.DatabaseConfig import * # DB 접속 정보 불러오기

db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    # 테이블 생성 sql 정의
    sql = '''
    CREATE TABLE IF NOT EXISTS `news_2015` (
    `news_head` text NULL,
    `news_date` date NULL,
    `news_img` varchar(2048) NULL,
    `news_url` varchar(2048) NULL
    )
    '''

    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
