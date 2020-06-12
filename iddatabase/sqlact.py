import pymysql
def add_to_sql(tablename,id,name,gender,grade,image_id):
    aiuse=pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="wang518518",
                             db="db_aiuse")

    cs3 = aiuse.cursor()
    sql3 = "insert into "+tablename+ " values(%s, %s, %s, %s,%s)"
    cs3.execute(sql3, (id,name,gender,grade,image_id))
    aiuse.commit()  ## 提交数据
    cs3.close() ## 关闭游标cs3
    aiuse.close() ## 关闭数据库
    print("well done")
def delete_one_sql(tablename,image_id):
    aiuse = pymysql.connect(host="localhost",
                            port=3306,
                            user="root",
                            password="wang518518",
                            db="db_aiuse")

    cs3 = aiuse.cursor()
    sql = "delete from"+tablename+ "where id=%s"
    cs3.execute(sql, (image_id))
    aiuse.commit()  ## 提交数据
    cs3.close()  ## 关闭游标cs3
    aiuse.close()  ## 关闭数据库
    print("well done")
def update_one_sql(tablename,name,grade):
    aiuse = pymysql.connect(host="localhost",
                            port=3306,
                            user="root",
                            password="wang518518",
                            db="db_aiuse")

    cs3 = aiuse.cursor()
    sql3 = "update "+tablename+ " set  name=%s,  grade=%s"
    cs3.execute(sql3, ( name, grade))
    aiuse.commit()  ## 提交数据
    cs3.close()  ## 关闭游标cs3
    aiuse.close()  ## 关闭数据库
    print("well done")
def search_sql(tablename,image_id):
    aiuse = pymysql.connect(host="localhost",
                            port=3306,
                            user="root",
                            password="wang518518",
                            db="db_aiuse")

    cs3 = aiuse.cursor()
    sql3 = "select * from "+tablename+" where image_id = %s "
    cs3.execute(sql3, (image_id))
    data3 = cs3.fetchall()  ## 指针移动到最后一行了
    # print(data3)
    cs3.close()  ## 关闭游标cs3
    aiuse.close()  ## 关闭数据库
    return data3
def search_all_sql(tablename):
    aiuse = pymysql.connect(host="localhost",
                            port=3306,
                            user="root",
                            password="wang518518",
                            db="db_aiuse")

    cs3 = aiuse.cursor()
    sql3 = "select name,gender,grade from "+tablename
    cs3.execute(sql3)
    data3 = cs3.fetchall()  ## 指针移动到最后一行了
    # print(data3)
    cs3.close()  ## 关闭游标cs3
    aiuse.close()  ## 关闭数据库
    return data3
# add_to_sql("student","1","张三","male",100,"85881b576b87b8b6b9fd88fd3106c6e9")
# data=search_sql("student","张三")
# print(data[0][-1])
# data=search_sql("student","6fe8ff94386e29f8584acac1edd39297")
# print(data)
# data3=search_all_sql("student")
# print(data3)