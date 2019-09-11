import requests
import browerConfig

def myWork(url,config):
    return requests.get(url=url,headers=config,verify=False).text;

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
                return fp.read()

def initBaidu():
    from aip import AipOcr

    """ 你的 APPID AK SK """
    APP_ID = '17220116'
    API_KEY = 'yGvGkDYSoyq43d1dlT2pTctz'
    SECRET_KEY = 'aMTh2kL6SxmUzuX7khQsPGq5ssSxKgoK'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    return client

def optical(client,image):
    """ 调用通用文字识别（高精度版） """
    client.basicAccurate(image);
    """ 如果有可选参数 """
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"
    print("开始加载图像验证码人工智能视觉识别技术，请保持网络链接...")
    yzm = client.basicAccurate(image, options).get("words_result")[0].get("words")
    return str(yzm).replace(" ", "")

def downloadImage(time,session):
    image = 'http://wechat.laixuanzuo.com/index.php/misc/verify.html'
    image = requests.get(image, browerConfig.initImage(str(time), session)).content
    with open('来选座验证码' + '.jpg', 'wb') as f:
        f.write(image)
        f.flush()
        f.close()
