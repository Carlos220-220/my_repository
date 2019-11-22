import requests
import json

url = "https://fanyi.baidu.com/sug"
def fanyi(kw):
    data = {"kw": kw}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    response = requests.post(url=url, headers=headers, data=data).content.decode("utf-8")

    response = json.loads(response)
    for i in response["data"]:
        word = i["k"]
        translate = i["v"]

        with open("fanyi.txt","a", encoding="utf-8") as pf:
            pf.write(word+":"+translate+"\n")
    print(response)
if __name__ == '__main__':
    while True:
        kw = input("请输入翻译的单词")
        fanyi(kw)