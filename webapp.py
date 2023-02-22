import web
import db
import os
import chardet

urls = (
    '/get_user', 'GetUser',
    '/update_user', 'UpdateUser',
    '/', 'Index',
    '/list', 'List',
    '/insert_user', 'InsertUser'

)

# 获得一个未爬的用户
class GetUser:
    def GET(self):
        params = web.input()
        ip = web.ctx.env.get('REMOTE_ADDR')
        print("get_user from " + ip)
        uid = db.get_user()
        return uid

# 更新爬好的数据
class UpdateUser:
    def GET(self):
        params = web.input()
        username = params.get('username')
        fans = params.get('fans')
        p1 = params.get('p1')
        p2 = params.get('p2')
        p3 = params.get('p3')
        p4 = params.get('p4')
        desc = params.get('desc')
        uid = params.get('id')
        ip = web.ctx.env.get('REMOTE_ADDR')
        print("update from " + ip + "id " + uid)
        return db.update_user(username, fans, p1, p2, p3, p4, desc, uid)

# 增加一个新用户
class InsertUser:
    def GET(self):
        params = web.input()
        uid = params.get('uid')
        ip = web.ctx.env.get('REMOTE_ADDR')
        print("insert from " + ip + "para " + uid)
        return db.insert_user(uid)

# Just for test
class Index:
    def GET(self):
        info=db.get_data_info()
        return "<HTML><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0,maximum-scale=1.0, user-scalable=no\"/><CENTER><H1>Hello to my XHS APP</H1><H2>ALL NUM: "+str(info[0])+"</H2> <H2>Finished: "+str(info[1])+"</H2></CENTER></HTML>"

# 随机获得一个可投放的ID
class List:
    def GET(self):
        ip = web.ctx.env.get('REMOTE_ADDR')
        print("list from " + ip)
        # f=open('list.html', encoding='gbk')
        # doc=f.read()

        with open('list.html', 'rb') as f:
            doc = f.read()
            encoding = chardet.detect(doc)['encoding']
        doc = doc.decode(encoding)
        info = db.get_user_list()
        doc = doc.replace('arg1', str(info[1]))
        # print(info[2])
        doc = doc.replace('arg2', str(info[2]))
        doc = doc.replace('arg3', str(info[3]))
        doc = doc.replace('arg4', str(info[4]))
        doc = doc.replace('arg5', str(info[5]))
        doc = doc.replace('arg6', str(info[8]))
        url = "https://www.xiaohongshu.com/user/profile/" + info[0]
        doc = doc.replace('arg7', url)
        doc = doc.encode('gbk', 'ignore')
        # print(doc)
        f.close()
        return doc


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
