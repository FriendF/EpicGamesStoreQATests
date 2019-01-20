import datetime

class TestSettings:
    def test_day():
        return datetime.datetime.now().strftime("%d-%m-%Y")

    def test_time():
        return datetime.datetime.now().strftime("%H-%M-%S")

    def CreatePath():
        path = r"D:\\Test\\"+TestSettings.test_day()+" - "
        return path

    def TakeScreenshot(path):
        screenpath = path+'\\' + TestSettings.test_time() + ".png"
        return screenpath







