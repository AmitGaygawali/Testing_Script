import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def OneTimeSetUp(request):
    driver = webdriver.Chrome(executable_path='D:\pycharm backup\cromedriver\chromedriver.exe')
    driver.get("www.demoblaze.com/")

    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()