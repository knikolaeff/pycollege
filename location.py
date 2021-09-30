import requests


def get_location():
    ip = requests.get("http://jsonip.com").json()["ip"]
    jsondata = requests.get("http://ip-api.com/json/" + ip).json()
    return jsondata


print(get_location())