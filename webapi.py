import requests
# 阿里云服务器地址
server = "http://121.40.62.199:8080/"


def get_user():
    url = server + "get_user"
    res = get_res(url)
    return res


def insert_user(userid):
    url = server + "insert_user?uid=" + userid
    res = get_res(url)
    return res


def update_user(username, fans, p1, p2, p3, p4, desc, id):
    url = server + "update_user?" + "username=" + username + "&fans=" + str(fans) + "&p1=" + str(p1) + "&p2=" + str(
        p2) + "&p3=" + str(p3) + "&p4=" + str(p4) + "&desc=" + desc + "&id=" + id
    res = get_res(url)
    return res


def get_res(url):
    try:
        res = requests.get(url).text  # 返回一个消息实体
    except:
        print('检查阿里云服务器')
        return -1
    return res
