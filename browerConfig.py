
def initPageIndex(solidtime,session):
    header = {
        "Host":"wechat.laixuanzuo.com",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Cookie":"Hm_lpvt_7838cef374eb966ae9ff502c68d6f098="+str(solidtime)+";"
                 " Hm_lvt_7838cef374eb966ae9ff502c68d6f098="+str(solidtime)+";"
                 " FROM_TYPE=weixin; wechatSESS_ID="+(str(session))+"",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko)"
                     " MicroMessenger/2.3.26(0x12031a10) MacWechat NetType/WIFI WindowsWechat",
        "Accept-Language":"zh-cn",
        "Accept-Encoding":"br, gzip, deflate",
        "Connection":"keep-alive"
    }

    return header

def initPagePre(time,solidtime,session):
    header = {
        "Host": "wechat.laixuanzuo.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=" + str(time) + ";"
                                                                            " Hm_lvt_7838cef374eb966ae9ff502c68d6f098=" + str(
            solidtime) + ";"
                    " FROM_TYPE=weixin; wechatSESS_ID=" + (str(session)) + "",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko)"
                      " MicroMessenger/2.3.26(0x12031a10) MacWechat NetType/WIFI WindowsWechat",
        "Accept-Language": "zh-cn",
        "Referer":"https://wechat.laixuanzuo.com/index.php/reserve/index.html",
        "Accept-Encoding": "br, gzip, deflate"
    }

    return header

def initImage(time,session):
    header = {
            "Host": "wechat.laixuanzuo.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116"
                          " Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501"
                          " NetType/WIFI WindowsWechat",
            "Accept": "image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
            "Accept-Encoding": "br, gzip, deflate",
            "Refer": "https://wechat.laixuanzuo.com/index.php/prereserve/index.html",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
            "Cookie": "wechatSESS_ID=" + session + "; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=" + str(time)
                      + "; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=" + time + "",
        }
    return header

def initBook(time,session):
    header = {
        "Host": "wechat.laixuanzuo.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Encoding": "gzip, deflate",
        "Refer": "https://wechat.laixuanzuo.com/index.php/reserve/layoutApi/action=prereserve_event&libid=11117",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
        "Cookie": "wechatSESS_ID=" + session + "; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=" + str(time) + "; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=" + str(time) + "",
    }
    return header

def initGetNameVerify(time,session):
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
        "Cookie": "wechatSESS_ID=" + session + "; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=" + str(
            time) + "; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=" + str(time) + "",

    }
    return header

def initImageWithName(time):
    header = {
        "Host": "static.wechat.laixuanzuo.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116"
                      " Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501"
                      " NetType/WIFI WindowsWechat",
        "Accept": "image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
        "Accept-Encoding": "br, gzip, deflate",
        "Accept-Language": "zh-CN",
        "Cookie": "Hm_lvt_7838cef374eb966ae9ff502c68d6f098=" + str(
            time)
                  + "; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=" + time + "",
    }
    return header