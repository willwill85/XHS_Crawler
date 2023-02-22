小红书爬虫
===
文件说明
---
——————————————————————
# 爬虫机
## xhsuser.py
负责爬指定用户的相关信息
数据从服务中获得

## feed.py
feed流获得用户列表增加到云端数据

## proxy.py
获得代理服务器ip

## webapi.py
云端接口



——————————————————————
# 服务器
## webapp.py
云端的服务器，提供4个接口，利用Web.py框架实现
1. 添加用户
2. 更新用户
3. 获得需要爬的用户
4. 获得一个符合投放条件的用户

## db.py
数据库服务 SQLite

## list.html
前端展示页面

## db
db数据库，SQLite

表结构SQL：
CREATE TABLE USERS (
	id TEXT,
	name TEXT,
	fans INTEGER,
	p1 INTEGER,
	p2 INTEGER,
	p3 INTEGER,
	p4 INTEGER,
	ND INTEGER
, "desc" TEXT);

