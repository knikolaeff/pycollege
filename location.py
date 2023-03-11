import requests


def get_location():
    ip = requests.get("http://jsonip.com").json()["ip"]
    return requests.get(f"http://ip-api.com/json/{ip}").json()


print(get_location())