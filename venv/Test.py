from selenium import webdriver
import os
import test_settings
chrome_path = r"D:\My Files\Project\MyFirstProject\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path) # Инициализация веб-драйвера
driver.maximize_window() #выставление максимального размера окна
driver.implicitly_wait(15)
driver.get("https://www.epicgames.com/") #переход на сайт
newpath = r"D:\\Test\\"+test_settings.test_day()+' TEST'
os.makedirs(newpath)
driver.get_screenshot_as_file(newpath+'\\'+test_settings.test_time()+'.png')
driver.find_element_by_xpath("//div[@id='user']").click()
driver.find_element_by_xpath("//a[@id='switchPageAction']").click()
driver.find_element_by_xpath("//input[@id='name']").send_keys("Тест")
driver.find_element_by_xpath("//input[@id='lastName']").send_keys("Тестовый")
driver.find_element_by_xpath("//input[@id='displayName']").send_keys("Selenium_test")
driver.find_element_by_xpath("//input[@id='email']").send_keys("test mail")
driver.find_element_by_xpath("//input[@id='password']").send_keys("testPassword1")
driver.find_element_by_xpath("//div[@class='checkContainer termsAgree filled']").click()
driver.find_element_by_xpath("//div[@class='btnContainer filled']").click()
assert "Введите действующий адрес электронной почты." in driver.page_source
driver.get_screenshot_as_file(newpath+'\\'+test_settings.test_time()+'.png')
driver.close()