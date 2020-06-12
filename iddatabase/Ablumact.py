import requests
import json
def create_album():
    http_url = "https://api-cn.faceplusplus.com/imagepp/v1/facealbum/createalbum"
    data = {
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM"
    }
    respose=requests.post(http_url,data=data)
    data=json.loads(respose.text)
    return data["facealbum_token"]
def delete_album(ablum_token):
    http_url = "https://api-cn.faceplusplus.com/imagepp/v1/facealbum/deletealbum"
    data = {
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "facealbum_token":ablum_token
    }
    respose=requests.post(http_url,data=data)
    data=json.loads(respose.text)
    return data

def find_facealbums(sta=1):
    http_url="https://api-cn.faceplusplus.com/imagepp/v1/facealbum/getfacealbums"
    data={
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "start":sta
    }
    respose=requests.post(http_url,data=data)
    data=json.loads(respose.text)
    print(data)
    return data
def find_albumdetail(facealbum_token,sta=1):
    http_url = "https://api-cn.faceplusplus.com/imagepp/v1/facealbum/getalbumdetail"
    data = {
        "api_key": "0QMbprc9PjUFpUuDM-Dea_uB4fL_QhNE",
        "api_secret": "miaBYP2j66n81meWzDjiDHudsp6_MVzM",
        "facealbum_token":facealbum_token,
        "start": sta
    }
    respose = requests.post(http_url, data=data)
    data = json.loads(respose.text)
    return data
# print(create_album())
# delete_album("1577420216-ffd9bbca-93e1-461f-9418-91023307c1c1")
# facealbum_token=create_album()
# print(facealbum_token)
