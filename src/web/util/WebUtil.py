
# encoding=UTF-8

"""实现一些Web相关的工具类"""
import re

WEBUTIL_OSNAME = re.compile(
    u"(\s+Android[\s/]+[\d.]{2,6})|(\s+iPhone\s+OS\s+[\d_.]{2,8}\s+)|(Windows\s+NT\s+[\d.]{2,8})|"
    u"(Mac\s+OS\s+X\s+[\d_.]{2,8})|(Windows\s+XP)|(iPhone;\s+[\w\s\d.]{2,14})|(Linux\s+[\w\d_.]{2,8})|"
    u"(OS\s+[\d_.]{2,8})|(Linux;[\s\w]+Xhrome\s+[\d_.]{2,8})"

)

WEBUTIL_SPIDER = ['spider', 'Baiduspider', 'Googlebot', '360Spider', 'bingbot', 'Yahoo', 'iaskspider', 'YodaoBot',
                  'msnbot', 'libcurl-agent', 'CFNetwork', 'okhttp', 'urllib', 'Python-urllib', 'HttpClient',
                  'Go-http-client', 'AHC', 'masscan']
# 一些相对正常的请求，如支付宝回调 微信回调
WEBUTIL_BOT = ['Mozilla/4.0']


def user_agent(userAgent):
    """parse useragent"""
    for bot in WEBUTIL_BOT:
        if bot.lower() == userAgent.lower():
            return {"os_name": "bot", "os_product": bot, "webkit": "", "version": "", "os_browser": ""}

    for spider in WEBUTIL_SPIDER:
        if spider.lower() in userAgent.lower() or spider.lower() == userAgent.lower():
            return {"os_name": "spider", "os_product": spider, "webkit": "", "version": "", "os_browser": ""}

    os_name = 'unkown'
    os_temp = WEBUTIL_OSNAME.findall(userAgent)
    if os_temp:
        os_name = os_temp[0]

    return {"os_name": os_name, "os_product": "unkown", "webkit": "unkown", "version": "unkown",
            "os_browser": "unkown"}
