class Helpers():
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_xpath(self, path):
        try:
            self.driver.find_element_by_xpath(path).click()
        except Exception:
            print(2 + 2)
