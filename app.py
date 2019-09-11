import introduce
import helper
import function
import url
import browerConfig
import time
import re
from bs4 import BeautifulSoup
import timer
import userConfig
import jscode
import threading

if __name__ == "__main__":
    introduce.initDesc()
    helper.initTry()
    session = userConfig.userInfo()
    firstTime = time.time()
    result = function.myWork(url.pageIndex,browerConfig.initPageIndex(firstTime,session))
    if("您好" in result):
        helper.succeed("成功渗透选座系统")
    else:
        helper.failed("渗透选座系统失败")
    html = function.myWork(url.pageCenter,browerConfig.initPageIndex(firstTime,session))
    soup = BeautifulSoup(html, "html.parser")
    print("您的个人信息如下：")
    for k in soup.find_all('div', class_='nick'):
        print("您的系统昵称：" + k.string)
    for k in soup.find_all('div', class_='userinfo'):
        print(str(k).replace("</div>", "").replace('<div class="userinfo" data-href="/index.php/times/index.html">', "")
              .replace('<div class="nick">', "用户名：").replace('<div class="study-detail">', "").replace("<div>", "")
              .replace('<div class="bg">', "").replace("学习时间", "：学习时间").replace("排名", "：排名").replace("单日最长", "：单日最长")
              .replace("\t", ""))
    print("核对信息中...,开始继续执行！")
    # 完成
    if (timer.timer_setting()):
        secondTime = time.time()
        # 修改选座页面
        Jsresult = function.myWork(url.pageIndex, browerConfig.initPageIndex(secondTime, session))
        #开始拉去js验证码
        js_url = jscode.obtain_js(Jsresult)
        js_code = ''
        try:
            js_code = js_url[1]
        except Exception  as e:
            print("Session 值错误，检查重试！")
        need_js = re.findall(r"layout/(.+?).js", js_code)
        print("验证码已获取：" + need_js[0])
        js_yzm = jscode.js_code.get(need_js[0])
        print("动态验证码已捕获：" + str(js_yzm))

        if js_yzm == None:
            helper.failed("验证码系统未初始化，请重新执行！")
            #exit(-1)
        #下载图片验证码
        t = threading.Thread(target=function.downloadImage(str(secondTime),session))
        t.setDaemon(True)
        t.start()
        t.join()
        #初始化百度验证码识别功能
        client = function.initBaidu();
        """ 读取图片 """
        image = function.get_file_content('来选座验证码.jpg')
        yzm = function.optical(client, image)

        for i in range(1,15):
            if len(str(yzm)) != 4:
                # 下载图片验证码
                t = threading.Thread(target=function.downloadImage(str(secondTime),session))
                t.setDaemon(True)
                t.start()
                t.join()
                print("验证码识别为：" + str(len(str(yzm))) + "个字符，与系统不匹配，默认开始继续识别！"+"第"+str(i)+"次识别")
                image = function.get_file_content('来选座验证码.jpg')
                yzm = function.optical(client, image)
                print("来选座系统验证码自动识别为：" + yzm)
            else:
                break

        yzm = function.optical(client, image)
        print("来选座系统验证码自动识别为：" + yzm)
        result = function.myWork(url.pageBook,browerConfig.initBook(firstTime,session))
        print("选座结果"+result)