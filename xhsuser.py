import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display

import webapi
import proxy

# display = Display(visible=0, size=(900, 800))
# display.start()
listnum = 0
# 设置ChromeOptions

chrome_options = Options()
prefs = {'profile.managed_default_content_settings.images': 2}  # 禁止加载图片
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('-–no-sandbox')
chrome_options.add_argument('-–disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')  # fix:DevToolsActivePort file doesn't exist
chrome_options.add_argument('--remote-debugging-port=9222')  # fix:DevToolsActivePort file doesn't
chrome_options.add_argument('--headless')  # 无界面模式
# proxy_addr = proxy.get_proxy_addr()
# print(proxy_addr)
# chrome_options.add_argument('--proxy-server=' + proxy_addr)
driver = webdriver.Chrome(options=chrome_options)

# 访问页面
retry = 0
while True:
    id = webapi.get_user()
    if id == -1:
        break
    url = "https://www.xiaohongshu.com/user/profile/" + id
    print(url)
    try:
        driver.get(url)
    except:
        print('WEB Driver crash')
        driver.close()
        chrome_options = Options()
        prefs = {'profile.managed_default_content_settings.images': 2}  # 禁止加载图片
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('-–no-sandbox')
        chrome_options.add_argument('-–disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')  # fix:DevToolsActivePort file doesn't exist
        chrome_options.add_argument('--remote-debugging-port=9222')  # fix:DevToolsActivePort file doesn't
        proxy_addr = proxy.get_proxy_addr()
        print(proxy_addr)
        chrome_options.add_argument('--proxy-server=' + proxy_addr)
        chrome_options.add_argument('--headless')  # 无界面模式
        driver = webdriver.Chrome(options=chrome_options)
        continue

    wait = WebDriverWait(driver, 2)

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "feeds-container")]')))

    except:
        # IP失效更换代理
        retry = retry + 1
        if retry < 2:
            driver.delete_all_cookies()
            driver.close()
            driver = webdriver.Chrome(options=chrome_options)
            print(str(retry) + ':获取失败重试')
            continue
        print('IP失效，更换新代理地址')
        driver.delete_all_cookies()
        driver.close()
        chrome_options = Options()
        my_prefs = {'profile.managed_default_content_settings.images': 2}  # 禁止加载图片
        chrome_options.add_experimental_option('prefs', my_prefs)
        chrome_options.add_argument('-–no-sandbox')
        chrome_options.add_argument('-–disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')  # fix:DevToolsActivePort file doesn't exist
        chrome_options.add_argument('--remote-debugging-port=9222')  # fix:DevToolsActivePort file doesn't
        proxy_addr = proxy.get_proxy_addr()
        print(proxy_addr)
        chrome_options.add_argument('--proxy-server=' + proxy_addr)
        chrome_options.add_argument('--headless')  # 无界面模式
        driver = webdriver.Chrome(options=chrome_options)
        retry = 0
        continue
    page_source = driver.page_source

    # file = open('doc.html', 'w', encoding='utf-8')
    # file.write(page_source)
    # file.close()

# 拉取博主数据
    soup = BeautifulSoup(page_source, 'html.parser')
    followers_tag = soup.find('div', class_='user-interactions')
    followers_count = followers_tag.find_all(class_='count')
    followers_num = followers_count[1].text.replace('W', '0000')
    followers_num = followers_num.replace('+', '')
    followers_num = followers_num.replace('k', '000')
    followers_num = followers_num.replace('K', '000')
    username = soup.find('span', class_='user-name').text
    # uid = soup.find(attrs={"name":"og:url"})['content'].replace('https://xiaohongshu.com/user/profile/', '')

    feed = soup.find('div', class_='feeds-container')
    feeds = feed.find_all(class_='count')
    desc = " "
    try:
        desc = soup.find('div', class_='user-desc').text
    except:
        print('No desc')

    # links = feed.find_all('a', class_='cover')
    count = 1
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0

# 拉取文章数据
    for a in feeds:
        # print(a.text)
        a = a.text.replace('W', '0000')
        a = a.replace('w', '0000')
        a = a.replace('k', '000')
        a = a.replace('K', '000')
        a = a.replace('+', '')
        if count == 1:
            p1 = a
        if count == 2:
            p2 = a
        if count == 3:
            p3 = a
        if count == 4:
            p4 = a
        count += 1

# 更新数据库数据
    if p1 != 0:
        listnum += 1
        webapi.update_user(username, followers_num, p1, p2, p3, p4, desc, id)
        print(str(listnum) + ':' + str(followers_num) + " " + username + " " + str(id) + " " + str(p1) + " " + str(
            p2) + " " + str(p3) + " " + str(p4))
    else:
        print('检查网络: %s,%s,%s,%s' % (p1, p2, p3, p4))

    time.sleep(0.6)

# 关闭web-driver
# driver.quit()
