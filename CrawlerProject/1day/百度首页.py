import requests


#   1.给出url
# url = 'https://www.baidu.com'
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%80%81%E6%8C%9D%E5%8F%91%E7%94%9F6%E7%BA%A7%E5%9C%B0%E9%9C%87&oq=%25E7%259A%2587%25E5%25AE%25A4%25E6%2588%2598%25E4%25BA%2589&rsv_pq=a168a6f900014b3a&rsv_t=0657eB0GXYzcHWhhRGIwFoxLbRxrovJu4Hbw37vWkpLqRxLZ8KeH9gOETsI&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_n=2&rsv_sug3=1&bs=%E7%9A%87%E5%AE%A4%E6%88%98%E4%BA%89"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}

#   2.请求方式
        #   request methods : get

#   3.发起请求
response = requests.get(url=url,headers=headers)
print(response)


#   4.查看响应内容
    #   (1) response.text : 返回文本信息
print(response.text)

    #   (2) response.content : 返回字节流信息   + .decode('gbk')
print(response.content.decode('utf-8'))


#   5. 写入本地文件
with open('baidu.html','w',encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))