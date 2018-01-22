
# coding:UTF-8
# version python3

"""
用于分析nginx access log
"""

import os
import re
import time
import urllib.parse
import util.WebUtil

# $remote_addr, $http_x_forwarded_for（反向） 记录客户端IP地址
REG_REMOTE_ADD = "?P<remote_add>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
# $remote_user 记录客户端用户名称
REG_REMOTE_USER = "?P<remote_user>\w{2,20}"
# $request 记录请求的URL和HTTP协议
REG_REQUEST = "\"(?P<method>(GET|POST|DELETE|PUT|HEAD))\s+(?P<request>\S{1,})\s+HTTP/\d.\d\""
# $status 记录请求状态
REG_STATUS = "?P<status>\d{3}"
# $body_bytes_sent 发送给客户端的字节数，不包括响应头的大小； 该变量与Apache模块mod_log_config里的“%B”参数兼容。
REG_BODY_BYTES_SEND = "?P<body_bytes_send>\d{1,10}"
# $bytes_sent 发送给客户端的总字节数。
REG_BYTES_SEND = "?P<bytes_send>\d{1,}"
# $connection 连接的序列号。
REG_CONNECTION = "\d{1,}"
# $connection_requests 当前通过一个连接获得的请求数量。
REG_CONNECTION_REQUESTS = ""
# $msec 日志写入时间。单位为秒，精度是毫秒。
# $pipe 如果请求是通过HTTP流水线(pipelined)发送，pipe值为“p”，否则为“.”。
REG_PIPE = ""
# $http_referer 记录从哪个页面链接访问过来的
REG_REFERER = "?P<referer>\"\S{0,}\""
# $http_user_agent 记录客户端浏览器相关信息
REG_USER_AGENT = "?P<userAgent>\".*\""
# $request_length 请求的长度（包括请求行，请求头和请求正文）。
REG_REQUEST_LENGTH = ""
# $request_time 请求处理时间，单位为秒，精度毫秒； 从读入客户端的第一个字节开始，直到把最后一个字符发送给客户端后进行日志写入为止。
REG_REQUEST_TIME = "?P<request_time>\d{1,}"
# $time_iso8601 ISO8601标准格式下的本地时间。
REG_TIME_ISO8601 = ""
# $time_local 通用日志格式下的本地时间。
REG_TIME_LOCAL = "?P<time>\[\d{1,2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s+\+0800\]"


def format_datetime(date):
    """用户格式话nginx access访问日子的时间"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(date, '%d/%b/%Y:%H:%M:%S +0800'))


def parse_logfile(file_path, encoding, pattern):
    """用于解析一个日志文件"""
    print("INFO:process file %s" % file_path)
    with open(file_path, 'rt', encoding=encoding) as ff:
        for line in ff.readlines():
            line = urllib.parse.unquote(line).strip()

            matchs = pattern.match(line)
            if matchs is not None:
                ip = matchs.group('remote_add')
                requesttime = format_datetime(matchs.group('time').replace('[', '').replace(']', ''))
                method = matchs.group('method')
                request = matchs.group('method')
                status = matchs.group('status')
                sends = matchs.group('bytes_send')
                referer = matchs.group('referer')
                userAgent = util.WebUtil.user_agent(matchs.group('userAgent'))

                info = {"ip": ip, "time": requesttime, 'method': method, "request": request, "status": status,
                        "sends": sends, "referer": referer, "userAgent": userAgent}

                print(info)
            else:
                print("patter not match :%s" % line)


if __name__ == '__main__':

    nginxAccessPattern = u"(%s)\s+-\s+-\s+(%s)\s+%s\s+(%s)\s+(%s)\s+(%s)\s+(%s)" \
                         % (REG_REMOTE_ADD, REG_TIME_LOCAL, REG_REQUEST, REG_STATUS, REG_BYTES_SEND, REG_REFERER,
                            REG_USER_AGENT)
    print("nginx access log pattern :%s " % nginxAccessPattern)
    RE_nginxAccessPattern = re.compile(nginxAccessPattern, re.VERBOSE)

    path = "/data/nginx_accesslog/"
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            parse_logfile(filepath, 'us-ascii', RE_nginxAccessPattern)
