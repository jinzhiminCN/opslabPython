
# coding=utf-8

# @descript: parser url in python
import sys
import urllib
from urllib.parse import urlparse


ljust = 15
print("""url's standard formart:
    \t scheme://username:password@xx.xx.com:port/pathname/filename?query=value#fargment""")


def demo_parseurl():
    url1 = "http://www.baidu.com"
    print("======================================================")
    print("url:" + url1)
    r = urlparse(url1)
    print("r's type->", type(r))
    print(r)
    print("scheme:".ljust(ljust), r.scheme)
    print("netloc:".ljust(ljust), r.netloc)
    print("path:".ljust(ljust), r.path)
    print("params:".ljust(ljust), r.params)
    print("query:".ljust(ljust), r.query)
    print("fragment:".ljust(ljust), r.fragment)
    print("username:".ljust(ljust), r.username)
    print("password:".ljust(ljust), r.password)
    print("hostname:".ljust(ljust), r.hostname)
    print("port:".ljust(ljust), r.port)

    print("====================================================")
    wsl_url1 = "http://www.baidu.com:login.php@www.qq.com/login.jsp?user=1234&suid=fasfjasklfjw"
    print("url:" + wsl_url1)
    wsl = urlparse(wsl_url1)
    print("wsl's type->", type(r))
    print(wsl)
    print("scheme:".ljust(ljust), wsl.scheme)
    print("netloc:".ljust(ljust), wsl.netloc)
    print("path:".ljust(ljust), wsl.path)
    print("params:".ljust(ljust), wsl.params)
    print("query:".ljust(ljust), wsl.query)
    print("fragment:".ljust(ljust), wsl.fragment)
    print("username:".ljust(ljust), wsl.username)
    print("password:".ljust(ljust), wsl.password)
    print("hostname:".ljust(ljust), wsl.hostname)
    print("port:".ljust(ljust), wsl.port)


# ==========================================================================================
# @join-url
# @descript：由于URL可以分成多个部分，所以有时就需要对URL进行拼接，可以使用urlparse
# 模块中的urljoin方法将其进行拼接。urljoin方法有俩个参数，一个是绝对地址，另外一个是相对地址，
# 直接调用此函数，将产生一个URL字符串.
# ==========================================================================================
def demo_join():
    print("演示如何拼接URL字符串")
    hostname = "http://www.baidu.com"
    pathname = "/v2/?login&tpl=mn"
    url = urllib.parse.urljoin(hostname, pathname)
    print(url)

    # 如果第二个参数及相对地址有指定协议优先使用
    url = urllib.parse.urljoin("http://www.baidu.com/", "ftp://www.baidu.com/index.html")
    print(url)


# ==========================================================================================
# @urlsplit
# urlsplit方法可以用来对于URL进行分解。其函数原型和urlparse类似，也接收一个字符串。
# 然后给出一个元组。与urlparse的方法结果相比。这里的结果少了param参数
# ==========================================================================================
def demo_split():
    url = "http://zz.xxx.com/tools/admin.php?user=admin&password=xxx"
    res = urllib.parse.urlsplit(url)
    print(res)
    print(urllib.parse.urlunsplit(res))


# ==========================================================================================
# @encode
# @descript：演示各种URL的加密与解密
# ==========================================================================================
def demo_decodeURL():

    print("使用urllib的还函数对url进行编码和解码")
    print("编码:quote/quote_safe")
    print("解码:unquote/unquote_safe")
    print("python 3.0 不支持 urllib.quote()")
    print("改成了下面：编码　：urllib.parse.quote(s)解码 ：urllib.parse.unquote(s)")

    host = "http://www.baidu.com/#wd="
    url1 = host + urllib.parse.quote("和尚")
    url2 = host + urllib.parse.quote("和尚 尼姑")
    url3 = host + urllib.parse.quote_plus("和尚  尼姑 ")
    print(url1)
    print(url2)
    print(url3)

    unurl1 = urllib.parse.unquote(url1)
    unurl2 = urllib.parse.unquote(url2)
    unurl3 = urllib.parse.unquote(url3)
    unurl4 = urllib.parse.unquote_plus(url3)
    print(unurl1)
    print(unurl2)
    print(unurl3)
    print(unurl4)

    print("利用urlencode对查询参数进行编码")
    print("因为list和字典都是无序的所以结果不一样，但是在url请求中的效果是一样的")
    params = [('entryid', '10000'), ('userid', 'admin'), ('note', 'python笔记')]
    url_query = urllib.parse.urlencode(params)
    print(url_query)

    params = ({'entryid': '10000', 'userid': 'admin', 'note': 'python笔记'})
    url_query = urllib.parse.urlencode(params)
    print(url_query)

    params = [('entryid', ['100001', '19999', '222222'])]
    print(urllib.parse.urlencode(params))
    print(urllib.parse.urlencode(params, True))


