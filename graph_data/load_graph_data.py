import pymysql
import openpyxl
import pandas as pd

from config.DatabaseConfig import * # DB 접속 정보 불러오기


# 학습 데이터 초기화
def all_clear_graph_data(db):
    # 기존 학습 데이터 삭제
    sql = '''
            delete from accident_graph
        '''
    with db.cursor() as cursor:
        cursor.execute(sql)

    # auto increment 초기화
    sql = '''
    ALTER TABLE accident_graph AUTO_INCREMENT=1
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)


# db에 데이터 저장
def insert_data(db, xls_row):
    year, pie = xls_row

    sql = '''
        INSERT accident_graph(year, pie) 
        values(
         "%s", "%s"
        )
    ''' % (year.value, pie.value)

    # 엑셀에서 불러온 cell에 데이터가 없는 경우, null 로 치환
    sql = sql.replace("'None'", "null")

    with db.cursor() as cursor:
        cursor.execute(sql)
        print('{} 저장'.format(year.value))
        db.commit()


xl_file = 'graph.xlsx'
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
    all_clear_graph_data(db)




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
