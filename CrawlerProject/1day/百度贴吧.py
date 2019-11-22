import requests

kw = input("请输入贴吧名")
url = "http://tieba.baidu.com/f?kw={}&ie=utf-8&pn=".format(kw)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}

for page in range(10):
    ful_url = url + str(page * 50)
    response = requests.get(url=ful_url, headers=headers).content.decode("utf-8")

    with open("tieba{}.html".format(page + 1), "w", encoding="utf-8") as pf:
        pf.write(response)
