import requests
import json
import base64
import cv2
def find_face(img_path):
    http_url="https://api-cn.faceplusplus.com/facepp/v3/detect"
    data = {
            "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
            "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM"
            }
    files={"image_file":open(img_path,"rb")}
    respose=requests.post(http_url,data=data,files=files)
    data=json.loads(respose.text)
    return data["faces"][0]["face_rectangle"]
def merge_face(image_template,image_merge,image_result,number):
    ff1=find_face(image_template)
    ff2=find_face(image_merge)
    rectangle1="{0},{1},{2},{3}".format(ff1["top"],
                                        ff1["left"],
                                        ff1["width"],
                                        ff1["height"])
    rectangle2 = "{0},{1},{2},{3}".format(ff2["top"],
                                          ff2["left"],
                                          ff2["width"],
                                          ff2["height"])
    url_add="https://api-cn.faceplusplus.com/imagepp/v1/mergeface"
    f1=open(image_template,"rb")
    f1_64=base64.b64encode(f1.read())
    f1.close()
    f2 = open(image_merge, "rb")
    f2_64 = base64.b64encode(f2.read())
    f2.close()
    data={
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "template_base64":f1_64,
        "template_rectangle":rectangle1,
        "merge_base64": f2_64,
        "merge_rectangle": rectangle2,
        "merge_number":number
    }
    response=requests.post(url_add,data=data)
    data=json.loads(response.text)
    result=data["result"]
    imgdata=base64.b64decode(result)
    file=open(image_result,"wb")
    file.write(imgdata)
    file.close()
