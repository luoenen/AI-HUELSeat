def initGetNameVerify():
    header = {
        "Host": "wechat.laixuanzuo.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116"
                      " Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501"
                      " NetType/WIFI WindowsWechat",
        "Accept": "image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
        "Referer":"https://wechat.laixuanzuo.com/index.php/prereserve/index.html",
        "Accept-Encoding": "br, gzip, deflate",
        "Accept-Language": "zh-CN",
        "Cookie": "",

    }
    return header


import requests

url = 'https://wechat.laixuanzuo.com/index.php/misc/verify.html'

result = requests.get(url,headers=initGetNameVerify())
print("状态码：")
print(result.status_code)
print("\n")
print("返回体：")
print(result.text)
print("\n")