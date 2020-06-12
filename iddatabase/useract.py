import faceact
import imageact
import Ablumact
import sqlact
import facedetect
import re
def create_database():              #创建一个人脸相册
    ablum_token=Ablumact.create_album()
    return ablum_token

def delete_database(ablum_token):      #删除一个人脸相册
    result=Ablumact.delete_album(ablum_token)
    return result

def find_alldatabase(sta=1):            #查看所有的人脸相册
    result=Ablumact.find_facealbums(sta)
    return result

def find_detail(facealbum_token,sta=1):     #查看某一人脸相册的具体信息
    result=Ablumact.find_albumdetail(facealbum_token,sta=1)
    return result

def add_newone(tablename,name,grade,facealbum_token,img_path):   #向库中增加一张图片
    result=imageact.add_image(facealbum_token,img_path)
    # face_token=result["faces"]["face_token"]
    image_id=result["image_id"]
    gender=facedetect.face_detect(img_path)["faces"][0]["attributes"]["gender"]["value"]
    id=int(re.search(r"\d+",img_path)[0])
    sqlact.add_to_sql(tablename,id,name,gender,grade,image_id)
    print("well, already add a new one.")

def update_one(facealbum_token,face_tokens,group_id):           #修改线上库信息
    result=faceact.update_face(facealbum_token,face_tokens,group_id)
    messages=result["face_tokens_success"]
    return messages

def update_message(tablename,name,grade):
    sqlact.update_one_sql(tablename,name,grade)

def group_all(facealbum_token,operation_type="incremental"):        #聚类照片
    result=faceact.group_face(facealbum_token,operation_type="incremental")
    group_result=result
    return group_result

def delete_one(facealbum_token,tablename,name):
    data=sqlact.search_sql(tablename,name)
    image_id=data[0][-1]
    result=faceact.delete_face(facealbum_token,image_id)
    sqlact.delete_one_sql()
    return result

def find_one(facealbum_token,img_file):
    result=imageact.search_image(facealbum_token,img_file)
    image_id=result["search_result"][0]["image_id_set"].split(",")[0]
    return image_id

# facealbum_token="1576157869-f678975b-19f3-41e1-a8be-6a05baaef268"
# facealbum_token="1577372360-35df51c8-ff6a-410f-9621-3e57b1af3005"
# facealbum_token="1577420216-ffd9bbca-93e1-461f-9418-91023307c1c1"
# img_path="E:\\iddatabasepic\\capnsew20191226231157.jpg"
# result=find_one(facealbum_token,img_path)
# add_newone("student","张三",100,facealbum_token,img_path)
# result=find_detail(facealbum_token)
# result=group_all(facealbum_token)
# print(result)

