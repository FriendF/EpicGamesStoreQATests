import datetime

def test_day ():
    return datetime.datetime.now().strftime("%d-%m-%Y")

def test_time ():
    return datetime.datetime.now().strftime("%H-%M-%S")