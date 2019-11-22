import requests

url = "http://www.renren.com/PLogin.do"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}
data = {
    "email": "17695427525",
    "password": "13032206430x2.20"
}
response = requests.post(url=url, headers=headers, data=data).content.decode("utf-8")
with open("renren.html", "w", encoding="utf-8") as fp:
    fp.write(response)
