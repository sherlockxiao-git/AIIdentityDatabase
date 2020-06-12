import requests
import json
import cv2
def add_image(facealbum_token, img_file):
    http_url = "https://api-cn.faceplusplus.com/imagepp/v1/facealbum/addimage"
    data = {
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "facealbum_token": facealbum_token
    }
    file={"image_file":open(img_file,"rb")}
    respose=requests.post(http_url,data=data,files=file)
    data= json.loads(respose.text)
    return data
def search_image(facealbum_token,img_file):
    http_url="https://api-cn.faceplusplus.com/imagepp/v1/facealbum/searchimage"
    data={
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "facealbum_token": facealbum_token

    }
    file={"image_file":open(img_file,"rb")}
    respose=requests.post(http_url,data=data,files=file)
    data=json.loads(respose.text)
    cv2.waitKey(500)
    http_url="https://api-cn.faceplusplus.com/imagepp/v1/facealbum/searchimagetaskquery"
    result={
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "task_id":data["task_id"]
    }
    respose = requests.post(http_url, data=result)
    result=json.loads(respose.text)
    return result
def find_candidate(facealbum_token,group_id):
    http_url = "https://api-cn.faceplusplus.com/imagepp/v1/facealbum/findcandidate"
    data = {
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "facealbum_token": facealbum_token,
        "group_id":group_id
    }
    respose = requests.post(http_url, data=data)
    data = json.loads(respose.text)
    return data
def get_imagedetail(facealbum_token,image_id):
    http_url = "https://api-cn.faceplusplus.com/imagepp/v1/facealbum/getimagedetail"
    data = {
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "facealbum_token": facealbum_token,
        "image_id":image_id
    }
    respose = requests.post(http_url, data=data)
    data = json.loads(respose.text)
    return data

# facealbum_token="1576157869-f678975b-19f3-41e1-a8be-6a05baaef268" #测试用相册token
# img_files="E:\AIChangingFace\\trysomethon\gakki.jpg" #测试用相片
# img_files="E:\iddatabasepic\capnew20191224201745.jpg"
# add_image(facealbum_token,img_files)          #添加相片
# result=search_image(facealbum_token,img_files)         #查找照片
# result=Ablumact.delete_album("")                     #删除相册
# Ablumact.find_facealbums()                    #查看已有相册
# print(result)
# file={"image_file":open(img_files,"rb")}
