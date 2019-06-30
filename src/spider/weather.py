#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import json
import logging
import requests
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=1)
def get_weather_info():
    arr = [
        "101010100",    #北京
        "101150101"     #西宁
        ]
    try:
        # 获取API信息
        weather = requests.get('http://t.weather.sojson.com/api/weather/city/')
        w = weather.json().get('data').get('forecast')[1]
        # 格式化天气消息
        today_weather = "今日天气：\n温度：%s/%s\n%s:%s\n空气指数：%s\n日出时间：%s\n日落时间：%s\n天气：%s\n%s" % \
                        (w.get('low'), w.get('high'), w.get('fx'), w.get('fl'),
                         w.get('aqi'), w.get('sunrise'), w.get('sunset'), w.get('type'), w.get('notice'))
        # 发送格式化后天气
        print(today_weather)
    except Exception as e:
        logging.warning(e)
        logging.warning('天气发送失败！')