import pymysql

host = 'localhost' #호스트 이름
port = 3306 #포트주소

database = 'madang'
username = 'root'
password = '2135658dbstmf!'

#접속상태확인
conflag = False

try:
    print('데이터베이스 연결 준비...')
    conn =pymysql.connect(host=host, user=username, database=database, \
        port=port, password=password, charset='utf8') #mysql 접속 함수 connect
    conflag = True
    print('데이터베이스 연결 성공!')
    
except Exception as err:
    print('데이터베이스 연결 실패')
    print(err)

#접속에 성공한다면 쿼리문 실행
if conflag:
    #커서(무언가 가르키는 것 의미) 객체 생성
    cursor = conn.cursor()
    sqlString = 'select * from book;' # 실행할 sql문 (mysql은 ;필요)
    res = cursor.execute(sqlString) 
    #실행 #커서객체는 sql실행결과의 레코드 수,메모리 첫 주소를 알고 있다. 즉, 커서를 통해서 데이터베이스를 저장해 놓은 메모리를 참조하고 그 크기를 통해서 전체 내용을 알고 있음.
    data = cursor.fetchall()
    print('data의 타입 = ', type(data)) # tuple 타입으로 나온다. 메모리 참조를 통해 값을 수정하면 안 되므로 튜플로 가지고 옴.
    print('{0}\t {1:<} \t {2:<} \t {3:>}'.format('bookid', 'bookname', 'publisher', 'price'))

    for rowdata in data:
        bookid = rowdata[0]
        bookname = rowdata[1]
        publisher = rowdata[2]
        price = rowdata[3]
        
        row = [bookid, bookname, publisher, price]
        
        for i in range(4):
            if row[i] == None:
                row[i] = 0
        
        print('{0}\t {1:<} \t {2:<} \t {3:>}'.format(row[0], row[1], row[2], row[3]))
    
    cursor.close()
    conn.close()