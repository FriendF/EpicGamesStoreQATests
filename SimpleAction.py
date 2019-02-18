import datetime


class TestSettings:
    def select_test_day():
        return datetime.datetime.now().strftime("%d-%m-%Y")

    def select_test_time():
        return datetime.datetime.now().strftime("%H-%M-%S")

    def CreatePath():
        path = r"D:\\Test\\" + TestSettings.select_test_day() + " - "
        return path

    def TakeScreenshot(path):
        screenpath = path + '\\' + TestSettings.select_test_time() + ".png"
        return screenpath
