from selenium import webdriver
from SimpleAction import TestSettings
import unittest
import os
from Helpers import Helpers


# import pytest
# import allure


class TestReg(unittest.TestCase):
    def setUp(self):
        chrome_path = r"D:\My Files\Project\MyFirstProject\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_path)  # Инициализация веб-драйвера
        self.driver.maximize_window()  # выставление максимального размера окна
        self.driver.implicitly_wait(15)

    def test_WrongMail(self):
        newpath = TestSettings.CreatePath() + "WrongMail"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        self.driver.get("https://www.epicgames.com/")  # переход на сайт
        self.driver.get_screenshot_as_file(TestSettings.TakeScreenshot(newpath))
        button = Helpers(self.driver)
        button.find_element_by_xpath("//div[@id='user']")
        # self.driver.find_element_by_xpath("//div[@id='user']").click()
        self.driver.find_element_by_xpath("//a[@id='switchPageAction']").click()
        self.driver.find_element_by_xpath("//input[@id='name']").send_keys("Тест")
        self.driver.find_element_by_xpath("//input[@id='lastName']").send_keys("Тестовый")
        self.driver.find_element_by_xpath("//input[@id='displayName']").send_keys("Selenium_test")
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys("test mail")
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("testPassword1")
        self.driver.find_element_by_xpath("//div[@class='checkContainer termsAgree filled']").click()
        self.driver.find_element_by_xpath("//div[@class='btnContainer filled']").click()
        assert "Введите действующий адрес электронной почты." in self.driver.page_source
        self.driver.get_screenshot_as_file(TestSettings.TakeScreenshot(newpath))

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
