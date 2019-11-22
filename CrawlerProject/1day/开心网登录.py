import requests
url = "https://security.kaixin001.com/login/login_post.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}
data = {
    "loginemail": "17695427525",
    "password": "13032206430x2.20"
}
response = requests.post(url=url, headers=headers, data=data).content.decode("utf-8")
with open("kaixin.html", "w", encoding="utf-8") as pf:
    pf.write(response)
