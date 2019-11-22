import requests


proxies = {
    "https": "117.69.24.223:42670",
    "http": "124.113.217.5:9999"
}
url = "https://www.xicidaili.com/?=2rn"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}
response = requests.get(url=url, headers=headers, proxies=proxies).content.decode("utf-8")
print(response)
# with open("daili.html", "w", encoding="utf-8") as pf:
#     pf.write(response)