# ==========================================================================================
# @handlerUrl
# 一个综合的url处理演示
# ==========================================================================================
def demo_handlerURL():
    list_res = []
    list_host = ['http://www.baidu.com',
                 'http://www.qq.com',
                 'http://www.163.com',
                 'http://www.jd.com']
    list_admin = ['admin.php',
                  'admin.jsp',
                  'admin.aspx',
                  '/admin/admin.php',
                  '/admin/admin.jsp']

    list_url = []
    for host in list_host:
        for admin in list_admin:
            list_url.append(urllib.parse.urljoin(host, admin))

    for url in list_url:
        scheme, netloc, path, query, fragment = urllib.parse.urlsplit(url)
        scheme = 'http'
        list_res.append(urllib.parse.urlunsplit((scheme, netloc, path, query, fragment)))

    for strs in list_res:
        print(strs)


# ==========================================================================================
# @base64
# 演示base64编码URL与解码URL
# ==========================================================================================
def demo_base64():
    import base64

    print("""在python中使用base64编码和解码是非常容易的.只需import base64
    然后直接使用encodestring()和decodestring()就可以如果用于除了URL则可以使用
    urlsafe_b64encode()和urlsafe_b64decode（）""")

    url = '''http://www.baidu.com/404.html?a=%24_%3Dstrrev%28edoced_46es
    ab%29%3B%40eval%28%24_%28%24_POST%5Bz0%5D%29%29%3B
    &z0=QGV2YWwoYmFzZTY0X2RlY29kZSgnYVdZb0pGOURU
    MDlMU1VWYkoweDVhMlVuWFNFOU1TbDdjMlYwWTI5dmEybGxLQ2RNZVd0bEp5d3hLVH
    RBWm1sc1pTZ25hSFIwY0RvdkwzZDNkeTVuYjI5a1pHOW5MbWx1TDBGd2FTNXdhSEEv
    VlhKc1BTY3VKRjlUUlZKV1JWSmJKMGhVVkZCZlNFOVRWQ2RkTGlSZlUwVlNWa1ZTV3
    lkU1JWRlZSVk5VWDFWU1NTZGRMaWNtVUdGemN6MG5MbXRsZVNna1gxQlBVMVFwS1R0O
    ScpKTtAaW5pX3NldCgiZGlzcGxheV9lcnJvcnMiLCIwIik7QHNldF90aW1lX2xpbWl0
    KDApO0BzZXRfbWFnaWNfcXVvdGVzX3J1bnRpbWUoMCk7ZWNobygiLT58Iik7OyREPWR
    pcm5hbWUoJF9TRVJWRVJbIlNDUklQVF9GSUxFTkFNRSJdKTtpZigkRD09IiIpJEQ9ZG
    lybmFtZSgkX1NFUlZFUlsiUEFUSF9UUkFOU0xBVEVEIl0pOyRSPSJ7JER9XHQiO2lmK
    HN1YnN0cigkRCwwLDEpIT0iLyIpe2ZvcmVhY2gocmFuZ2UoIkEiLCJaIikgYXMgJEwp
    aWYoaXNfZGlyKCJ7JEx9OiIpKSRSLj0ieyRMfToiO30kUi49Ilx0IjskdT0oZnVuY3R
    pb25fZXhpc3RzKCdwb3NpeF9nZXRlZ2lkJykpP0Bwb3NpeF9nZXRwd3VpZChAcG9zaX
    hfZ2V0ZXVpZCgpKTonJzskdXNyPSgkdSk%2FJHVbJ25hbWUnXTpAZ2V0X2N1cnJlbnR
    fdXNlcigpOyRSLj1waHBfdW5hbWUoKTskUi49Iih7JHVzcn0pIjtwcmludCAkUjs7ZW
    NobygifDwtIik7ZGllKCk7'''

    print("原始URL：\n" + url)
    url = urllib.unquote(url)
    print("经过urldecode解码后:\n" + url)
    index = url.rfind("=")
    url = url[:index + 1] + base64.urlsafe_b64decode(url[index + 1:])
    print("经过base64解码后:\n" + url)
    print("请继续base64.urlsafe_b64decode你会发现一个秘密")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        selfMod = __import__(__name__)
        return_function = getattr(selfMod, "demo_%s" % sys.argv[1])
        if (callable(selfMod.return_function)):
            return_function()
    else:
        print("""help:
        self.py parseurl".ljust(30), "演示如何解析url
        *.py  join".ljust(30), "合并url
        *.py  split".ljust(30), "拆分URL
        *.py  decodeURL".ljust(30), "解码URL
        *.py  handlerURL".ljust(30), "一个处理URL的例子
        *.py  base64".ljust(30), "一个BASE64编码的URL实例""")

        demo_parseurl()
        demo_join()

        demo_split()

        demo_decodeURL()

        demo_handlerURL()

        demo_base64()