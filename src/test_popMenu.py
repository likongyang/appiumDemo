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


