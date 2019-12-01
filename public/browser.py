#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:选择浏览器
 @author: yansh
"""
import os.path
from selenium import webdriver
from public.log import Log
from public.readconfig import ReadConfig

log = Log()


class BrowserEngine(object):

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        read = ReadConfig()
        browser = read.getValue("browserType", "browserName")
        url = read.getValue("testServer", "URL")
        if browser == "Firefox":
            driver = webdriver.Firefox()
            log.info("启动{}浏览器".format(browser))
        elif browser == "Chrome":
            # driver = webdriver.Chrome(self.chrome_driver_path)
            driver = webdriver.Chrome()
            log.info("启动{}浏览器".format(browser))
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            log.info("启动{}浏览器".format(browser))
        driver.get(url)
        log.info("打开链接：{}".format(url))
        driver.maximize_window()
        log.info("最大化窗口")
        driver.implicitly_wait(10)
        log.info("隐式等待10s")
        return driver

    def quit_browser(self):
        log.info("退出浏览器驱动")
        self.driver.quit()

if __name__ == '__main__':
    # BrowserEngine().open_browser()
    print(os.path.join(os.path.abspath('..'), 'config', 'conf.ini'))