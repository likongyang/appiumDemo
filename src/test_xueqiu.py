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
        self.driver.implicitly_wait(8)
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


    # # 封装一个滚动方法，swipe(item, director) return element
    # def swipe_new(self, item, director):
    #     print(self.driver.get_window_size())
    #     width = self.driver.get_window_size()['width']
    #     height = self.driver.get_window_size()['height']
    #     pgs = ["a", "a"]
    #     if director == "up":
    #         while len(self.driver.find_elements(item['by'], item['value'])) < 1:
    #             self.driver.swipe(width / 2, height * 3/4, width / 2, height / 4, 1000)
    #             pgs[0] = self.driver.page_source
    #             if pgs[0] == pgs[1]:
    #                 return print("can't not find your elment")
    #             else:
    #                 pgs[1] = pgs[0]
    #         return self.driver.find_element(item['by'], item['value'])
    #
    #     elif director == "down":
    #         while len(self.driver.find_elements(item['by'], item['value'])) < 1:
    #             self.driver.swipe(width / 2, height / 4, width / 2, height * 3/4, 1000)
    #             pgs[0] = self.driver.page_source
    #             if pgs[0] == pgs[1]:
    #                 return print("can't not find your elment")
    #             else:
    #                 pgs[1] = pgs[0]
    #         return self.driver.find_element(item['by'], item['value'])
    #
    #
    #     elif director == "left":
    #         while len(self.driver.find_elements(item['by'], item['value'])) < 1:
    #             self.driver.swipe(width * 9/10, height / 2, width / 10, height / 2, 1000)
    #             pgs[0] = self.driver.page_source
    #             if pgs[0] == pgs[1]:
    #                 return print("can't not find your elment")
    #             else:
    #                 pgs[1] = pgs[0]
    #         return self.driver.find_element(item['by'], item['value'])
    #
    #     else:
    #         while len(self.driver.find_elements(item['by'], item['value'])) < 1:
    #             self.driver.swipe(width / 4, height / 2, width * 3/4, height / 2, 1000)
    #             pgs[0] = self.driver.page_source
    #             if pgs[0] == pgs[1]:
    #                 return print("can't not find your elment")
    #             else:
    #                 pgs[1] = pgs[0]
    #         return self.driver.find_element(item['by'], item['value'])


    # 封装一个滚动方法，swipe(item, director) return element
    def swipe_new(self, targetElement, director):
        print(self.driver.get_window_size())
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        pgs = ["", ""]

        #向上滑动并查找指定的元素
        if director == "up":
            while len(self.driver.find_elements(targetElement['by'], targetElement['value'])) < 1:
                self.driver.swipe(width / 2, height * 3/4, width / 2, height / 4, 1000)
                #判断是否滑动到底，如果是则返回None，如果不是则返回当前页面为第二次准备作比较
                pgs[0] = self.driver.page_source
                if pgs[0] == pgs[1]:
                    return None
                else:
                    pgs[1] = pgs[0]
            return self.driver.find_element(targetElement['by'], targetElement['value'])      #返回指定元素

        # 向下滑动并查找指定的元素
        elif director == "down":
            while len(self.driver.find_elements(targetElement['by'], targetElement['value'])) < 1:
                self.driver.swipe(width / 2, height / 4, width / 2, height * 3/4, 1000)
                pgs[0] = self.driver.page_source
                if pgs[0] == pgs[1]:
                    return None
                else:
                    pgs[1] = pgs[0]
            return self.driver.find_element(targetElement['by'], targetElement['value'])

        # 向左滑动并查找指定的元素
        elif director == "left":
            while len(self.driver.find_elements(targetElement['by'], targetElement['value'])) < 1:
                self.driver.swipe(width * 9/10, height / 2, width / 10, height / 2, 1000)
                pgs[0] = self.driver.page_source
                if pgs[0] == pgs[1]:
                    return None
                else:
                    pgs[1] = pgs[0]
            return self.driver.find_element(targetElement['by'], targetElement['value'])

        # 向右滑动并查找指定的元素
        elif director == "right":
            while len(self.driver.find_elements(targetElement['by'], targetElement['value'])) < 1:
                self.driver.swipe(width / 4, height / 2, width * 3/4, height / 2, 1000)
                pgs[0] = self.driver.page_source
                if pgs[0] == pgs[1]:
                    return None
                else:
                    pgs[1] = pgs[0]
            return self.driver.find_element(targetElement['by'], targetElement['value'])

        else:
            print("输入有误!")
            return None



    # 交易 -> 基金 -> 已有蛋卷基金账户登录 -> 使用密码登陆 -> 输入用户名密码 -> 登录
    def test_sign_in(self):
        self.phoneNumber = 13512345678
        self.driver.find_element_by_xpath("//*[@text='交易' and contains(@resource-id, 'tab_name')]").click()

        #emulator
        #self.driver.find_element_by_accessibility_id("15da75b0b27c24f3fee84026").click()
        #self.driver.find_element_by_accessibility_id("已有蛋卷基金账户登录").click()
        # self.driver.find_element_by_accessibility_id("使用密码登录").click()
        # self.driver.find_element_by_accessibility_id("请输入手机号").send_keys(self.phoneNumber)
        # self.driver.find_element_by_xpath("//*[contains(@content-desc, '登录密码')]/following-sibling::android.widget.EditText").send_keys("123456")
        # self.driver.find_element_by_xpath("//*[contains(@content-desc, '登录密码')]/following-sibling::android.widget.EditText").click()
        # self.driver.find_element_by_accessibility_id("安全登录").click()

        #mobile phone
        self.driver.find_element_by_xpath("//*[@text='15da75b0b27c24f3fee84026']").click()
        self.driver.find_element_by_xpath("//*[@text='已有蛋卷基金账户登录']").click()
        self.driver.find_element_by_xpath("//*[@text='使用密码登录']").click()
        self.driver.find_element_by_xpath("//*[@text='手机号']/following-sibling::android.widget.EditText").send_keys(self.phoneNumber)
        self.driver.find_element_by_xpath("//*[@text='登录密码']/following-sibling::android.widget.EditText").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@text='安全登录']").click()
        assert 1 == len(self.driver.find_elements_by_xpath("//*[contains(@text, '误')]"))
