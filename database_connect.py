import pymysql

#sheet_name = ['总资产利润率(%)', '销售净利率(%)', '流动比率(%)',
#              '资产负债率(%)', '总资产周转率(次)', '流动资产周转率(次)',
#            '速动比率(%)']

try:
    db=pymysql.connect(host = "localhost", #主机名称
                       user = "root", #数据库用户名
                       password = "271828", #用户名对应的密码
                       database = "dbtest", #数据库名称
                      )
    print("数据库连接成功")

    
    cur=db.cursor()
    cur.execute("drop table if exists Student")#大小写没有关系
    sql='create table Student(Name char(20)not null,Email char(20),Age int)'
    cur.execute(sql)
    print("表格插入成功")
    

    '''
    创建表
    cur=db.cursor()
    cur.execute("drop table if exists Student")#大小写没有关系
    sql='create table Student(Name char(20)not null,Email char(20),Age int)'
    cur.execute(sql)
    print("表格插入成功")
    '''

    '''
    插入数据
    cur=db.cursor()
    sql='insert into Student(Name,Email,Age)Value(%s,%s,%s)'
    value=('Mike','123@163.com',20)
    cur.execute(sql,value)
    db.commit()
    print("数据插入成功")
    '''

    '''
    查询数据
    cur=db.cursor()
    sql='select * from Student'
    cur.execute(sql)
    results=cur.fetchall()
    for row in results:
        name=row[0]
        email=row[1]
        age=row[2]
        print('Name:%s,Email:%s,Age:%s'%(name,email,age))
    '''

    '''
    更新数据
    cur=db.cursor()
    sql='update Student set Name=%s where Name=%s'
    value=('John','Mike')
    cur.execute(sql,value)
    db.commit()
    print("数据更新成功")
    '''

    '''
    删除数据
    cur=db.cursor()
    sql='delete from Student where Name=%s'
    value=('John')
    cur.execute(sql,value)
    db.commit()
    print("数据删除成功")
    '''

    '''
    删除表格
    cur=db.cursor()
    sql='drop table if exists Student'
    cur.execute(sql)
    print("表格删除成功")
    '''
    
except pymysql.Error as e:
    '''
    print("数据插入失败："+str(e))
    db.rollback()
    '''
    #print("数据查询失败："+str(e))
    '''
    print("数据更新失败："+str(e))
    db.rollback()
    '''
db.close()
