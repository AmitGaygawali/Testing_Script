import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def OneTimeSetUp(request):
    driver = webdriver.Chrome(executable_path='C:\\Users\\gaiga\\OneDrive\\Desktop\\chromedriver88\\chromedriver.exe')
    driver.get("https://www.calculatestuff.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()