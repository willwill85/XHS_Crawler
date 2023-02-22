import sqlite3


# 添加一个用户
def insert_user(userid):
    conn = sqlite3.connect('db')
    # 创建一个游标对象
    cursor = conn.cursor()
    user = (userid,)
    cursor.execute('SELECT * FROM USERS WHERE id=?', user)
    existing_user = cursor.fetchone()
    if existing_user is None:
        new_user = (userid, '1')
        cursor.execute('INSERT INTO USERS(id,ND) VALUES(?,?)', new_user)
        conn.commit()
        conn.close()
        return 1
    else:
        conn.close()
        return 0


# 随机获得一个没有爬过的用户
def get_user():
    conn = sqlite3.connect('db')
    # 创建一个游标对象
    cursor = conn.cursor()
    user = (1,)
    cursor.execute('SELECT * FROM USERS WHERE ND=? order by RANDOM() LIMIT 1', user)
    existing_user = cursor.fetchone()
    conn.close()

    if existing_user is None:
        return 0
    else:
        return existing_user[0]


# 更新用户的信息
def update_user(username, fans, p1, p2, p3, p4, desc, id):
    conn = sqlite3.connect('db')
    # 创建一个游标对象
    cursor = conn.cursor()
    user = (username, fans, p1, p2, p3, p4, desc, 0, id)
    cursor.execute('UPDATE USERS SET name=?,fans=?,p1=?,p2=?,p3=?,p4=?,desc=?,ND=? WHERE id=?', user)
    res = cursor.fetchone()
    conn.commit()
    conn.close()
    return res


# 随机获得一个可用的账号
def get_user_list():
    conn = sqlite3.connect('db')
    # 创建一个游标对象
    cursor = conn.cursor()
    cursor.execute('select * from USERS  where fans<10000 and p1>10 and p2>10 and p3>10 order by RANDOM() LIMIT 1')
    res = cursor.fetchone()
    conn.close()
    return res
# print(get_user())
