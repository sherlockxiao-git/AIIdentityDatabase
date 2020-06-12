import requests
import json
def update_face(facealbum_token,face_tokens,group_id):
    http_url="https://api-cn.faceplusplus.com/imagepp/v1/facealbum/updateface"
    data={
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "facealbum_token": facealbum_token,
        "new_group_id":group_id,
        "face_tokens":face_tokens
    }
    respose = requests.post(http_url, data=data)
    data = json.loads(respose.text)
    return data
def group_face(facealbum_token,operation_type="incremental"):
    http_url="https://api-cn.faceplusplus.com/imagepp/v1/facealbum/groupface"
    data={
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "facealbum_token": facealbum_token,
        "operation_type": operation_type
    }
    respose = requests.post(http_url, data=data)
    data = json.loads(respose.text)
    http_url="https://api-cn.faceplusplus.com/imagepp/v1/facealbum/groupfacetaskquery"
    result = {
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "task_id":data["task_id"]
    }
    respose = requests.post(http_url, data=result)
    result= json.loads(respose.text)
    return result
def delete_face(facealbum_token,image_id):
    http_url = "https://api-cn.faceplusplus.com/imagepp/v1/facealbum/deleteface"
    data = {
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "facealbum_token": facealbum_token,
        "image_id": image_id
    }
    respose = requests.post(http_url, data=data)
    data = json.loads(respose.text)
    return data

# delete_face('1577372360-35df51c8-ff6a-410f-9621-3e57b1af3005','e0cac2226b16cdf69ce0047c261f7dfc')