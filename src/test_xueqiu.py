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
        self.driver.implicitly_wait(15)
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


    # 封装一个滚动方法，swipe(item, director) return element
    def swipe(self, item, director):
        if director == "up":
            pass
        elif director == "down":
            pass
        elif director == "left":
            pass
        else:
            pass

        return item
        # el = self.driver.find_element(by, director)
        # actions = TouchAction(self.driver)
        # actions.tap_and_hold(el)
        # actions.move_to(50, 50).perform()
        # return self


    # 交易 -> 基金 -> 已有蛋卷基金账户登录 -> 使用密码登陆 -> 输入用户名密码 -> 登录
    def test_sign_in(self):
        self.phoneNumber = 13512345678
        self.driver.find_element_by_xpath("//*[@text='交易' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_accessibility_id("15da75b0b27c24f3fee84026").click()
        self.driver.find_element_by_accessibility_id("已有蛋卷基金账户登录").click()
        self.driver.find_element_by_accessibility_id("使用密码登录").click()
        self.driver.find_element_by_accessibility_id("请输入手机号").send_keys(self.phoneNumber)
        self.driver.find_element_by_xpath("//*[contains(@content-desc, '登录密码')]/following-sibling::android.widget.EditText").send_keys("123456")
        self.driver.find_element_by_xpath("//*[contains(@content-desc, '登录密码')]/following-sibling::android.widget.EditText").click()
        self.driver.find_element_by_accessibility_id("安全登录").click()
        assert 1 == self.driver.find_elements_by_xpath("//*[contains(@text, '有误')]")



