import requests
import time
import re


def get_proxy_addr():
    # url = 'https://api.xiaoxiangdaili.com/ip/get?appKey=945513382088691712&appSecret=EYqvzSjd&cnt=&wt=text'
    # url='https://proxy.qg.net/extract?Key=C061F259&Num=1&AreaId=&Isp=&DataFormat=txt&DataSeparator=%5Cr%5Cn&Detail=0&Pool=1'
    url = 'https://mobile.huashengdaili.com/servers.php?session=U135b5de30222131510--cb1081e4c796834e867fee06f01e2aaa&time=3&count=1&type=text&only=1&province=330000&pw=no&protocol=http&separator=1&ip_type=tunnel'
    url = 'https://mobile.huashengdaili.com/servers.php?session=U135b5de30222131510--cb1081e4c796834e867fee06f01e2aaa&time=1&count=1&type=text&only=1&province=310000&city=310100&pw=no&protocol=http&separator=1&province_arr=310000,320000,330000&ip_type=direct'
    addr = requests.get(url).text  # 返回一个消息实体
    return addr
