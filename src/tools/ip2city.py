#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon


import requests
import json
import time


res = open('C:/Users/Administrator/Desktop/222.txt','a+')

with open('C:/Users/Administrator/Desktop/111.txt') as ff:
	for line in ff.readlines():
		try:
			line=line.strip('\n') 
			tt = line.split(",")

			url = "http://ip.taobao.com/service/getIpInfo.php?ip="+str(tt[0]).replace("\"","")
			r = requests.get(url)
			json_response = r.content.decode()
			print(url +"-->"+json_response)
			dict_json = json.loads(json_response)

			if dict_json['code'] == 0:
				address = dict_json['data']['country']+"/"+dict_json['data']['region']+"/"+dict_json['data']['city']
				yys = dict_json['data']['isp']
				
				line += ",\""+address+"\",\""+yys+"\""
			
			time.sleep(1)
		except Exception as e:
			# traceback.print_exc()
			pass
		finally:
			res.write(line+"\n")	
			
		
