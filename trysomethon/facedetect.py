import requests
import json
import base64
import cv2
def face_detect(img_path):
    http_url="https://api-cn.faceplusplus.com/facepp/v3/detect"
    data={"api_key":"0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
          "api_secret":"miaBYP2j66n81meWzDjiDHudsp6_MVzM",
          "return_attributes":"age,gender,headpose,emotion,beauty",
          "return_landmark":1
          }
    files={"image_file":open(img_path,"rb")}
    respose=requests.post(url=http_url,data=data,files=files)
    # print(respose.text)
    data=json.loads(respose.text)
    img=cv2.imread(img_path)
    face_rectangle=data["faces"][0]["face_rectangle"]
    x=face_rectangle["left"]
    y=face_rectangle["top"]
    w=face_rectangle["width"]
    h=face_rectangle["height"]
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    attr=data["faces"][0]["attributes"]
    gender=attr["gender"]["value"]
    beauty=(attr["beauty"]["female_score"]+attr["beauty"]["male_score"])//2
    text="{0},score:{1}".format(gender,beauty)
    cv2.putText(img,text,(x-30,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imshow("xiao",img)
    cv2.waitKey(0)
face_detect("E:\\AIChangingFace\\trysomethon\\gakki.jpg")
