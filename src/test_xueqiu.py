#-*-coding:utf-8-*-

from appium import webdriver
import unittest
import pytest


class testXueqiu(unittest.TestCase):
    load = False

    def setUp(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps["automationName"] = "UiAutomator2"

        # if load == True:
        #     caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        load = True

    def loaded(self):
        waitCondition = ["x", "y"]
        while waitCondition[-1] != waitCondition[-2]:
            elLocation = self.driver.find_element_by_xpath("//*[@text='自选']").location
            waitCondition.append(elLocation)

    def test_add_pdd(self):
        self.loaded()
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("pdd")
        if len(self.driver.find_elements_by_id("com.xueqiu.android:id/follow_btn")) > 0:
            self.driver.find_element_by_id("com.xueqiu.android:id/follow_btn").click()
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()

    def test_pdd_exist(self):
        self.loaded()
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        elText = self.driver.find_element_by_id("com.xueqiu.android:id/portfolio_stockName")
        assert elText.text == "拼多多"

    def test_search_add(self):
        self.loaded()
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_id(
            "com.xueqiu.android:id/action_create_cube").click()
        self.driver.find_element_by_id(
            "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_id("com.xueqiu.android:id/follow_btn")
        self.driver.find_element_by_id("com.xueqiu.android:id/follow_btn").click()
        self.driver.find_element_by_xpath("//*[@text='下次再说']").click()
        print(self.driver.find_element_by_id("com.xueqiu.android:id/add_attention") \
              .find_element_by_class_name("android.widget.TextView").get_attribute("resource-id"))
        self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
        try:
            self.driver.find_element_by_id("com.xueqiu.android:id/iv_close").click()
        finally:
            elText = self.driver.find_element_by_id("com.xueqiu.android:id/portfolio_stockName")
            assert elText.text == "阿里巴巴"


