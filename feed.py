from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options

import time
import webapi

chrome_options = Options()
prefs = {'profile.managed_default_content_settings.images': 2}  # 禁止加载图片
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('-–no-sandbox')
chrome_options.add_argument('-–disable-dev-shm-usage')

chrome_options.add_argument('--disable-gpu')  # fix:DevToolsActivePort file doesn't exist
chrome_options.add_argument('--remote-debugging-port=9222')  # fix:DevToolsActivePort file doesn't

# chrome_options.add_argument('--headless')  # 无界面模式

count = 0;
while True:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.xiaohongshu.com/explore")
    for i in range(1, 50):
        # 模拟鼠标操作
        actions = ActionChains(driver)
        actions.move_by_offset(5, 30)
        actions.click()
        actions.send_keys(Keys.PAGE_DOWN * 10)  # 向下滚动 10 页
        actions.release()
        actions.perform()
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        links = soup.find_all('a', class_='author')
        links = links[-20:]
        for link in links:
            # print(link['href'])
            uid = link['href'].replace('/user/profile/', '')
            count += int(webapi.insert_user(uid))
            print(str(count) + ':' + uid)
        num = len(links)
        if num < 1:
            print('get data failed')
        time.sleep(0.1)
    driver.close()
