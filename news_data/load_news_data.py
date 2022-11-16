import pymysql
import openpyxl
import pandas as pd

from config.DatabaseConfig import * # DB 접속 정보 불러오기


# 학습 데이터 초기화
def all_clear_news_data(db):
    # 기존 학습 데이터 삭제
    sql = '''
            delete from news_2015
        '''
    with db.cursor() as cursor:
        cursor.execute(sql)

    # auto increment 초기화
    sql = '''
    ALTER TABLE news_2015 AUTO_INCREMENT=1
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)


# db에 데이터 저장
def insert_data(db, xls_row):
    news_head, news_date, news_img, news_url = xls_row

    sql = '''
        INSERT news_2015(news_head, news_date, news_img, news_url) 
        values(
         "%s", "%s", "%s", "%s"
        )
    ''' % (news_head.value, news_date.value, news_img.value, news_url.value)

    # 엑셀에서 불러온 cell에 데이터가 없는 경우, null 로 치환
    sql = sql.replace("'None'", "null")

    with db.cursor() as cursor:
        cursor.execute(sql)
        print('{} 저장'.format(news_head.value))
        db.commit()


xl_file = 'news.xlsx'
db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    # 기존 학습 데이터 초기화
    all_clear_news_data(db)




    # 학습 엑셀 파일 불러오기
    wb = openpyxl.load_workbook(xl_file)
    sheet = wb['Sheet1']
    for row in sheet.iter_rows(min_row=2): # 해더는 불러오지 않음
        # 데이터 저장
        insert_data(db, row)

    wb.close()

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
