import requests
import os
from configobj import ConfigObj
import json
import time

spath = os.path.split(__file__)[0]

class DObj:
    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigObj(filename, encoding='UTF8')

    def readobj(self, section, item, default: str = "") -> str:
        config = self.config
        try:
            res = config[section][item]
        except:
            res = default
        return res

    def writeobj(self, section, item, value):
        if section not in self.config:
            self.config[section] = {}
        self.config[section][item] = value
        self.config.write()


def user_search(username):
    url = f"https://api.bilibili.com/x/web-interface/search/type?search_type=bili_user&keyword={username}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text

def get_user_following_list(vmid, ps=50, pn=1):
    url = f"http://api.bilibili.com/x/relation/followings?vmid={vmid}&ps={ps}&pn={pn}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text

def get_biliuser_info(mid):
    url = f"http://api.bilibili.com/x/space/acc/info?mid={mid}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text

def get_all_vtb_info():
    if not os.path.isdir(f"{spath}/cache"):
        os.mkdir(f"{spath}/cache")

    config = DObj(f"{spath}/cache/cache.ini")
    last_time = int(config.readobj("cache", "last_update_time", "0"))
    time_now = int(time.time())
    if time_now - last_time > 600:
        url = "https://api.vtbs.moe/v1/info"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        proxies = {
            'http': f'127.0.0.1:10087',
            'https': f'127.0.0.1:10087'
        }
        '''
        proxies = {
            'http': f'{sets.BotBaseSettings.Proxy.host}:{sets.BotBaseSettings.Proxy.port}',
            'https': f'{sets.BotBaseSettings.Proxy.host}:{sets.BotBaseSettings.Proxy.port}'
        }
        '''
        response = requests.request("GET", url, headers=headers, proxies=proxies)
        try:
            data = json.loads(response.text)
            if type(data) == list:
                if len(data) > 1000:
                    with open(f"{spath}/cache/vtb_data_simple.json", "w", encoding="utf8") as f:
                        f.write(response.text)
                    config.writeobj("cache", "last_update_time", str(int(time.time())))
        except Exception as e:
            print(e)
        return response.text
    else:
        print("检测到有效缓存")
        with open(f"{spath}/cache/vtb_data_simple.json", "r", encoding="utf8") as f:
            return f.read()
