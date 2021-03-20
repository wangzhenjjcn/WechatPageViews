#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import threading
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




def initDriver(chromeDriverFile,userDataPath):  
    driver=None 
    _userDataPath=userDataPath
    _chromeDriverFile=chromeDriverFile
    sysdir=os.path.dirname(os.path.realpath(sys.argv[0]))
    if not   os.path.exists(_chromeDriverFile) :
        print("chromeDriverFile not exist！")
        return
    if not   os.path.exists(_userDataPath) :
        print("userDataPath not exist！")
        _userDataPath=sysdir+"/tmp"
        if not   os.path.exists(_userDataPath) :
            os.makedirs(_userDataPath)

    _user_data_dir=_userDataPath+"/userdata"
    if not   os.path.exists(_user_data_dir) :
        os.makedirs(_user_data_dir)
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--user-data-dir=' + _user_data_dir)
        # chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--enable-javascript')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('-–single-process')
        # chrome_options.add_argument('blink-settings=imagesEnabled=false') 
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('window-size=1920x1080')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # self.Logger("     --disable-dev-shm-usage")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(
            chrome_options=chrome_options, executable_path=_chromeDriverFile)
        driver.set_page_load_timeout(8000) 
        driver.get("chrome://version/")
    except Exception as e:
        print(str(e))
    print("Chrome Ready...")
    return driver



if __name__ == "__main__":
    sysdir=os.path.dirname(os.path.realpath(sys.argv[0]))
    url="https://mp.weixin.qq.com/s/skrRciQHFgOmiTDV2TG0Ng" #要刷的页面
    chromeDriverFile=sysdir+"/chromedriver.exe" #驱动目录Linux为chromedriver
    userDataPath=sysdir+"/tmp" #用户目录
    sleepTime=3 #页面刷新等待时间
    total=99999 #循环次数
    webdriver=initDriver(chromeDriverFile,userDataPath)
    time.sleep(10)
    for t  in range(0,total):
        webdriver.get(url)
        print("Success: %s"%str(t))
        ActionChains(webdriver).key_down(Keys.HOME).perform()
        ActionChains(webdriver).key_down(Keys.DOWN).perform()
        ActionChains(webdriver).key_down(Keys.DOWN).perform()
        ActionChains(webdriver).key_down(Keys.DOWN).perform()
        time.sleep(1)
        ActionChains(webdriver).key_down(Keys.END).perform()
        time.sleep(1)
        ActionChains(webdriver).key_up(Keys.HOME).perform()
        webdriver.delete_all_cookies()
        time.sleep(int(sleepTime))


