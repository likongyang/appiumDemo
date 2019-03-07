#encoding=utf-8
import uiautomator as uiautomator
from appium import webdriver
import pytest
import unittest

from appium.webdriver.common.touch_action import TouchAction


class test_popmenu(unittest.TestCase):

    def setUp(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "popDemo"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["autoGrantPermissions"] = "true"
        caps["automationName"] = "UiAutomator2"
        # caps["newCommandTimeout"] = 600

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_pop(self):
        self.driver.find_element_by_xpath("//*[@text='Views']").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().className("android.widget.ListView").instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0))'
            ).click()
        self.driver.find_element_by_accessibility_id("Make a Popup!").click()
        self.driver.find_element_by_xpath("//*[@text='Search']").click()
        print(self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text)


    # # 封装一个滚动方法，swipe(item, director) return element
    # def swipe_new(self, item, director):
    #     print(self.driver.get_window_size())
    #     width = self.driver.get_window_size()['width']
    #     height = self.driver.get_window_size()['height']
    #     pgs = ["a", "a"]
    #
    #     #向上滑动并查找指定的元素
    #     if director == "up":
    #         while len(self.driver.find_elements(item['by'], item['value'])) < 1:
    #             self.driver.swipe(width / 2, height * 3/4, width / 2, height / 4, 1000)
    #             #判断是否滑动到底，如果是则返回None，如果不是则返回当前页面为第二次准备作比较
    #             pgs[0] = self.driver.page_source
    #             if pgs[0] == pgs[1]:
    #                 return None
    #             else:
    #                 pgs[1] = pgs[0]
    #         return self.driver.find_element(item['by'], item['value'])      #返回指定元素
    #
    #     # 向下滑动并查找指定的元素
    #     elif director == "down":
    #         while len(self.driver.find_elements(item['by'], item['value'])) < 1:
    #             self.driver.swipe(width / 2, height / 4, width / 2, height * 3/4, 1000)
    #             pgs[0] = self.driver.page_source
    #             if pgs[0] == pgs[1]:
    #                 return None
    #             else:
    #                 pgs[1] = pgs[0]
    #         return self.driver.find_element(item['by'], item['value'])
    #
    #     # 向左滑动并查找指定的元素
    #     elif director == "left":
    #         while len(self.driver.find_elements(item['by'], item['value'])) < 1:
    #             self.driver.swipe(width * 9/10, height / 2, width / 10, height / 2, 1000)
    #             pgs[0] = self.driver.page_source
    #             if pgs[0] == pgs[1]:
    #                 return None
    #             else:
    #                 pgs[1] = pgs[0]
    #         return self.driver.find_element(item['by'], item['value'])
    #
    #     # 向右滑动并查找指定的元素
    #     elif director == "right":
    #         while len(self.driver.find_elements(item['by'], item['value'])) < 1:
    #             self.driver.swipe(width / 4, height / 2, width * 3/4, height / 2, 1000)
    #             pgs[0] = self.driver.page_source
    #             if pgs[0] == pgs[1]:
    #                 return None
    #             else:
    #                 pgs[1] = pgs[0]
    #         return self.driver.find_element(item['by'], item['value'])
    #
    #     else:
    #         print("输入有误!")
    #         return None
