import pymysql
aiuse=pymysql.connect(host="localhost",
                         port=3306,
                         user="root",
                         password="wang518518",
                         db="db_aiuse")

cs3 = aiuse.cursor()
sql3 = "insert into student values(%s, %s, %s, %s)"
cs3.execute(sql3, ("1", "张伟","男", "100"))
aiuse.commit()  ## 提交数据
cs3.close() ## 关闭游标cs3
aiuse.close() ## 关闭数据库