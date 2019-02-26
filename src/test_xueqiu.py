#-*-coding:utf-8-*-

from appium import webdriver
import unittest
import pytest


class testXueqiu(unittest.TestCase):

    def setUp(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps["automationName"] = "UiAutomator2"
        # caps = {
        #     "platformName" : "android",
        #     "deviceName" : "demo",
        #     "appPackage" : "com.xueqiu.android",
        #     "appActivity" : ".view.WelcomeActivityAlias",
        #     "autoGrantPermissions" : "true",
        #     "automationName" : "UiAutomator2"
        # }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_add_pdd(self):
        self.driver.find_element_by_xpath("//*[contains(@text, '搜索股票')]").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("pdd")
        if len(self.driver.find_elements_by_id("follow_btn")) > 0:
            self.driver.find_element_by_id("follow_btn").click()
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()

    def test_pdd_exist(self):
        print("testcase 2")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        zixuanText = self.driver.find_element_by_id("com.xueqiu.android:id/portfolio_stockName").text
        assert zixuanText == "拼多多"
